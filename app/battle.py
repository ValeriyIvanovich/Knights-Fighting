from typing import Dict, List
from app.knight import Knight


class Battle:
    @staticmethod
    def simulate_battle(
            attacker: Knight,
            defender: Knight
    ) -> None:
        damage_to_defender = max(
            0, attacker.power - defender.protection
        )
        defender.hp -= damage_to_defender

    @staticmethod
    def run_battle(
            knight_1: Knight,
            knight_2: Knight
    ) -> None:
        Battle.simulate_battle(knight_1, knight_2)
        Battle.simulate_battle(knight_2, knight_1)

    @staticmethod
    def get_battle_results(
            knights: List[Knight]
    ) -> Dict[str, int]:
        return {knight.name: max(knight.hp, 0)
                for knight in knights}
