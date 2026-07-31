from fastapi import FastAPI
from pydantic import BaseModel
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.postgresql import PostgresDbConnection
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
POSTGRES_CONNECTION = PostgresDbConnection(CONNECTION_STRING)
MERCH_SERVICE = StoreService(POSTGRES_CONNECTION)


@app.get("/products")
def read_products():
    return MERCH_SERVICE.get_all_products()

@app.get("/products/{merch_id}")
def read_product(merch_id: int):
    return MERCH_SERVICE.get_product(merch_id)
