from src.common.constants import Constants
from src.common.player import Player
from src.inheritance.board import Board


class GameInstance:

    def __init__(self, players_names, board=None):
        self.board = board if board is not None else Board.from_default()
        self.players = [Player(name) for name in players_names]

    def play_game(self):
        turn_count = 0
        while turn_count < Constants.TURN_LIMIT:
            self.print_turn_status(turn_count)
            for p in self.players:
                bankrupt = self.take_turn(p)
                if bankrupt:
                    self.report_winners()
                    return None
                print()
            turn_count += 1

    def print_turn_status(self, turn_counter):
        delimiter = '================\n'
        print(f'{delimiter}Turn: {turn_counter}')
        print(delimiter[:-1])

        for player in self.players:
            print(f'{player.name} has {player.money} and is at square {player.loc}: {self.board.squares[player.loc]}')
        print(delimiter, ' \n')

    def take_turn(self, player):
        old_loc = player.loc
        new_loc = player.roll()
        # TODO this should use mod operator
        roll = new_loc - old_loc if old_loc < new_loc else (old_loc + new_loc) % len(self.board.squares)
        print(
            f'{player.name} rolls {roll} and moves to {self.board.squares[new_loc]}')
        status = self.board.squares[new_loc].action(player)
        print(f'{player.name} now has {player.money}')
        if status == Constants.ROLL_AGAIN:
            self.take_turn(player)
        elif status == Constants.GO_TO_BATHROOM:
            player.loc = self.board.bathroom_loc
            self.board.squares[player.loc].action(player)
        elif new_loc < old_loc and not status == Constants.CHANCE_MOVE:
            player.add_money(Constants.PASS_GO_BONUS)
        elif status == Constants.PROP_PURCHASED:
            self.board.monopolies[new_loc].check_monopoly()
        return player.is_broke()

    def report_winners(self):
        max_money = max((p.money for p in self.players))
        print('====\nWINNERS\n====\n')
        losers = []
        for player in self.players:
            if player.money == max_money:
                print(f'{player} wins with ${player.money}')
            else:
                losers.append(player.name)
        print('====\nLosers\n====\n')
        print('\n'.join(losers))
