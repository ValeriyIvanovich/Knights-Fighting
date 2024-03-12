class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> str:
        return f"'{self.__class__.__name__}({self.name}, {self.power})'"
