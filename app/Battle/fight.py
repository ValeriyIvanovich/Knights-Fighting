class Fight:
    def __init__(self, knight1: dict, knight2: dict) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def battle(self) -> dict:
        self.knight1["hp"] -= \
            (self.knight2["power"] - self.knight1["protection"])
        self.knight2["hp"] -= \
            (self.knight1["power"] - self.knight2["protection"])

        # check if someone fell in battle
        if self.knight1["hp"] <= 0:
            self.knight1["hp"] = 0

        if self.knight2["hp"] <= 0:
            self.knight2["hp"] = 0

        # Return battle results:
        return {
            self.knight1["name"]: self.knight1["hp"],
            self.knight2["name"]: self.knight2["hp"]
        }
