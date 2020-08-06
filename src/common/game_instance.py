from src.inheritance.board import Board
from src.common.player import Player
from src.common.constants import Constants


class GameInstance:

    def __init__(self, players_names, board=None):
        self.board = board if board is not None else Board.from_default()
        self.players = [Player(name) for name in players_names]

    def play_game(self):
        turn_count = 0
        while turn_count < Constants.TURN_LIMIT:
            for p in self.players:
                bankrupt = self.take_turn(p)
                if bankrupt:
                    self.report_winners
                    return None
            turn_count += 1

    def take_turn(self, player):
        old_loc = player.loc
        new_loc = player.roll()
        status = self.board.squares[new_loc].action(player)
        if status == Constants.ROLL_AGAIN:
            self.take_turn(player)
        elif status == Constants.GO_TO_BATHROOM:
            player.loc = self.board.bathroom_loc
        elif new_loc < old_loc and status not in Constants.CHANCE_MOVE:
            player.add_money(Constants.PASS_GO_BONUS)
        elif status == Constants.PROP_PURCHASED:
            self.board.monopolies[new_loc].check_monopoly()
        return player.is_broke()

    def report_winners(self):
        max_money = max((p.money for p in self.players))
        print('====\nWINNERS\n====\n')
        losers = []
        for p in self.players:
            if p.money == max_money:
                print(p)
            else:
                losers.append(p.name)
        print('====\nLosers\n====\n')
        print('\n'.join(losers))