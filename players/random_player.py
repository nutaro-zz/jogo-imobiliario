from random import randint

from players import Player
from proprietys import Propriety


class RandomPlayer(Player):

    def buy_propriety(self, propriety: Propriety) -> None:
        if randint(0, 1):
            super().buy_propriety(propriety)
