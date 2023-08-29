"""
Here we introduce class Knight and enable its instances to fight each other.
"""
from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def fight(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        if self.hp < 0:
            self.hp = 0
        enemy.hp -= self.power - enemy.protection
        if enemy.hp < 0:
            enemy.hp = 0
