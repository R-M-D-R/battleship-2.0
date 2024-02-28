global developer_mode
#developer_mode = True
developer_mode = False

import random

class Ship:
    def __init__(self, grid_size, orientation, length, list_of_ships):
        self.status = "alive"
        overlap = True
        while overlap:
            self.coordinates = []
            if orientation == "horizontal":
                row = random.randint(0, grid_size - 1)
                starting_column = random.randint(0, grid_size - length)
                for column in range(starting_column, starting_column + length):
                    self.coordinates.append([row, column, False])
            elif orientation == "vertical":
                column = random.randint(0, grid_size - 1)
                starting_row = random.randint(0, grid_size - length)
                for row in range(starting_row, starting_row + length):
                    self.coordinates.append([row, column, False])
            else:
                None
            intersect = False
            for element in self.coordinates:
                for i in range(0, len(list_of_ships)):
                    if element in list_of_ships[i].coordinates:
                        intersect = True
            if intersect == False:
                if developer_mode == True: print(self.coordinates)
                overlap = False

    def print(self):
        for item in self.coordinates:
            print(*item)

    def check_alive(self):
        if self.status == "alive":
            return True
        elif self.status == "dead":
            return False

    def print_coordinates(self):
        for coordinates in self.coordinates:
            statement = (str(coordinates) + " <–> [" +
                         str(coordinates[0] + 1) +
                         ", " + str(chr(coordinates[1] + 65)) +
                         ", " + str(coordinates[2]) + "]")
            print(statement)

    def print_status(self):
        print("Ship status: " + self.status)
