from app.heroes.knight import Knight
from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = battle_prepare(knights_config)
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    # check if someone fell in battle
    for knight in knights.values():
        knight.check_hp()

    # Return battle results:
    return {knight.name: knight.hp for knight in knights.values()}


def battle_prepare(knights_config: dict) -> dict[str, Knight]:
    knights = {}
    for name, properties in knights_config.items():
        knight = create_knight(properties["name"], properties)
        if properties["armour"]:
            armours = [
                create_armour(armour) for armour in properties["armour"]
            ]
            knight.set_protection(armours)
        weapon = create_weapon(properties["weapon"])
        knight.increase_power(weapon)
        if properties["potion"]:
            potion = create_potion(properties["potion"])
            knight.set_effect(potion)
        knights[name] = knight

    return knights


def create_knight(name: str, propertires: dict) -> Knight:
    return Knight(name, propertires["power"], propertires["hp"])


def create_armour(armour: dict) -> Armour:
    return Armour(armour["part"], armour["protection"])


def create_weapon(weapon: dict) -> Weapon:
    return Weapon(weapon["name"], weapon["power"])


def create_potion(potion: dict) -> Potion:
    return Potion(potion["name"], potion["effect"])


print(battle(KNIGHTS))
