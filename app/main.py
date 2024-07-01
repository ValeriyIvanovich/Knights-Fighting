from app.warrior import Knight
from app.konfig_warrior import (sort_through_armour,
                                sort_weapon,
                                sort_the_potion)
from app.battle_konfig import battle_knights

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
    list_warrior = []
    for knight in knights_config.values():
        warrior = Knight(name=knight["name"],
                         power=knight["power"],
                         hp=knight["hp"], )
        if knight["armour"]:
            warrior.protection = sort_through_armour(knight["armour"])
        warrior.power += sort_weapon(knight["weapon"])
        if not knight["potion"] is None:
            effect = sort_the_potion(knight["potion"]["effect"],
                                     warrior.power,
                                     warrior.hp,
                                     warrior.protection)
            warrior.power = effect[0]
            warrior.hp = effect[1]
            warrior.protection = effect[2]
        list_warrior.append(warrior)
    return battle_knights(list_warrior)


print(battle(KNIGHTS))
