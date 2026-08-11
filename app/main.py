from fastapi import FastAPI
from pydantic import BaseModel
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.mocked import Mocked
from app.database.postgresql import PostgresDbConnection
from app.models.order import Order
from app.service.store_service import StoreService

import dotenv
dotenv.load_dotenv()  # Load environment variables from .env file


app = FastAPI()


# 1. Define the allowed origins
origins = [
    "http://localhost",
    "http://localhost:3000",  # Common React port
    "http://localhost:5173",  # Common Vite / Vue port
    "http://127.0.0.1:3000",  # Alternative local IP syntax
    "https://www.gabrielmeale.com.br",
    "https://gabrielthewalrus.github.io/merch-store"
]

# 2. Add the middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

CONNECTION_STRING = f"postgresql://postgres.aeymuhifmzcadduyavjl:{os.getenv('db_pass')}@aws-0-sa-east-1.pooler.supabase.com:5432/postgres"
#POSTGRES_CONNECTION = PostgresDbConnection(CONNECTION_STRING)
POSTGRES_CONNECTION = Mocked(CONNECTION_STRING)
MERCH_SERVICE = StoreService(POSTGRES_CONNECTION)


@app.get("/products")
def read_products():
    return MERCH_SERVICE.get_all_products()

@app.get("/products/{merch_id}")
def read_product(merch_id: int):
    return MERCH_SERVICE.get_product(merch_id)

@app.post("/order")
def create_order(order: Order):
    if not MERCH_SERVICE.validate_order(order):
        return {"status": "error", "message": "Invalid order data"}
    
    print(f"Received order: {order}")
    return MERCH_SERVICE.create_order(order)

@app.get("/shipping/{zipcode}")
def calculate_shipping(zipcode: str):
    shipping_price = MERCH_SERVICE.calculate_shipping(zipcode)
    return {"zipcode": zipcode, "shipping_price": shipping_price}

@app.post("/webhook/{order_id}/{payment_id}")
def handle_payment_webhook(order_id: str, payment: str):
    # Check if payment is "paid" or "failed" and update the order status accordingly
    if payment == "paid":
        # Update order status to "paid" in the database (mocked for now)
        print(f"Order {order_id} has been paid.")
    else:
        # Update order status to "failed" in the database (mocked for now)
        print(f"Payment for order {order_id} has failed.")
    return {"message": f"Webhook received for payment status: {payment}"}
