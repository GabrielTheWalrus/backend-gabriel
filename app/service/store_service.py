import re

from app.models.order import Order
from app.service.merch_service_interface import IMerchService
from app.models.product import Product


class StoreService(IMerchService):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_products(self) -> list[Product]:
        return self.db_connection.get_all_products()

    def get_product(self, merch_id: int) -> Product:
        return self.db_connection.get_product(merch_id)

    def create_order(self, order: Order) -> dict:
        return self.db_connection.create_order(order)

    def calculate_shipping(self, zipcode: str) -> float:
        # Mocked shipping calculation logic
        if zipcode.startswith("1"):
            return 10.0  # Example shipping price for zipcodes starting with '1'
        elif zipcode.startswith("2"):
            return 15.0  # Example shipping price for zipcodes starting with '2'
        else:
            return 20.0  # Default shipping price for other zipcodes

    def validate_order(self, order: Order) -> bool:
        cpf = re.sub(r"\D", "", order.customer.cpf)
        if not cpf or len(cpf) != 11:
            return False
        if "@" not in order.customer_email:
            return False
        if not order.customer_phone or len(re.sub(r"\D", "", order.customer_phone)) != 11:
            return False
        if not order.zipcode or len(re.sub(r"\D", "", order.zipcode)) != 8:
            return False
        if order.items:
            for order_item in order.items:
                item = self.get_product(order_item.product_id)
                if not item:
                    return False
                if order_item.quantity > item.stock:
                    return False
                if item.active is False:
                    return False
        return True
