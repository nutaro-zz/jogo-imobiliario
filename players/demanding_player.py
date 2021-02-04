from players import Player
from proprietys import Propriety


class DemandingPlayer(Player):

    def buy_propriety(self, propriety: Propriety) -> None:
        if propriety.rent <= 50:
            return
        super().buy_propriety(propriety)
