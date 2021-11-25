from ....common.constants import *


def bathroom_print_message(self, player):
    print(f'{player.name} lands on {self.name}')


def chance_print_message(self):
    print(self.print_msg)


def go_square_print_message(self, player):
    print(f'{player} lands on go and collects ${Constants.PASS_GO_BONUS}')


def go_to_bathroom_print_message(self, player):
    print(f'{player} moves to bathroom')


def print_message(self, player):
    print(f'{player.name} lands on {self.name} and gains ${self.money_pot}')
