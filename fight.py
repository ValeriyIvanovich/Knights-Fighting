from app.KNIGHTS.knight import Knight


def fight(knight1: "Knight", knight2: "Knight") -> None:
    knight1.potion_activate()
    knight2.potion_activate()
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    if knight1.hp < 0:
        knight1.hp = 0
    if knight2.hp < 0:
        knight2.hp = 0
