from __future__ import annotations

from app.warrior.equipment.armour import Armour
from app.warrior.equipment.potion import Potion
from app.warrior.equipment.weapon import Weapon


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = self.parse_armour(armour)
        self.protection = 0
        self.weapon = self.parse_weapon(weapon)
        self.potion = self.parse_potion(potion)

    def get_ready_to_battle(self) -> Knight:
        self.power += self.weapon.power

        if self.armour:
            for armour in self.armour:
                self.protection += armour.protection

        if self.potion:
            if self.potion.effect.get("power"):
                self.power += self.potion.effect.get("power")
            if self.potion.effect.get("hp"):
                self.hp += self.potion.effect.get("hp")
            if self.potion.effect.get("protection"):
                self.protection += self.potion.effect.get("protection")

        print(f"Knight {self.name} is ready to battle!")
        return self

    def fight(self, opponent: Knight) -> Knight:
        print(f"Knight {self.name} is fighting with {opponent.name}!")
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp < 0:
            self.hp = 0
        elif opponent.hp < 0:
            opponent.hp = 0

        winner = self if self.hp > opponent.hp else opponent
        print(f"Winner of the battle {winner.name}!")
        return winner

    @staticmethod
    def parse_armour(armour: list[dict]) -> list[Armour]:
        return [Armour(element["part"],
                       element["protection"]) for element in armour]

    @staticmethod
    def parse_weapon(weapon: dict) -> Weapon:
        return Weapon(**weapon)

    @staticmethod
    def parse_potion(potion: dict) -> Potion:
        return Potion(**potion) if potion else None
