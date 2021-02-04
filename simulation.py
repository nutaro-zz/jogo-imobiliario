from collections import defaultdict

from maze import Maze
from players import Player, CautiousPlayer, DemandingPlayer, ImpulsivePlayer, RandomPlayer
from proprieties import Propriety


propriety_values = [(65, 25), (90, 52), (100, 60), (50, 10), (50, 20), (85, 40), (125, 70),
                    (70, 35), (80, 35), (90, 55), (70, 30), (78, 24), (80, 30), (100, 60),
                    (80, 40), (90, 60), (120, 70), (40, 10), (62, 35), (80, 40)]


def build_proprieties() -> list:
    proprieties = []
    for value in propriety_values:
        propriety = Propriety(value[0], value[1])
        proprieties.append(propriety)
    return proprieties


def build_players() -> list:
    players = [ImpulsivePlayer(), DemandingPlayer(),
               CautiousPlayer, RandomPlayer]
    return players


def define_winner(players: list) -> Player:
    if len(players) == 1:
        return players[0]


def simulate() -> None:
    score = defaultdict(int)
    round_amount = 0
    for x in range(0, 300):
        proprieties = build_proprieties()
        players = build_players()
        maze = Maze(proprieties, players)
        maze.run()
        winner = define_winner()
        score[type(winner).__name__] += 1