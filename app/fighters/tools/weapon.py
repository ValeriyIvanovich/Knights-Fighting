class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


def get_weapon_instance(weapon: dict) -> Weapon:
    return Weapon(weapon["name"], weapon["power"])
