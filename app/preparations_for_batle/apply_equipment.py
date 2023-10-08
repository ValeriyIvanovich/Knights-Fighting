class PrepareForBattle:
    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
