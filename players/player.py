from players import Player


class Player:

    def __init__(self, *args, **kwargs):
        self.__money = 300
        self.__owned_propriety = []

    @property
    def money(self):
        return self.__money

    @property
    def owned_propriety(self) -> list:
        return self.__owned_propriety

    def pay_rent(self, value: int, owner: Player) -> None:
        self.__money -= value
        owner.receive_rent(value)

    def receive_rent(self, value: int) -> None:
        self.__money += value

    def buy_property(self, propriety: Propriety):
        self.__money -= propriety.cost
        self.__owned_propriety.append(propriety)
        propriety.owner = self
