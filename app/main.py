from app.heroes.knight import Knight
from app.helpers.data_transform import transform_to_knight


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
    },
}


def get_knight(knight_name: str, knight_battlers: dict) -> Knight:
    return transform_to_knight(knight_battlers[knight_name])


def knight_duel(first_knight: Knight, second_knight: Knight) -> dict:
    first_knight.battle_preparations()
    second_knight.battle_preparations()
    first_knight.strike_opponent(second_knight)
    second_knight.strike_opponent(first_knight)

    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp
    }


def battle(knight_battlers: dict) -> dict:
    # 1 fight
    lancelot = get_knight(
        knight_name="lancelot",
        knight_battlers=knight_battlers
    )
    mordred = get_knight(
        knight_name="mordred",
        knight_battlers=knight_battlers
    )

    # 2 fight
    arthur = get_knight(
        knight_name="arthur",
        knight_battlers=knight_battlers
    )
    red_knight = get_knight(
        knight_name="red_knight",
        knight_battlers=knight_battlers
    )

    return {
        **knight_duel(lancelot, mordred),
        **knight_duel(arthur, red_knight),
    }


print(battle(KNIGHTS))
