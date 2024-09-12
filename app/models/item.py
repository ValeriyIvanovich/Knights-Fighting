class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def get_power(self) -> int:
        return self.power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def get_protection(self) -> int:
        return self.protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def get_power(self) -> int:
        return self.effect["power"]

    def get_hp(self) -> int:
        return self.effect["hp"]

    def get_protection(self) -> int:
        return self.effect["protection"] if "protection" in self.effect else 0
