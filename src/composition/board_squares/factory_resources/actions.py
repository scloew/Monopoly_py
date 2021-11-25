from random import choice

from ....common.constants import *


def bathroom_action(self, player):
    player.add_money(-Constants.TAX)
    self.print_message(player)


def chance_action(self, player):
    action = choice((Constants.CHANCE_MOVE, Constants.CHANCE_ADD_MONEY))
    if action == Constants.CHANCE_ADD_MONEY:
        money = choice(range(-5, 6))
        player.add_money(money)
        self.print_msg = f'chance contributes ${money} to {player}'


def go_square_action(self, player):
    player.add_money(Constants.PASS_GO_BONUS)
    self.print_message(player)


# TODO does this need to call print_message?
def go_to_bathroom_action(self, player):
    return Constants.GoToBathRoom


def loose_change_action(self, player):
    player.add_money(self.money_pot)
    self.print_message(player)
    self.money_pot = 0
    return None


def property_square_action(self, player):
    if self.owner is None:
        if player.money > self.cost:
            self.owner = player
            player.add_money(-self.cost)
            self.print_message(player)
            self.print_lambda = lambda plyr: f'and pays {self.cost} to {self.owner}' \
                if not self.owner == player else ''
            return Constants.PROP_PURCHASED
    self.print_message(player)
    self.owner.add_money(self.cost)
    player.add_money(-self.cost)
    return None


def railroad_action(self, player):
    self.print_message(player)
    return Constants.ROLL_AGAIN


def tax_action(self, player):
    player.add_money(-Constants.TAX)
    self.loose_change.add_money(Constants.TAX)
    self.print_message(player)
