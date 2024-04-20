from __future__ import annotations
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour
from app.equipment.potion import Potion


class Fighter:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int

    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_armour(self, armour_list: list[Armour]) -> None:
        for armour in armour_list:
            self.protection += armour.protection

    def apply_potion(self, potion: Potion) -> None:
        self.power += potion.power
        self.hp += potion.hp
        self.protection += potion.protection

    def battle(self, opponent: Fighter) -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp < 0:
            self.hp = 0

        if opponent.hp < 0:
            opponent.hp = 0
