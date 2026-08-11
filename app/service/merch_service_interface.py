from abc import ABC, abstractmethod
from app.models.order import Order
from app.models.product import Product


class IMerchService(ABC):

    @abstractmethod
    def get_all_products(self) -> list[Product]:
        pass

    @abstractmethod
    def get_product(self, merch_id: int) -> Product:
        pass

    @abstractmethod
    def create_order(self, order: Order) -> dict:
        pass

    @abstractmethod
    def calculate_shipping(self, zipcode: str) -> float:
        pass
