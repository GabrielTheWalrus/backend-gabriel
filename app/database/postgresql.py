from app.database.db_connection_interface import IDbConnection
from app.models.order import Order
from app.models.product import Product


class PostgresDbConnection(IDbConnection):

    def __init__(self, connection_string: str):
        import psycopg2
        self.connection_string = connection_string
        self.connection = psycopg2.connect(connection_string)

    def get_all_products(self) -> list[Product]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM public.tb_products")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        products = [dict(zip(column_names, row)) for row in rows]
        return [Product(**product_data) for product_data in products]

    def get_product(self, merch_id: int) -> Product:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM public.tb_products WHERE id = %s", (merch_id,))
        row = cursor.fetchone()
        if row:
            column_names = [desc[0] for desc in cursor.description]
            product_data = dict(zip(column_names, row))
            return Product(**product_data)
        else:
            return None

    def create_order(self, order: Order) -> dict:
        pass
