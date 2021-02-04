from .player import Player
from proprieties import Propriety


class ImpulsivePlayer(Player):

    def buy_propriety(self, propriety: Propriety) -> None:
        super().buy_propriety(propriety)
