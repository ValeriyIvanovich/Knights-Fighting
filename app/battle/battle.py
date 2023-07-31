from app.knight.knight import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def fight(self) -> dict:
        self.knight_1.hp -= self.knight_2.power - self.knight_1.protection
        self.knight_2.hp -= self.knight_1.power - self.knight_2.protection

        self.knight_1.hp = max(self.knight_1.hp, 0)
        self.knight_2.hp = max(self.knight_2.hp, 0)

        return {
            self.knight_1.name: self.knight_1.hp,
            self.knight_2.name: self.knight_2.hp
        }
