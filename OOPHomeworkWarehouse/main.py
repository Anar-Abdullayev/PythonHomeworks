from functools import reduce

import pandas as pd
from dataclasses import dataclass
from types import MappingProxyType


@dataclass
class InventoryItem:
    name: str
    quantity: int
    price: float

    def __post_init__(self):
        if self.quantity < 0 or self.price < 0:
            raise ValueError("Quantity or price cannot be negative")


class Warehouse:
    __slots__ = ("__items",)

    def __init__(self):
        self.__items: dict[str, InventoryItem] = {}

    @property
    def items(self):
        return MappingProxyType(self.__items)

    def add_item(self, item: InventoryItem):
        if item.name in self.__items:
            existing = self.__items[item.name]
            existing.quantity += item.quantity
        else:
            self.__items[item.name] = InventoryItem(item.name, item.quantity, item.price)

    def remove_item(self, name: str, quantity: int | None = None):
        if name not in self.__items:
            raise KeyError(f"Item '{name}' not found in warehouse")

        if quantity is None or quantity >= self.__items[name].quantity:
            del self.__items[name]
        else:
            self.__items[name].quantity -= quantity

    def total_value(self) -> float:
        total = reduce(
            lambda x, item: x + (item.price * item.quantity),
            self.__items.values(),
            0
        )
        return total

    def load_from_excel(self, filepath: str):
        df = pd.read_excel(filepath)

        for _, row in df.iterrows():
            item = InventoryItem(
                name=row["name"],
                quantity=int(row["qty"]),
                price=float(row["price"])
            )
            self.add_item(item)

    def from_csv(self, path: str):
        df = pd.read_csv(path)

        for _, row in df.iterrows():
            self.add_item(InventoryItem(
                name=row["name"],
                quantity=int(row["qty"]),
                price=float(row["price"])
            ))

    def __str__(self):
        lines = []
        for item in self.__items.values():
            lines.append(f"{item.name}: qty={item.quantity}, price={item.price}")
        return "\n".join(lines)


warehouse = Warehouse()
warehouse.load_from_excel("warehouse.xlsx")
print(warehouse)
print(warehouse.total_value())
