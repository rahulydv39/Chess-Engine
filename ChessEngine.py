# This class os responsible for storing all the information about the current state of a chess.
# It will also be responsible for determining the valid moves at the current state. It will also keep a move log.


class GameState():
    def __init__(self):
        #board is an 8x8 2d list, each elements of the list has 2 characters.
        #The first charecter represents the color of the piece, 'b' or 'w'
        #The second charecter represents the type of the piece, 'k' , 'Q', 'R', 'B', 'N' or 'P'
        #"--" - represints an empty space with no pieces.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]

        ]

        self.whiteMove = True
        self.moveLog = []