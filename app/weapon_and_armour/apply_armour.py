class ApplyArmour:
    def __init__(self, knights_config: dict) -> None:
        self.knights_config = knights_config
        self.knights_config["protection"] = 0
        for part_of_armour in self.knights_config["armour"]:
            self.knights_config["protection"] += part_of_armour["protection"]
