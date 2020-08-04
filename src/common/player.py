from random import randint, choice
from string import ascii_letters, digits, punctuation

from .constants import Constants


class Player:
    """
    a Player class for text verions of monopoly junior
    the player does not make decisions as logic for this
    exercise is predefined
    """

    def __init__(self, name=None):
        if not name:
            chars = ascii_letters+digits+punctuation
            self.name = ''.join((choice(chars) for _ in range(randint(5, 20))))
        else:
            self.name = name
        self.money = Constants.STARTING_MONEY
        self.loc = 0

    def is_broke(self):
        return self.money > 0

    def add_money(self, amt):
        self.money += amt

    def __str__(self):
        return f'{self.name}: {self.money}'

    @classmethod
    def roll(cls):
        return randint(1, 7)
