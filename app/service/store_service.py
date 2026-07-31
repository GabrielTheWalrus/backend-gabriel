from app.service.merch_service_interface import IMerchService
from app.models.product import Product


class StoreService(IMerchService):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_products(self) -> list[Product]:
        return self.db_connection.get_all_products()

    def get_product(self, merch_id: int) -> Product:
        return self.db_connection.get_product(merch_id)
