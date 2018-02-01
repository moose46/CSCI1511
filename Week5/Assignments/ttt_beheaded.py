# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent

import sys

sys.path.append('./')
import ttt_library as tttl
##from ttt_library import *

def main():
    tttl.display_instruct()
    computer, human = tttl.pieces()
    turn = tttl.X
    board = tttl.new_board()
    tttl.display_board(board)

    while not tttl.winner(board):
        if turn == human:
            move = tttl.human_move(board, human)
            board[move] = human
        else:
            move = tttl.computer_move(board, computer, human)
            board[move] = computer
        tttl.display_board(board)
        turn = tttl.next_turn(turn)

    the_winner = tttl.winner(board)
    tttl.congrat_winner(the_winner, computer, human)


# start the program
main()
input("\n\nPress the enter key to quit.")
