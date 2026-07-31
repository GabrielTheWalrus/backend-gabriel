#  {"color": "blue", "size": "L", "material": "cotton", "qty": 5},
class Placeholder:
    def __init__(self, color: str, size: str, material: str, qty: int):
        self.color = color
        self.size = size
        self.material = material
        self.qty = qty

    def to_dict(self):
        return {
            "color": self.color,
            "size": self.size,
            "material": self.material,
            "qty": self.qty
        }

class Product:
    def __init__(self, id: str, name: str, desc: str, price: float, images: list[str], placeholder: Placeholder, active: bool):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.images = images
        self.placeholder = Placeholder(**placeholder)
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "price": self.price,
            "images": self.images,
            "placeholder": self.placeholder,
            "active": self.active
        }