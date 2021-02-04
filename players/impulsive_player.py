from players import Player
from proprietys import Propriety


class ImpulsivePlayer(Player):

    def buy_propriety(self, propriety: Propriety) -> None:
        super().buy_propriety(propriety)
