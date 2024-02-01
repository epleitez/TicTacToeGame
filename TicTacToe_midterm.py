"""
Tic Tac Toe game
@Xi Kramer
"""

import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
    
    
def display_board(board):

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
def marker_choice():
    print("Player 1...")
    userResponse = input("which marker would you like to use for this game? ('x' or 'o')")
    if userResponse == "X" or userResponse == "x":
      player1_marker = "x"
      player2_marker = "o"
    elif userResponse == "O" or userResponse == "o":
      player1_marker = "o"
      player2_marker = "x"
    else:
      print("sorry could not recognize response")
      
    return (player1_marker,player2_marker) 

    
def place_marker(board, marker, position):  # current board list, which marker, place where

    board[position - 1] = marker
    position = board[position - 1]
    
    
def haswon(board, marker):

    #check Horizontal Rows
    if board[0] == board[1] == board[2] == marker:
      return True
    elif board[3] == board[4] == board[5] == marker:
      return True
    elif board[6] == board[7] == board[8] == marker:
      return True
    #check vertical Rows
    elif board[0] == board[3] == board[6] == marker:
      return True
    elif board[1] == board[4] == board[7] == marker:
      return True
    elif board[2] == board[5] == board[8] == marker:
      return True
    #check diagonal Rows
    elif board[0] == board[4] == board[8] == marker:
      return True
    elif board[2] == board[4] == board[6] == marker:
      return True
    else:
      return False
     

def choose_first():
    player1 = 1
    player2 = 2
    randomNum = random.randint(1,2)
    
    if randomNum == player1:
      return "player 1"
    elif randomNum == player2:
      return "player 2"
    

def board_isfull(board):
    
    i = "-"
    if i in board:
      return True
    else:
      return False
    

def player_choice(board):
  
    print("where would you like to go (next)?")
    
    
    if board_isfull(board) == False:
    
      position = get_digit()
      if board[position - 1] == " ":
         position = position
      else:
         print("player is already in that spot!")
         position = get_digit()
         
      return position
    
def get_digit():
   
   digit = int(input("Choose position(1-9):"))
   
   if digit >= 1 and digit <= 9:
      digit = digit
   else:
      print("position not in range...")
      digit = get_digit()
      
   return digit
   


def replay():

    choice = input("\nWould you like to play again? (Yes or No): ")
    if choice == "Yes" or choice == "yes":
      return True
    elif choice == "No" or choice == "no":
      return False
    else:
      print("response not recognized...")
      return False

def yes_no():
   
    choice = input("Yes or No: ")
    if choice == "Yes" or choice == "yes":
      return True
    elif choice == "No" or choice == "no":
      return False
    else:
      print("response not recognized...")
      return False

def winning_message(winner):
    
    print("\n")
    print(winner, "HAS WON!!!")

def display_keypad():

    print("_________")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

def instructions():

    print("This is a two-player game. Each player takes turns and")
    print("choose a corresponding position of where you'd place")
    print("your marker according to the following keypad layout:")
    display_keypad()

def play_TicTacToe():

    # print game instructions
    print("    *** Welcome to our Tic Tac Toe game! ***    ")
    instructions()

    while True:  #each iteration is one full game/exit if wish not play again
        print("A few questions before we start!")
        the_board = [' '] * 10

        # set player markers
        player1_marker, player2_marker = marker_choice()  # tuple unpacking
        print("Okay, Player 1's marker is '" + player1_marker + "', player 2's marker is '" + player2_marker + "', and", end=" ")

        # who goes first - randomly decide
        # simulate flip coin which player goes first by calling choose_first() which will return "player 1" or "player 2"
        turn = choose_first()
        print(turn + " will go first!")

        # why need to ask "Ready to play?"
        # we will use a boolean gameon to signify if a game is on
        # when there is a win or tie, gameon will be set to false, wait to see if starts another game
        # as user if ready, confirm, set gameon to true until a win or tie set gamon to false
        print("Ready to play?", end=" ")
        gameon = yes_no()  # boolean control one game, ini here

        # game play
        while gameon:  # unless win or tie
            # -----------------player 1's turn--------------------
            if turn == "player 1":  # could switch on 0, or 1, here to be clear
                # 1, display the board by calling display_board(board)
                display_board(the_board)

                # 2, player choose a position by calling player_choice(board)
                print("Player 1 ('" + player1_marker, end="') ")  # reminder the player's current marker choice, nicer message folowing by " choose a position
                position = player_choice(the_board)

                # 3, place the marker on the position by calling place_marker(board, marker, position)
                place_marker(the_board, player1_marker, position)

                # 4, check if they won, or check if it's a tie, else player 2's turn
                # to check if the player has won, by calling haswon(board, mark)
                # to check if it's a tie, by checking if the board if full, by calling board_isfull(board):
                # no tie and no win? next player's turn
                if haswon(the_board, player1_marker):
                    winning_message("PLAYER 1")
                    display_board(the_board)
                    gameon = False
                elif board_isfull(the_board):
                    print("TIE GAME")
                    display_board(the_board)
                    gameon = False
                else:
                    turn = "player 2"
            # --------------------player 2's turn-------------------
            else:  # player 2's turn
                # 1, display the board by calling display_board(board)
                display_board(the_board)

                # 2, player choose a position by calling player_choice(board)
                print("Player 2 ('" + player2_marker, end="') ")
                # print("Player 2", end = " ")
                position = player_choice(the_board)

                # 3, place the marker on the position by calling place_marker(board, marker, position)
                place_marker(the_board, player2_marker, position)  ####change here!

                # 4, check if they won, or check if it's a tie, else player 2's turn
                # to check if the player has won, by calling haswon(board, mark)
                # to check if it's a tie, by checking if the board if full, by calling board_isfull(board):
                # no tie and no win? next player's turn
                if haswon(the_board, player2_marker):  ####change here!
                    winning_message("PLAYER 2")
                    display_board(the_board)
                    gameon = False
                elif board_isfull(the_board):
                    print("Tie game")
                    display_board(the_board)
                    gameon = False
                else:
                    turn = "player 1"  ####change here!
        # --------------------------------
        # single exit the game
        # break out of the while loop on replay()
        
        if not replay():
            print("Thank you. :) Goodbye!")
            break #end the program

    # end while loop

# ----------------------------------
def main():
    play_TicTacToe()

if __name__ == "__main__":
    main()