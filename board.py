import random

class Board:
    def __init__(self, grid_size, name, visibility):
        self.board = []
        self.grid_size = 8
        self.name = name
        self.visibility = visibility
        self.create()

    def create(self):
        for row in range(0, self.grid_size):
            self.board.append([])
            for column in range(0, self.grid_size):
                self.board[row].append(None)

    def display(self, ships):
        display_board = self.create_display_board(ships)
        for row in display_board:
            print(*row)

    def attach(self, list_of_ships):
        for ship in list_of_ships:
            for coordinates in ship.coordinates:
                if coordinates[2] == False:
                    self.board[coordinates[0]][coordinates[1]] = False
                elif coordinates[2] == True:
                    self.board[coordinates[0]][coordinates[1]] = True

    def display_raw(self):
        for row in self.board:
            print(row)

    def create_display_board(self, ships):
        display_board = []
        length = self.grid_size
        display_board.append(["\n"])
        name = self.name + "'s board."
        display_board.append([name.center(3 * self.grid_size)])
        header = ["     "]
        for k in range(0, length):
            header.append(chr(k + 65) + " ")
        display_board.append(header)
        for i in range(0, length):
            if i < 9:
                row = ["  " + str(i + 1) + " "]
            else:
                row = ["  " + str(i + 1)]
            for j in range(0, length):
                if self.board[i][j] == None:
                    #row.append(" _")
                    row.append(" ░")
                elif self.board[i][j] == False:
                    if self.visibility == True:
                        row.append(" O")
                    elif self.visibility == False:
                        #row.append(" _")
                        row.append(" ░")
                elif self.board[i][j] == True:
                    row.append(" ■")
                elif self.board[i][j] == "miss":
                    row.append(" X")
            display_board.append(row)
        return display_board
