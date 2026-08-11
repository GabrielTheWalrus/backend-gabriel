from app.database.db_connection_interface import IDbConnection
from app.models.order import Order
from app.models.product import Product


class Mocked(IDbConnection):
    def __init__(self, connection_string: str):
        pass         
 
    def get_all_products(self) -> list[Product]:
            products = [
                {
                    "id": "1",
                    "name": "Get Born, Stay Born",
                    "desc": "Camiseta - Preta - Algodão",
                    "price": 49.90,
                    "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/camiseta-get-born-stay-born-preta.png"],
                    "placeholder": {"color": "red", "size": "M", "material": "cotton", "qty": 10},
                    "active": True,
                    "tags": ["t-shirt"],
                    "order": 2
                },
                {
                    "id": "2",
                    "name": "Get Born, Stay Born",
                    "desc": "Camiseta - Branca - Algodão",
                    "price": 49.90,
                    "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/camiseta-get-born-stay-born-branco.png"],
                    "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                    "active": True,
                    "tags": ["t-shirt"],
                    "order": 3
                },
                {
                    "id": "3",
                    "name": "Get Born, Stay Born",
                    "desc": "Palheta - Delrin - Branca .88mm",
                    "price": 9.90,
                    "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-branca-frente-get-born-stay-born.png", "https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-branca-verso-get-born-stay-born.png"],
                    "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                    "active": True,
                    "tags": ["pick"],
                    "order": 5
                },
                {
                    "id": "4",
                    "name": "Get Born, Stay Born",
                    "desc": "Palheta - Delrin - Preta 1.08mm",
                    "price": 9.90,
                    "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-preto-frente-get-born-stay-born.png", "https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-preto-verso-get-born-stay-born.png"],
                    "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                    "active": True,
                    "tags": ["pick"],
                    "order": 6
                },
                {
                    "id": "5",
                    "name": "Get Born, Stay Born",
                    "desc": "Caneca branca 325ml - Cerâmica",
                    "price": 39.90,
                    "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/caneca-get-born-stay-born.png"],
                    "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                    "active": True,
                    "tags": ["mug"],
                    "order": 4
                },
                {
                    "id": "6",
                    "name": "Get Born, Stay Born",
                    "desc": "CD - Digipack - 2025",
                    "price": 29.90,
                    "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/cd-get-born-stay-born-front.png", "https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/cd-get-born-stay-born-back.png"],
                    "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                    "active": True,
                    "tags": ["cd"],
                    "order": 1
                },
            ]
            return sorted([Product(**product_data) for product_data in products], key=lambda p: p.order)
    
    def get_product(self, merch_id: int) -> Product:
        # mocked
        product_data = {
            "id": str(merch_id),
            "name": f"Product {merch_id}",
            "desc": f"Description for Product {merch_id}",
            "price": 19.99 + merch_id,
            "images": [f"image{merch_id}.jpg"],
            "placeholder": {"color": "green", "size": "S", "material": "cotton", "qty": 15},
            "active": True
        }
        return Product(**product_data)

    def create_order(self, order: Order) -> dict:
        # Mocked order creation logic
        return {
            "status": "success",
            "message": "Order created successfully",
            "order_details": order.model_dump()
        }   