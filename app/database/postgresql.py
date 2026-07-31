from app.database.db_connection_interface import IDbConnection
from app.models.product import Product


class PostgresDbConnection(IDbConnection):

    def __init__(self, connection_string: str):
        import psycopg2
        self.connection_string = connection_string
        self.connection = psycopg2.connect(connection_string)

    # mocked
    def get_all_products(self) -> list[Product]:
        products = [
            {
                "id": "1",
                "name": "Get Born, Stay Born",
                "desc": "Camiseta - Preta - Algodão",
                "price": 49.90,
                "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/camiseta-get-born-stay-born-preta.png"],
                "placeholder": {"color": "red", "size": "M", "material": "cotton", "qty": 10},
                "active": True
            },
            {
                "id": "2",
                "name": "Get Born, Stay Born",
                "desc": "Camiseta - Branca - Algodão",
                "price": 49.90,
                "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/camiseta-get-born-stay-born-branco.png"],
                "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                "active": True
            },
            {
                "id": "3",
                "name": "Get Born, Stay Born",
                "desc": "Palheta - Delrin - Branca .88mm",
                "price": 9.90,
                "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-branca-frente-get-born-stay-born.png", "https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-branca-verso-get-born-stay-born.png"],
                "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                "active": True
            },
            {
                "id": "4",
                "name": "Get Born, Stay Born",
                "desc": "Palheta - Delrin - Preta 1.08mm",
                "price": 9.90,
                "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-preto-frente-get-born-stay-born.png", "https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/palheta-preto-verso-get-born-stay-born.png"],
                "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                "active": True
            },
            {
                "id": "5",
                "name": "Get Born, Stay Born",
                "desc": "Caneca branca 325ml - Cerâmica",
                "price": 39.90,
                "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/caneca-get-born-stay-born.png"],
                "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                "active": True
            },
            {
                "id": "6",
                "name": "Get Born, Stay Born",
                "desc": "CD - Digipack - 2025",
                "price": 29.90,
                "images": ["https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/cd-get-born-stay-born-front.png", "https://aeymuhifmzcadduyavjl.supabase.co/storage/v1/object/public/product-images/cd-get-born-stay-born-back.png"],
                "placeholder": {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
                "active": True
            },
        ]
        return [Product(**product_data) for product_data in products]

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

    # def get_all_products(self) -> list[Product]:
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM public.tb_products")
    #     rows = cursor.fetchall()
    #     column_names = [desc[0] for desc in cursor.description]
    #     products = [dict(zip(column_names, row)) for row in rows]
    #     return [Product(**product_data) for product_data in products]

    # def get_product(self, merch_id: int) -> Product:
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM public.tb_products WHERE id = %s", (merch_id,))
    #     row = cursor.fetchone()
    #     if row:
    #         column_names = [desc[0] for desc in cursor.description]
    #         product_data = dict(zip(column_names, row))
    #         return Product(**product_data)
    #     else:
    #         return None
