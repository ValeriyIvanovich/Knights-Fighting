from app.weapon import Weapon
from app.armour import Armour
from app.potion import Potion
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


def battle(knightsconfig: dict) -> dict:
    weapon = Weapon(knightsconfig)
    weapon_score = weapon.weapon_score()
    armour = Armour(weapon_score)
    armor_score = armour.armor_score()
    potion = Potion(armor_score)
    finished_dict = potion.potion_score()
    lancelot = finished_dict["lancelot"]
    mordred = finished_dict["mordred"]
    arthur = finished_dict["arthur"]
    red_knight = finished_dict["red_knight"]
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]
    for i in finished_dict:
        if finished_dict[i]["hp"] < 0:
            finished_dict[i]["hp"] = 0
    return {lancelot["name"]: lancelot["hp"],
            arthur["name"]: arthur["hp"],
            mordred["name"]: mordred["hp"],
            red_knight["name"]: red_knight["hp"],
            }
