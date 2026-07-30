from fastapi import FastAPI
from pydantic import BaseModel
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. Define the allowed origins
origins = [
    "http://localhost",
    "http://localhost:3000",  # Common React port
    "http://localhost:5173",  # Common Vite / Vue port
    "http://127.0.0.1:3000",  # Alternative local IP syntax
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

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


def get_products_from_db():
    import psycopg2

    query = "SELECT * FROM public.tb_products"

    try:
        # 1. Connect to your PostgreSQL database
        connection = psycopg2.connect(CONNECTION_STRING)
        
        # 2. Open a cursor to perform database operations
        cursor = connection.cursor()
        
        # 3. Execute a SQL query
        cursor.execute(query)
        
        # 4. Fetch all rows from the result set
        rows = cursor.fetchall()
        
        # 5. Process and return the results
        column_names = [desc[0] for desc in cursor.description]
        
        products = [dict(zip(column_names, row)) for row in rows]
        return products

    except Exception as error:
        print(f"Error connecting to database: {error}")
        return []

    finally:
        # 6. Always close the cursor and connection when done
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


@app.get("/products")
def read_products():
    return get_products_from_db()
