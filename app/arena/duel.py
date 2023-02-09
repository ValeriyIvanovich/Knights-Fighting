from random import choice
from app.king_garden.knights import Knight


def duel(knight: Knight, enemy: Knight) -> None:
    print("Knights approaching the battlefield...")
    print("......................................")
    print("......................................")
    print("......................................")

    print(f"{knight.name.capitalize()} {choice(duel_approach())}")
    print("......................................")
    print(f"{enemy.name.capitalize()} {choice(duel_approach())}")
    print("**************************************")
    print(f"Suddenly {choice([knight, enemy])} runs on his enemy!!!")
    print("And the fight has started...")
    knight.fight_enemy(enemy)
    enemy.fight_enemy(knight)

    for visav in (knight, enemy):
        hp_check(visav)
    print("......................................")
    print("......................................")
    print("......................................")
    print("......................................")
    print("......................................")
    print(".......................some time later")
    print("Battle was glorious(lul), but result is result")


def duel_approach() -> list[str]:
    greetings = [
        "is pretty friendly today, he's smiling wide!",
        "not in a best mood, his helmet is already down...",
        "shining like a bright sun with a devilish smile ]:>",
        "is extremely hard... Seems like we see waves around him.",
    ]
    return greetings


def hp_check(knight: Knight) -> None:
    if knight.hp < 0:
        knight.hp = 0
