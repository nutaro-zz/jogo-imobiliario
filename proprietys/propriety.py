from players import Player


class Propriety:

    def __init__(self, cost: int, rent: int, **kwargs):
        self.__cost = cost
        self.__rent = rent
        self.__owner = None

    @property
    def cost(self) -> int:
        return self.__cost

    @property
    def rent(self) -> int:
        return self.__rent

    @property
    def owner(self) -> Player:
        return self.__owner

    @owner.setter
    def owner(self, value: Player) -> None:
        if self.has_owner():
            raise ValueError("Propriety has owner")
        self.__owner = value

    def has_owner(self) -> bool:
        return self.__owner is not None
