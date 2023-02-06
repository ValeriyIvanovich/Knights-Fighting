from app.knights import Knight


class Arena:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> dict:
        knight1.hp -= knight2.power
        knight2.hp -= knight1.power
        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0
        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        }
