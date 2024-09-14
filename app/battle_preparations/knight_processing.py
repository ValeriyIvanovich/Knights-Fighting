from knight_constructor import Knight


def process_knight(knight_data) -> Knight:
    knight = Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        armour=knight_data["armour"],
        weapon=knight_data["weapon"],
        potion=knight_data["potion"]
    )

    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()

    return knight
