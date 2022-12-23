def apply_armour(fighter: dict) -> None:
    fighter["protection"] = 0
    for armour in fighter["armour"]:
        fighter["protection"] += armour["protection"]
