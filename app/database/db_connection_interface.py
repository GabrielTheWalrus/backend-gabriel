from abc import ABC, abstractmethod
from app.models.product import Product


class IDbConnection(ABC):

    @abstractmethod
    def get_all_products(self) -> list[Product]:
        pass

    @abstractmethod
    def get_product(self, merch_id: int) -> Product:
        pass
