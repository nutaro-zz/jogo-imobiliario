from players import Player


class Propriety:

    def __init__(self, cost: int, rent: int, **kwargs):
        self.__cost = cost
        self.__rent = rent
        self.__owner = None

