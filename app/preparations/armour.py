def apply_armour(knight: dict) -> int:
    knight["protection"] = 0
    for element in knight["armour"]:
        knight["protection"] += element["protection"]
    return knight["protection"]
