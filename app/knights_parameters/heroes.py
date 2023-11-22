from .models_knights import KnightsParameters

lancelot = KnightsParameters(
    name="Lancelot",
    power=35,
    hp=100,
    armor=[],
    weapon={"name": "Metal Sword",
            "power": 50,
            },
    potion=None
)
arthur = KnightsParameters(
    name="Arthur",
    power=45,
    hp=75,
    armor=[
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
    weapon={
        "name": "Two-handed Sword",
        "power": 55,
    },
    potion=None
)
mordred = KnightsParameters(
    name="Mordred",
    power=30,
    hp=90,
    armor=[
        {
            "part": "breastplate",
            "protection": 15,
        },
        {
            "part": "boots",
            "protection": 10,
        }
    ],
    weapon={
        "name": "Poisoned Sword",
        "power": 60
    },
    potion={
        "name": "Berserk",
        "effect": {
            "hp": -5,
            "power": +15,
            "protection": +10,
        }
    }
)
red_knight = KnightsParameters(
    name="Red Knight",
    power=40,
    hp=70,
    armor=[
        {
            "part": "breastplate",
            "protection": 25,
        }
    ],
    weapon={
        "name": "Sword",
        "power": 45
    },
    potion={
        "name": "Blessing",
        "effect": {
            "hp": +10,
            "power": +5,
        }
    }
)

knights = [lancelot, red_knight, mordred, arthur]
