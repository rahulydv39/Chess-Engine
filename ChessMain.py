# This is our main driver file . It will be responseble for handling user input and dispalying the GameState Object.

from os import path
import pygame as p
import ChessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8  # DIMENSION OF CHESS BORAD 8X8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animation later on
IMAGES = {}

'''
Initialize a global dictonary of images . This will be exactly once in the main.
'''

def LoadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
The main driver for our code. This will handle user input and upadting the graphics.
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)
    LoadImages()  # only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        # ✅ FIXED: Indented inside the while loop
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
responsible for all the graphics within a current game state
'''
def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the bord
    drawPieces(screen, gs.board)  # draw pieces on the top of those squares


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            # ✅ FIXED: p.draw.rect (lowercase) + p.Rect (uppercase) + 4 arguments
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]

            if piece != "--":
                screen.blit(
                    IMAGES[piece],
                    p.Rect(
                        col * SQ_SIZE,
                        row * SQ_SIZE,
                        SQ_SIZE,
                        SQ_SIZE
                    )
                )


if __name__ == "__main__":
    main()