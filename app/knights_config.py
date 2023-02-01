from __future__ import annotations


class KnightInfo:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def using_armour(self, armour: list) -> int:
        for part in armour:
            self.hp += part["protection"]
        return self.hp

    def using_weapon(self, weapon: int) -> int:
        self.power += weapon
        return self.power

    def using_potion(self, potion: dict) -> callable:
        if potion is not None:
            if potion["effect"].get("power"):
                self.power += potion["effect"]["power"]
            if potion["effect"].get("hp"):
                self.hp += potion["effect"]["hp"]
            if potion["effect"].get("protection"):
                self.hp += potion["effect"]["protection"]
        return self.power, self.hp
