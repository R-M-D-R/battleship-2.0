########################
#                      #
#      BATTLESHIP      #
# with turtle graphics #
#         by           #
#                      #
#      Robin Ryder     #
#   rmd6050@uncw.edu   #
#                      #
########################

global developer_mode
#developer_mode = True
developer_mode = False

######################################################################################################
# import packages/modules #
######################################################################################################

import random
import turtle

from ship import *
from board import *
from turtle_board import *

######################################################################################################
# variables #
######################################################################################################

orienation_options = ["horizontal", "vertical"]

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

######################################################################################################
# functions #
######################################################################################################

# Check to make sure no two ships' coordinates
# overlap. This is necessary when creating ships.
def check_coordinates_overlap(new_coordinates, ship_list):
    overlap = False
    for ship in ship_list:
        for coordinate in new_coordinates:
            if coordinate in ship.coordinates:
                overlap = True
    return overlap

# this returns the number of ships still alive
# (so if it returns zero, there are zero ships
# remaining, and someone has won the game)
def number_ships_alive(ship_list):
    alive_ships = 0
    for ship in ship_list:
        if ship.status == "alive":
            alive_ships += 1
    return alive_ships

# creates a list that is all the ship
# this also creates the ships
def create_ship_list():
    ship_list = []

    orientation = random.choice(orienation_options)
    ship_list.append(Ship(grid_size, orientation, 5, ship_list))

    orientation = random.choice(orienation_options)
    ship_list.append(Ship(grid_size, orientation, 4, ship_list))

    orientation = random.choice(orienation_options)
    ship_list.append(Ship(grid_size, orientation, 3, ship_list))

    return ship_list

# choose the row that the player or computer will fire at
# this loop that won't break until an appropriate choice has been made
def choose_row(row_choice_max):
    while True:
        try:
            row = int(input("Choose a row (1 - " + str(row_choice_max) + "): "))
            if row < 1 or row > row_choice_max:
                print("Row choice must be between 1 and " + str(row_choice_max) + "\n")
                continue
            return row - 1  # the reason for the "minus one" is because the displayed row
                            # is one higher than the row number used by the system
                            # (due to indexing)
        except:
            print("Row choice must be between 1 and " + str(row_choice_max) + "\n")
            continue

# choose the column that the player or computer will fire at
# this loop that won't break until an appropriate choice has been made
def choose_column(column_choice_max):
    while True:
        try:
            column = str(input("Choose a column (A - " + str(column_choice_max) + "): ")).upper()
            if column not in column_choices:
                print("Column choice must be between A and " + str(column_choice_max) + "\n")
                continue
            return int(ord(column) - 65)    # this returns an integer that is the column
                                            # as it is indexed on the board ... so choosing
                                            # column C is translated into it's Unicode number 67
                                            # and then turned into the integer 2 so that the program
                                            # will look to the third column in the board (2 corresponds
                                            # to the third column due to indexing)
        except:
                print("Column choice must be between A and " + str(column_choice_max) + "\n")

# This determines whether or not a ship has been sunk.
# It returns a Boolean true or false.
def check_ship_sunk(ship):
    hits = 0
    #if developer_mode == True:
    #    ship.print_coordinates()
    #    ship.print_status()
    for coordinates in ship.coordinates:
        if coordinates[2] == True:
            hits += 1
            if developer_mode == True:
                print("Hits = " + str(hits))
    if hits == len(ship.coordinates):
        return True
    else:
        return False

# if a ship has been hit, this will update the coordinate's
# status to hit within the ship list
def update_ship_list(row, column, ship_list):
    for ship in ship_list:
        for coordinates in ship.coordinates:
            if coordinates == [row, column, False]:
                coordinates[2] = True
                return ship

def print_ships_remaining(ship_list, opponent):
    n = number_ships_alive(ship_list)
    if n != 1:
        print("\n" + opponent + " has " + str(n) + " ships remaining.")
    else:
        print("\n" + opponent + " has " + str(n) + " ship remaining.")

######################################################################################################
# program loop #
######################################################################################################

running = True
while running:
    # start the program
    print("\n\nWelcome to Battleship\n\n")
    grid_size = 8

    # create the boards
    player_board = Board(grid_size, "Player", True)                 # create the player's board
    computer_board = Board(grid_size, "Computer", developer_mode)   # create the computer's board

    # create the ships
    player_ships = create_ship_list()   # make the player's ships
    player_board.attach(player_ships)   # this places the ships onto the board

    computer_ships = create_ship_list()     # make the computer's ships
    computer_board.attach(computer_ships)   # this places the ships onto the board

    row_choice_max = grid_size
    column_choice_max = chr(grid_size + 64)
    column_choices = []
    for i in range(0, grid_size):
        column_choices.append(chr(i + 65))

#    print(player_ships)
#    print(player_ships[0])
#    print(player_ships[0].coordinates)
    
    # draw the turtle boards
    t = Turtleboard()
    t.draw()
    t.player(player_ships)

    
    
    # draw the player's board
    player_board.display(player_ships)
    print("\nPlayer has " + str(number_ships_alive(player_ships)) + " ships.")
    input("Press enter to continue.\n")
    
    #############
    # game loop #
    #############

    last_move_hit = False   # This is used to determine if the computer's previous move resulted
                            # in a hit. This is necessary to know because, if so, then the computer
                            # would try to hit adjacent spots in order to sink the ship (instead
                            # of shooting somewhere else).
    hit_list = []   # This is the list of coordinates hit (by the computer)
                    # when the computer is trying to sink a specific ship.
    #sunk_this_turn = False  # used to determine if the computer has sunk a ship on this particular turn

    player_win = False
    computer_win = False
    winner = False

    
    while not winner:

        #######################
        # player takes a turn #
        #######################

        # Where does the player want to attack?
        #players_turn = False
        players_turn = True
        while players_turn:
            # draw the computer's board
            computer_board.display(computer_ships)

            # where does the player want to attack?
            print("\nPlayer's turn.")
            row = choose_row(row_choice_max)
            column = choose_column(column_choice_max)

            # check if the coordinate has already been played
            if computer_board.board[row][column] == True:
                print("Coordinate has already been played. Choose again.\n")
                continue

            # check if the coordinate has already been played
            elif computer_board.board[row][column] == "miss":
                print("Coordinate has already been played. Choose again.\n")
                continue

            # player MISSES!
            elif computer_board.board[row][column] == None:
                computer_board.board[row][column] = "miss"
                computer_board.display(computer_ships)
                t.player_miss(row, column)
############# add a MISS to the computer's board
#####                # DRAW THE MISSED SPOT ON COMPUTER'S TURTLE BOARD
                print("\nMiss!")
                players_turn = False

            # player HITS!
            elif computer_board.board[row][column] == False:
                computer_board.board[row][column] = True    # update the board to show that there has been a hit
                # update the ship list to show that that coordinate on that specific ship has been hit
                computer_board.display(computer_ships)
                t.player_hit(row, column)
############# add a HIT to the computer's board
#####                # DRAW THE HIT SPOT ON COMPUTER'S TURTLE BOARD
                print("\nYou hit a ship!")
                for ship in computer_ships:
                    for coordinates in ship.coordinates:
                        if coordinates == [row, column, False]:
                            coordinates[2] = True
                            # check to see if this ship has been sunk
                            if check_ship_sunk(ship) == True:
                                ship.status = "dead"
                                print("Ship has been sunk!")
                                print_ships_remaining(computer_ships, "Computer")
                players_turn = False
            else:
                None

            # check for winner
            if number_ships_alive(computer_ships) == 0:
                player_win = True
                print("\nPlayer wins!")
                winner = True

            players_turn = False
        if winner == True:
            break

        #######################
        # computer takes turn #
        #######################

        input("\nComputer's turn. Press enter.\n")
        #computers_turn = False
        computers_turn = True
        while computers_turn:

            if len(hit_list) == 0:  # the computer has not hit anything in the last
                                    # move (or few) and is not currently trying to
                                    # sink a specific ship

                # computer chooses where to attack
                row = random.randint(0, grid_size - 1)      # pick a row
                column = random.randint(0, grid_size - 1)   # pick a column

                # computer chose a coordinate that has already been played (previous hit)
                if player_board.board[row][column] == True:
                    continue

                # computer chose a coordinate that has already been played (previous miss)
                elif player_board.board[row][column] == "miss":
                    continue

                # computer MISSES!
                elif player_board.board[row][column] == None:
                    player_board.board[row][column] = "miss"
                    t.computer_miss(row, column)
############# add a MISS to the player's board
                    computers_turn = False
                    player_board.display(player_ships)
                    played = str(row + 1) + str(chr(column + 65))
                    print("\nComputer played " + played)
                    print("\nComputer missed!")
                    break

                # computer HITS!
                elif player_board.board[row][column] == False:
                    player_board.board[row][column] = True      # update the board to show that there has been a hit
                    t.computer_hit(row, column)
############# add a HIT to the player's board
                    previous_move_hit = True
                    hit_list.append([row, column])
                    if developer_mode == True: print("Hit list:", *hit_list)
                    directions = [UP, DOWN, LEFT, RIGHT]
                    direction_has_been_chosen = False

                    player_board.display(player_ships)
                    played = str(row + 1) + str(chr(column + 65))
                    print("Computer played " + played)
                    print("\nComputer hit!")

                    # update the ship list to show that that coordinate on that specific ship has been hit
                    this_hit_ship = update_ship_list(row, column, player_ships)

                    # check to see if that particular ship has been sunk
                    if check_ship_sunk(this_hit_ship) == True:
                        this_hit_ship.status = "dead"
                        sunk_this_turn = True
                        print("Ship has been sunk!")
                        hit_list = []
                        print(ships_remaining(player_ships, "Player"))
                    break

                else:
                    None

                computers_turn = False  # this ends the computer's turn

            # if the computer has HIT a ship in one of the last few moves and is now in "attach mode"
            elif len(hit_list) > 0:        # the computer has only one hit on the ship
                attacking = True
                while attacking:
                    if developer_mode == True: print("Hit list: ", hit_list)
                    if direction_has_been_chosen == False:
                        if directions == []:
                            directions = [UP, DOWN, LEFT, RIGHT]
                        else:
                            direction = directions[-1]
                            directions.pop(-1)
                        if developer_mode == True: print("Directions:", *directions)
                        if developer_mode == True: print("Direction:", direction)

                        row = hit_list[0][0]
                        column = hit_list[0][1]

                        if direction == UP:
                            if row == 0: continue
                            else: row = row - 1
                        elif direction == DOWN:
                            if row == grid_size - 1: continue
                            else: row = row + 1
                        elif direction == LEFT:
                            if column == 0: continue
                            else: column = column - 1
                        elif direction == RIGHT:
                            if column == grid_size - 1: continue
                            column = column + 1
                        else:
                            None

                        direction_has_been_chosen = True
                        if developer_mode == True: print("Direction:", str(direction))

                    elif direction_has_been_chosen == True:

                        row = hit_list[-1][0]
                        column = hit_list[-1][1]

                        if direction == UP:
                            if row == 0:
                                direction_has_been_chosen = False
                                continue
                            else:
                                row = row - 1

                        elif direction == DOWN:
                            if row == grid_size - 1:
                                direction_has_been_chosen = False
                                continue
                            else:
                                row = row + 1

                        elif direction == LEFT:
                            if column == 0:
                                direction_has_been_chosen = False
                                continue
                            else:
                                column = column - 1

                        elif direction == RIGHT:
                            if column == grid_size - 1:
                                direction_has_been_chosen = False
                                continue
                            else:
                                column = column + 1

                        else:
                            None

                    # display the new attack coordinates
                    if developer_mode == True: print(str(row), str(column))

                    # computer chose a coordinate that has already been played (previous hit)
                    if player_board.board[row][column] == True:
                        direction_has_been_chosen = False
                        continue

                    # computer chose a coordinate that has already been played (previous miss)
                    elif player_board.board[row][column] == "miss":
                        direction_has_been_chosen = False
                        continue

                    # computer MISSES!
                    elif player_board.board[row][column] == None:
                        player_board.board[row][column] = "miss"
                        t.computer_miss(row, column)
############# add a MISS to the player's board
                        direction_has_been_chosen = False
                        computers_turn = False

                        player_board.display(player_ships)
                        played = str(row + 1) + str(chr(column + 65))
                        print("\nComputer played " + played)
                        print("\nComputer missed!")
                        attacking = False
                        break

                    # computer HITS!
                    elif player_board.board[row][column] == False:
############# add a HIT to the player's board
                        player_board.board[row][column] = True      # update the board to show that there has been a hit
                        hit_list.append([row, column])
                        t.computer_hit(row, column)

                        player_board.display(player_ships)
                        played = str(row + 1) + str(chr(column + 65))
                        print("Computer played " + played)
                        print("\nComputer hit!")
                        if developer_mode == True: print("\nHit List: " + str(hit_list))

                        # update the ship list to show that that coordinate on that specific ship has been hit
                        # update_ship_list(row, column, player_ships)

                        for ship in player_ships:
                            for coordinates in ship.coordinates:
                                if coordinates == [row, column, False]:
                                    coordinates[2] = True
                                    # check to see if this ship has been sunk
                                    if check_ship_sunk(ship) == True:
                                        ship.status = "dead"
                                        hit_list = []
                                        print("Ship has been sunk!")
                                        print_ships_remaining(player_ships, "Player")
                        break

                    else:
                        None

                #################################
                # this ends the computer's turn #
                #################################

            # check for winner
            if number_ships_alive(player_ships) == 0:
                computer_win = True
                print("\nComputer wins!")
                winner = True

            computers_turn = False

        if winner == True:
            break

    play_again = input("\nPlay again? (y/n) ")
    if play_again.upper() == "N":
        running = False
print("Good bye")
