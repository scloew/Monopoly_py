"""
constants used throughout program
these maybe over written by utilizing from_file in board_builder
"""
#TODO get rid of this note when board_builder_has that functionality


class Constants:
    PASS_GO_BONUS = 2
    STARTING_MONEY = 35
    TAX = 2
    BATHROOM_TAX = 3
    TURN_LIMIT = 100
    BOARD_LENGTH = None

    CHANCE_ADD_MONEY = 'ADD_MONEY'
    CHANCE_MOVE = 'MOVE'
    CHANCE_SET_LOC = 'SET_LOCATION'

    PROP_PURCHASED = 'PURCHASED'
    GO_TO_BATHROOM = 'GO_TO_BATHROOM'
    ROLL_AGAIN = 'ROLL_AGAIN'
