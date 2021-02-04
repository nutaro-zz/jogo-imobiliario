from random import randint

from .player import Player
from proprieties import Propriety


class RandomPlayer(Player):

    def buy_propriety(self, propriety: Propriety) -> None:
        if randint(0, 1):
            super().buy_propriety(propriety)
