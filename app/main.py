from app.Ammunition.armours import Armour
from app.Heroes.knights import Knight
from app.Ammunition.potions import Potion
from app.Ammunition.weapons import Weapon


def create_knight(config: dict) -> Knight:
    name = config["name"]
    power = config["power"]
    health = config["hp"]
    weapon = Weapon(config["weapon"]["name"],
                    config["weapon"]["power"])
    armour = []
    for _armour in config["armour"]:
        armour.append(Armour(_armour["part"], _armour["protection"]))
    potion = config["potion"]
    if potion is not None:
        effect = potion["effect"]
        potion = Potion(potion["name"],
                        effect.get("power", 0),
                        effect.get("hp", 0),
                        effect.get("protection", 0))
    return Knight(name, power, health, weapon, armour, potion)


def health_update(knight: Knight) -> None:
    if knight.health < 0:
        knight.health = 0


def royal_battle(fighter_1: Knight, fighter_2: Knight) -> None:
    fighter_1.health -= fighter_2.power - fighter_1.protection
    fighter_2.health -= fighter_1.power - fighter_2.protection
    health_update(fighter_1)
    health_update(fighter_2)


def battle(knights_config: dict) -> dict:
    knights = {
        knight: create_knight(knights_config[knight])
        for knight in knights_config
    }
    for knight in knights:
        knights[knight].potion_increasing()

    royal_battle(knights["lancelot"], knights["mordred"])
    royal_battle(knights["arthur"], knights["red_knight"])

    return {
        knights[knight].name: knights[knight].health
        for knight in knights
    }
