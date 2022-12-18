from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 protection: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def __sub__(self, other: Knight) -> Knight:
        self.hp -= other.power - self.protection
        return self

    @staticmethod
    def check_hp_knight(hp: int) -> int:
        if hp <= 0:
            hp = 0
        return hp
