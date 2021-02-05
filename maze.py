from random import randint

from players import Player
from proprieties import Propriety


class Maze:

    def __init__(self, proprieties: list, players: list):
        self._size = len(proprieties)
        self._propriety = proprieties
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

    @property
    def winner(self) -> Player:
        winner = None
        for player in self.players:
            if winner is None:
                winner = player
                continue
            if player.money > winner.money:
                winner = player
        return winner

    @property
    def players(self) -> list:
        return self._players

    def run(self):
        for x in range(0, self._max_rounds):
            losers = []
            self.round_number = x + 1
            for count, player in enumerate(self.players):
                self.move_player(player)
                index = player.position - 1
                self.handle_propriety(player, self._propriety[index])
                if player.money < 0:
                    self.remove_proprieties(player)
                    losers.append(count)
            self.remove_players(losers)
            if len(self.players) == 1:
                break
        else:
            self.time_out = True

    def remove_players(self, losers: list) -> None:
        losers.sort(reverse=True)
        for x in losers:
            self.players.pop(x)

    @staticmethod
    def remove_proprieties(player: Player) -> None:
        for propriety in player.owned_propriety:
            propriety.owner = None

    def move_player(self, player: Player) -> None:
        new_position = player.position + randint(1, 6)
        if new_position > len(self._propriety):
            new_position -= len(self._propriety)
            player.money = player.money + 100
        player.position = new_position

    @staticmethod
    def handle_propriety(player: Player, propriety: Propriety) -> None:
        if propriety.has_owner():
            player.pay_rent(propriety.rent, propriety.owner)
            return
        if not propriety.has_owner():
            player.buy_propriety(propriety)
