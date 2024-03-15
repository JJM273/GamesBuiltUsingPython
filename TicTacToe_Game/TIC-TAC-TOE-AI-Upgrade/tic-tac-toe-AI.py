"""
TIC TAC TOE - ADVANCED
Author: Tushar Nankani
Contributor: Jay Morehart

Specifications:
2 players will be able to play the game (both sitting at the same computer);
The board will be printed out every time a player makes a move
THIS ADVANCED VERSION WILL ALSO PRINT A BOARD SIMULTANEOUSLY: STATING THE REMAINING MOVES.

"""
# Standard Imports
import random

# Third Party Imports

# Local Imports


#FUNCTIONS;

def default():
    """
	To be printed as Default;
    """
    print("\nWelcome! Let's play TIC TAC TOE!\n")


def display_rules():
    """display the rules"""
    print("The board will look like this!")
    print("The positions of this 3 x 3 board is same as the right side of your key board.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position(1-9).")


def play():
    """Asking if the player is ready"""
    return input("\nAre you ready to play the game? Enter [Y]es or [N]o.\t").upper().startswith('Y')


def get_names(p2: str = None):
    """Player names input"""
    p1 = input("\nEnter NAME of PLAYER 1:\t").capitalize()
    if p2 is None:
        p2 = input("Enter NAME of PLAYER 2:\t").capitalize()
    return (p1, p2)


def get_mark_choice():
    """Player choice input"""
    p1 = ' '
    p2 = ' '
    while p1 != 'X' or p1 != 'O':          #while loop; if the entered value isn't X or O;

        #WHILE LOOP STARTS

        p1 = input(f"\n{p1_name}, Do you want to be X or O?\t")[0].upper()
        #The input above has [0].upper() in the end
        #So the user can enter x, X, xxxx or XXX; the input will always be taken as X
        #Thereby, increasing the user input window

        if p1 == 'X' or p1 == 'O':
            #if entered value is X or O; get out of the loop
            break
        print("INVALID INPUT! Please Try Again!")
        #if the entered value isn't X or O, re-run the while loop

        #WHILE LOOP ENDS
    #Assigning the value to p2 and then diplaying the values
    if p1 == 'X':
        p2 = 'O'
    elif p1 == 'O':
        p2 = 'X'

    return (p1, p2)



def choose_first_player():
    """This function will randomly decide who will go first"""
    return random.choice((0, 1))


def display_board(board, avail):
    """display the board"""
    print("    " + " {} | {} | {} ".format(board[7],board[8],board[9]) + "            " + " {} | {} | {} ".format(avail[7],avail[8],avail[9]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4],board[5],board[6]) + "            " + " {} | {} | {} ".format(avail[4],avail[5],avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1],board[2],board[3]) + "            " + " {} | {} | {} ".format(avail[1],avail[2],avail[3]))


def player_choice(board, name, choice):
    """get player choice"""
    pos = 0
    #Initialising position as 0^; so it passes through the while loop
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board, pos):
        pos = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) \t'))

        if pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board, pos) or pos == "":
            #To check whether the given position is in the set [1-9] or whether it is empty or occupied;
            print("INVALID INPUT. Please Try Again!\n")
    print("\n")
    return pos


# THIS IS THEFUNCTION WHERE AI IS ADDED:
def ai_choice(board):
    """feed the "AI" a board and get its choice
    this is just randomly selecting a position from the first availible group:
    corners > Center > edges
    """
    pos = 0
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    # including both X and O, since if computer will win, he will place a choice there, but if the component will win --> we have to block that move
    for letter in ['O', 'X']:
        for i in possibilities:
            # Creating a copy of the board everytime, placing the move and checking if it wins;
            # Creating a copy like this  and not this boardCopy = board, since changes to boardCopy changes the original board;
            board_copy = board[:]
            board_copy[i] = letter
            if win_check(board_copy, letter):
                pos = i
                return pos

    open_corners = [x for x in possibilities if x in [1, 3, 7, 9]]

    if len(open_corners) > 0:
        pos = select_random(open_corners)
        return pos

    if 5 in possibilities:
        pos = 5
        return pos

    open_edges = [x for x in possibilities if x in [2, 4, 6, 8]]

    if len(open_edges) > 0:
        pos = select_random(open_edges)
        return pos



def select_random(board):
    """random spot on board"""
    ln = len(board)
    r = random.randrange(0,ln)
    return board[r]


def place_marker(board, avail, choice, pos):
    """To mark/replace the position on the board list"""
    board[pos] = choice
    avail[pos] = ' '


def space_check(board, pos):
    """To check whether the given position is empty or occupied;"""
    return board[pos] == ' '


def full_board_check(board):
    """To check if the board is full, then the game is a draw;"""
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def win_check(board, choice):
    """check if a win condition is true"""
    #To check if one of the following patterns are true; then the respective player has won!;
    #HORIZONTAL CHECK;

    return (
       ( board[1] == choice and board[2] == choice and board[3] == choice )
    or ( board[4] == choice and board[5] == choice and board[6] == choice )
    or ( board[7] == choice and board[8] == choice and board[9] == choice )
    #VERTICAL CHECK;
    or ( board[1] == choice and board[4] == choice and board[7] == choice )
    or ( board[2] == choice and board[5] == choice and board[8] == choice )
    or ( board[3] == choice and board[6] == choice and board[9] == choice )
    #DIAGONAL CHECK;
    or ( board[1] == choice and board[5] == choice and board[9] == choice )
    or ( board[3] == choice and board[5] == choice and board[7] == choice )  )


def replay():
    """check if the users want to play the game again?"""
    return input('\nDo you want to play again? Enter [Y]es or [N]o: ').lower().startswith('y')


def choose_starting_player(p1, p2):
    """randomly choose starting player"""
    if random.choice((0, 1)):
        starting_player = p2
    else:
        starting_player = p1
    return starting_player

def win_screen(name: str = None):
    """output the win screen"""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if name is not None:
        print(f'\n\nCONGRATULATIONS {name}! YOU HAVE WON THE GAME!\n\n')
    else:
        print('\n\nTHE Computer HAS WON THE GAME!\n\n')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def tie_screen():
    """display DRAW screen"""
    print("~~~~~~~~~~~~~~~~~~")
    print('\nThe game is a DRAW!\n')
    print("~~~~~~~~~~~~~~~~~~")

def get_mode():
    """1 or 2 player game"""
    print("\n0. 1-player game with the computer.")
    print("1. 2-player game.")
    mode = int(input("\nSelect an option [0] or [1]: "))
    return mode

if __name__ == "__main__":
    #MAIN PROGRAM STARTS;

    print("\n\t\t NAMASTE! \n")
    input("Press ENTER to start!")

    default()
    display_rules()


    while True:
        ####################################################################################

        #Creating the board as a list; to be kept replacing it with user input;
        the_board = [' ']*10

        #Creating the available options on the board:
        available = [str(num) for num in range(0,10)] # a List Comprehension
        #available = '0123456789'



        mode = get_mode()
        if mode:
            p1_name, p2_name = get_names()
        else:
            p1_name, p2_name = get_names("Computer")

        # Asking Choices; Printing choices; X or O;
        p1_choice, p2_choice = get_mark_choice()
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)

        #Printing randomly who will go first;
        turn = choose_starting_player(p1_name, p2_name)

        print(f"\n{turn} will go first!")

        #Asking the user, if ready to play the game; Output will be True or False;
        play_game = play()

        display_board(the_board, available)
        while play_game:

            #PLAYER1
            if turn == p1_name:


                #Position of the input;
                position = player_choice(the_board, p1_name, p1_choice)

                #Replacing the ' ' at *position* to *p1_choice* in *theBoard* list
                place_marker(the_board, available, p1_choice, position)
                display_board(the_board, available)

                #To check if Player 1 has won after the current input;
                if win_check(the_board, p1_choice):
                    win_screen(p1_name)
                    play_game = False

                else:
                    #To check if the board is full; if yes, the game is a draw;
                    if full_board_check(the_board):
                        tie_screen()
                        break
                    #If none of the above is possible, next turn of Player 2
                    turn = p2_name


            #PLAYER2
            elif turn == p2_name:


                #Position of the input;
                if mode:
                    position = player_choice(the_board, p2_name, p2_choice)
                else:
                    position = ai_choice(the_board)
                    print(f'\n{p2_name} ({p2_choice}) has placed on {position}\n')

                #Replacing the ' ' at *position* to *p2_choice* in *theBoard* list
                place_marker(the_board, available, p2_choice, position)
                display_board(the_board, available)

                #To check if Player 2 has won after the current input;
                if win_check(the_board, p2_choice):
                    if mode:
                        win_screen(p2_name)
                    else:
                        win_screen()
                    play_game = False

                else:
                    #To check if the board is full; if yes, the game is a draw;
                    if full_board_check(the_board):
                        tie_screen()
                        break
                    #If none of the above is possible, next turn of Player 1
                    else:
                        turn = p1_name

        #If the users want to play the game again?
        if replay():
            #if Yes;
            continue
        else:
            #if No;
            break

        ####################################################################################

    print("\n\n\t\t\tTHE END!")
