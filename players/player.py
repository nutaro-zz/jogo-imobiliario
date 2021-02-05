from proprieties import Propriety


class Player:

    def __init__(self, *args, **kwargs):
        self._money = 300
        self._owned_propriety = []
        self._position = 0

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, value: int) -> None:
        self._position = value

    @property
    def money(self) -> int:
        return self._money

    @money.setter
    def money(self, value: int) -> None:
        self._money = value

    @property
    def owned_propriety(self) -> list:
        return self._owned_propriety

    def pay_rent(self, value: int, owner) -> None:
        self._money -= value
        owner.receive_rent(value)

    def receive_rent(self, value: int) -> None:
        self._money += value

    def buy_propriety(self, propriety: Propriety) -> None:
        money_after_purchase = self.money - propriety.cost
        if money_after_purchase < 0:
            return
        self._money -= propriety.cost
        self._owned_propriety.append(propriety)
        propriety.owner = self
