from app.potion import Potion


class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self.weapon_dict = weapon_dict

    def weapon_score(self) -> dict:
        for key, value in self.weapon_dict.items():
            if value["weapon"]:
                value["power"] +=\
                    value["weapon"]["power"]
        potion = Potion(self.weapon_dict)
        return potion.potion_score()
