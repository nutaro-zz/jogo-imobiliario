from players import Player

class Player:

    def __init__(self, *args, **kwargs):
        self.__money = 300
        self.__owned_property = []

    @property
    def money(self):
        return self.__money

    @property
    def owned_property(self) -> list:
        return self.__owned_property

    def pay_rent(self, value: int, owner: Player) -> None:
        self.__money -= value
        owner.receive_rent(value)

    def receive_rent(self, value: int) -> None:
        self.__money += value

    def buy_property(self, property: Property):
        self.__money -= property.cost
        self.__owned_property.append(property)
