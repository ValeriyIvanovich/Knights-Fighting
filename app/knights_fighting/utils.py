from knights_fighting.models import Knight


def create_knights(config: dict) -> dict:
    knights = {}
    for name, data in config.items():
        knights[name] = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data.get("potion"),
        )
    return knights


def battle(knights_config: dict) -> dict:
    knights = create_knights(knights_config)

    # 1 Lancelot vs Mordred
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)

    # 2 Arthur vs Red Knight
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]
    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
