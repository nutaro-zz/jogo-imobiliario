from random import randint

from players import Player
from proprietys import Propriety


class Maze:

    def __int__(self, propriety: list, players: list):
        self._size = len(propriety)
        self._propriety = propriety
        self._players = players
        self._round_number = 0
        self._max_rounds = 1000
        self.time_out = False

    @property
    def round_number(self) -> int:
        return self._round_number

    @round_number.setter
    def round_number(self, value: int) -> None:
        self._round_number = value

    def run(self):
        for x in range(0, self._max_rounds):
            self.round_number = x + 1
            if len(self._players) == 1:
                break
            for count, player in enumerate(self._players):
                self.move_player(player)
                index = player.position - 1
                self.handle_propriety(player, self._propriety[index])
                if player.money < 0:
                    del self._players[count]
        else:
            self.time_out = True

    @staticmethod
    def move_player(player: Player) -> None:
        steps = randint(1, 6)
        new_position = player.position + steps
        if new_position > 20:
            new_position -= 20
        player.position = new_position

    @staticmethod
    def handle_propriety(player: Player, propriety: Propriety) -> None:
        if propriety.has_owner():
            player.pay_rent(propriety.rent, propriety.owner)
            return
        player.buy_propriety(propriety)
