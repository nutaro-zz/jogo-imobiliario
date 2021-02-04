from players import Player
from proprietys import Propriety


class Player:

    def __init__(self, *args, **kwargs):
        self._money = 300
        self._owned_propriety = []

    @property
    def money(self):
        return self._money

    @property
    def owned_propriety(self) -> list:
        return self._owned_propriety

    def pay_rent(self, value: int, owner: Player) -> None:
        self._money -= value
        owner.receive_rent(value)

    def receive_rent(self, value: int) -> None:
        self._money += value

    def buy_property(self, propriety: Propriety) -> None:
        self._money -= propriety.cost
        self._owned_propriety.append(propriety)
        propriety.owner = self
