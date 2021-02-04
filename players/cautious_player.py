from player import Player
from proprietys import Propriety


class CautiousPlayer(Player):

    def buy_propriety(self, propriety: Propriety) -> None:
        money_after_purchase = self.money - propriety.cost
        if money_after_purchase >= 80:
            super().buy_propriety(propriety)
