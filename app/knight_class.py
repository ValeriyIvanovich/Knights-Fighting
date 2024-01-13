from __future__ import annotations


class Knight:
    knights_statistics = {}

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.protection = knight["protection"]
        self.power = knight["power"]

    def fight(self, other: Knight) -> None:
        self.hp = max(self.hp - (other.power - self.protection), 0)
        other.hp = max(other.hp - (self.power - other.protection), 0)

    @classmethod
    def get_statistics(cls, knights: dict[str, Knight]) -> dict:
        cls.knights_statistics = {
            knight.name: knight.hp
            for knight in knights.values()
        }
        return cls.knights_statistics
