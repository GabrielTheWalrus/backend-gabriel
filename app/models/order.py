from datetime import datetime

from pydantic import BaseModel


class Items(BaseModel):
    product_id: str
    quantity: int
    price: float


class Order(BaseModel):
    id: str
    customer_name: str
    customer_email: str
    customer_phone: str
    cpf: str
    address: str
    city: str
    state: str
    zipcode: str 
    shipping_price: float = 0.0
    total_price: float = 0.0
    payment_type: str 
    payment_status: str = "pending"
    order_status: str = "pending"
    created_at: str = datetime.now().isoformat()
    items: Items
