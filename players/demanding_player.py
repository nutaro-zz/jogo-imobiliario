from players import Player
from proprietys import Propriety


class DemandingPlayer(Player):

    def buy_propriety(self, propriety: Propriety) -> None:
        if propriety.rent > 50:
            super().buy_propriety(propriety)
