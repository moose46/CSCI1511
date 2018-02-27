"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: tic-tac-toe-robertcurtiss
 -Created: Feb, 06, 2018
Description:
                   Chapter 6
"""
# global constants
X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 9


def askTheYNQuestion(question):
    """Ask for a response of y or n"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def displayTheBoard(board):
    """display the board on the screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "-" * 9)
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "-" * 9)
    print("\t", board[6], "|", board[7], "|", board[8])


def displayInstructions():
    """Display the instructions of the game on the screen"""
    print("""
	Good luck to you, tic-tic-toe is my game!
	A showdown with my silicon brain :) and your mushy brain :(!
	You will make your move know by entering a number: 0 - 8.
	The number will correspond to the board position as illustrated.
	""")


def askForNumber(question, low, high):
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except Exception as ex:
            pass
    return response


def whoGoesFirst():
    pass


def legalMoves(board: object) -> object:
    """Create a list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 6),
        (2, 4, 6)
    )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner  # found a winner, return the tuple
    if EMPTY not in board:
        return TIE  # found a tie game
    return None  # no one has won yet



def computerMove(board, computer, human):
    """ Computer move"""
    board = board[:]  # make a copy of the board
    # best moves in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")
    # if the computer can winn take that move
    for move in legalMoves(board):
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
    # check to see if mushy can win
    for move in legalMoves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move undo it
        board[move] = EMPTY
    # since no one can win on next move, pick the best open square
    for move in BEST_MOVES:
        if move in legalMoves(board):
            print(move)
            return move

    pass


def humanMove(board, human):
    """ get the human move """
    legal = legalMoves(board)
    move = None
    while move not in legal:
        move = askForNumber("Hey mushy, what's your next choice? (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nWell mushy, your brain is mush, that square is already taken, ha ha ha!")
    print("OK...")
    return move


def nextTurn(turn):
    """ Switch turns"""
    if turn == X:
        return O
    else:
        return X


# congratulates the winner
def contratsWinner(theWinner, computer, human):
    """ Congratulate the winner """
    if theWinner != TIE:
        print(theWinner, "Won!\n")
    else:
        print("It's a tie!\n")
    if theWinner == computer:
        print("As I predicted, mushy, I am triumphant once more.\n")
    elif theWinner == human:
        print("Well well mushy, stop taking the smart pills please!\n")
    elif theWinner == TIE:
        print("Mushy got lucky, next time you are mine!\n")


def newBoard():
    # create a new board
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


# determines who goes first
def pieces():
    # determines if player or computer goes first
    goFirst = askTheYNQuestion("Do you want the first move, mushy? (y/n)")
    if goFirst == "y":
        print("\nThen you can have the first move mushy. You will need it!")
        human = X
        computer = O
    else:
        print("\nYou are brave, mushy... I will go first.")
        human = O
        computer = X
    return computer, human


# askForNumber("Enter you guess mushy (0-8): ", 0, 8)

# print(pieces())

def main():
    displayInstructions()
    computer, human = pieces()
    turn = X

    board = newBoard()
    displayTheBoard(board)
    while not winner(board):
        if turn == human:
            move = humanMove(board, human)
            board[move] = human
        else:
            move = computerMove(board, computer, human)
            board[move] = computer
        displayTheBoard(board)
        turn = nextTurn(turn)
    theWinner = winner(board)
    contratsWinner(theWinner, computer, human)


# main program start
main()
input("\nPress enter to continue: ")
