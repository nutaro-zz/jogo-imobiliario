from collections import defaultdict

from maze import Maze
from players import Player, CautiousPlayer, DemandingPlayer, ImpulsivePlayer, RandomPlayer
from proprieties import Propriety


propriety_values = [(160, 55), (170, 52), (180, 60), (90, 25), (170, 65), (120, 40), (160, 70),
                    (140, 35), (130, 35), (170, 55), (120, 30), (140, 30), (155, 55), (140, 35),
                    (180, 60), (150, 45), (150, 70), (180, 55), (150, 55), (110, 35)]


def build_proprieties() -> list:
    proprieties = []
    for value in propriety_values:
        propriety = Propriety(value[0], value[1])
        proprieties.append(propriety)
    return proprieties


def build_players() -> list:
    players = [ImpulsivePlayer(), DemandingPlayer(),
               CautiousPlayer(), RandomPlayer()]
    return players


def calculate_winner_behavior(score: dict) -> str:
    winner = {"name": None, "matches": 0}
    for player in score:
        won_matches = score[player]
        if winner["matches"] < won_matches:
            winner['name'] = player
            winner['matches'] = won_matches
    return winner["name"]


def calculate_percentage(score: dict, number_of_rounds: int) -> dict:
    percentage = defaultdict(int)
    for player in score:
        won_rounds = score[player] * 100
        percentage[player] = won_rounds / number_of_rounds
    return percentage


def print_percentage(percentage: dict) -> None:
    for player in percentage:
        print(f"The {player} won {percentage[player]}% of the matches")


def simulate() -> None:
    score = defaultdict(int)
    round_amount = 0
    time_out = 0
    for x in range(0, 300):
        maze = Maze(build_proprieties(), build_players())
        maze.run()
        score[type(maze.winner).__name__] += 1
        round_amount += maze.round_number
        if maze.time_out:
            time_out += 1
    winner_behavior = calculate_winner_behavior(score)
    average = round_amount / 300
    print()
    print_percentage(calculate_percentage(score, 300))
    print()
    print(f"The behavior that won more matches was {winner_behavior}\n")
    print(f"The average rounds is {average}\n")
    print(f"Timeout matches {time_out}")


if __name__ == '__main__':
    simulate()
