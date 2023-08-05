class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = 0
        self.calculate_stats()

    def calculate_stats(self) -> None:
        # Calculate the protection and power for the knight
        self.protection = sum(part["protection"] for part in self.armour)
        self.power = self.base_power + self.weapon["power"]
        if self.potion:
            self.apply_potion_effects()

    def apply_potion_effects(self) -> None:
        # Apply potion effects to the knight's power, protection, and HP
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]
        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]
        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]


class Battle:
    @staticmethod
    def simulate_battle(attacker, defender) -> None:
        # Simulate battle between an attacker and a defender
        damage_to_defender = max(0, attacker.power - defender.protection)
        defender.hp -= damage_to_defender

    @staticmethod
    def run_battle(knight1, knight2) -> None:
        # Run a battle between two knights
        Battle.simulate_battle(knight1, knight2)
        Battle.simulate_battle(knight2, knight1)

    @staticmethod
    def get_battle_results(knights) -> dict:
        # Get the battle results for all knights
        return {knight.name: max(knight.hp, 0) for knight in knights}


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


def battle(knights):
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights["lancelot"]

    # apply armour
    lancelot["protection"] = 0
    for a in lancelot["armour"]:
        lancelot["protection"] += a["protection"]

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            lancelot["protection"] += lancelot["potion"]["effect"]["protection"]

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    # arthur
    arthur = knights["arthur"]

    # apply armour
    arthur["protection"] = 0
    for a in arthur["armour"]:
        arthur["protection"] += a["protection"]

    # apply weapon
    arthur["power"] += arthur["weapon"]["power"]

    # apply potion if exist
    if arthur["potion"] is not None:
        if "power" in arthur["potion"]["effect"]:
            arthur["power"] += arthur["potion"]["effect"]["power"]

        if "protection" in arthur["potion"]["effect"]:
            arthur["protection"] += arthur["potion"]["effect"]["protection"]

        if "hp" in arthur["potion"]["effect"]:
            arthur["hp"] += arthur["potion"]["effect"]["hp"]

    # mordred
    mordred = knights["mordred"]

    # apply armour
    mordred["protection"] = 0
    for a in mordred["armour"]:
        mordred["protection"] += a["protection"]

    # apply weapon
    mordred["power"] += mordred["weapon"]["power"]

    # apply potion if exist
    if mordred["potion"] is not None:
        if "power" in mordred["potion"]["effect"]:
            mordred["power"] += mordred["potion"]["effect"]["power"]

        if "protection" in mordred["potion"]["effect"]:
            mordred["protection"] += mordred["potion"]["effect"]["protection"]

        if "hp" in mordred["potion"]["effect"]:
            mordred["hp"] += mordred["potion"]["effect"]["hp"]

    # red_knight
    red_knight = knights["red_knight"]

    # apply armour
    red_knight["protection"] = 0
    for a in red_knight["armour"]:
        red_knight["protection"] += a["protection"]

    # apply weapon
    red_knight["power"] += red_knight["weapon"]["power"]

    # apply potion if exist
    if red_knight["potion"] is not None:
        if "power" in red_knight["potion"]["effect"]:
            red_knight["power"] += red_knight["potion"]["effect"]["power"]

        if "protection" in red_knight["potion"]["effect"]:
            red_knight["protection"] += red_knight["potion"]["effect"]["protection"]

        if "hp" in red_knight["potion"]["effect"]:
            red_knight["hp"] += red_knight["potion"]["effect"]["hp"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


def battle_main(config):
    # Create instances of the Knight class using the provided configuration
    lancelot = Knight(**config["lancelot"])
    arthur = Knight(**config["arthur"])
    mordred = Knight(**config["mordred"])
    red_knight = Knight(**config["red_knight"])

    # Simulate battles between pairs of knights
    Battle.run_battle(lancelot, mordred)
    Battle.run_battle(arthur, red_knight)

    # Get and return the battle results for all knights
    return Battle.get_battle_results([lancelot, arthur, mordred, red_knight])


# Run the main battle function with the provided knight data
print(battle(KNIGHTS))
