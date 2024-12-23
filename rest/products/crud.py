import random
import string
from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    name: str
    price: int


@dataclass
class ProductsStorage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    @property
    def names(self) -> set[str]:
        return {product.name for product in self.products.values()}

    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)

    def add(self, product_name: str, product_price: int) -> Product:
        product = Product(
            id=self.next_id,
            name=product_name,
            price=product_price,
        )
        self.products[product.id] = product
        return product

    def update(
        self,
        product_id: int,
        product_name: str,
        product_price: int,
    ) -> Product:
        product = self.products[product_id]
        product.name = product_name
        product.price = product_price
        return product

    def delete(self, product_id: int) -> None:
        self.products.pop(product_id, None)

    def get_list(self) -> list[Product]:
        return list(self.products.values())

    def check_names(self) -> list[str]:
        product_names = [product.name for product in self.products.values()]
        return product_names

    def name_exists(self, product_name: str) -> bool:
        return product_name in self.names


products_storage = ProductsStorage()

# products_storage.add(
#     "Laptop",
#     1299,
# )
#
# products_storage.add(
#     "Desktop",
#     1999,
# )
#
# products_storage.add(
#     "Smartphone",
#     999,
# )

for idx in range(1, 61):
    random_suffix = "".join(random.choices(string.ascii_letters, k=4))
    product_name = f"product-{idx:03d} {random_suffix}"
    product_price = random.randint(1, 9) * random.choice([10, 50, 100, 200, 500])
    products_storage.add(
        product_name=product_name,
        product_price=product_price,
    )
