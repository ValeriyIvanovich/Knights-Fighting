from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.knight import Knight


def battle(knights_config: dict) -> dict[str, int]:
    knights = create_knights(knights_config)
    for knight in knights:
        knight.use_potion()

    return fight(*knights)


def create_knights(knights_config: dict) -> list:
    return [
        Knight(
            stats["name"],
            stats["power"],
            stats["hp"],
            Armour.create_armours(stats["armour"]),
            Weapon.create_weapon(stats["weapon"]),
            Potion.create_potion(stats["potion"])
        )
        for stats in knights_config.values()
    ]


def fight(
        lancelot: Knight,
        arthur: Knight,
        mordred: Knight,
        red_knight: Knight
) -> dict[str, int]:
    # Lancelot vs Mordred
    lancelot.duel_battle(mordred)
    mordred.duel_battle(lancelot)

    # Arthur vs Red Knight
    arthur.duel_battle(red_knight)
    red_knight.duel_battle(arthur)

    return {
        knight.name: knight.hp
        for knight in [lancelot, arthur, mordred, red_knight]
    }
