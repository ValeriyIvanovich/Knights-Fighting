from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict | None,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection
        self.battle_preparation()

    def battle_preparation(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            for effect in self.potion["effect"]:
                if effect == "power":
                    self.power += self.potion["effect"]["power"]
                if effect == "protection":
                    self.protection += self.potion["effect"]["protection"]
                if effect == "hp":
                    self.hp += self.potion["effect"]["hp"]

    def fight(self, defender: Knight) -> None:
        damage = max(0, self.power - defender.protection)
        defender.hp = max(0, defender.hp - damage)
