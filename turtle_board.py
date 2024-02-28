import turtle

class Turtleboard:
    def __init__(self):
        self.width = 800
        self.half_width = self.width // 2
        self.height = 400
        self.half_height = self.height // 2
        self.size = 26
        self.speed = 0
        self.font = 'Veranda'
        self.font_size = 15
        self.t = turtle.getturtle()
        self.x = 13
        self.y = 13
        
        turtle.setup(self.width, self.height)
        window = turtle.Screen()
        window.title('Battleship')

        self.t.hideturtle()
        self.t.speed(self.speed)

    def draw(self):
        # draw player's board (top left board)
        self.t.penup()
        self.t.setposition(-self.half_width + 130, self.half_height - 60)
        self.t.write("Player's Board", font=(self.font, 15))
        self.t.setposition(-self.half_width + 100, self.half_height - 90)
        self.t.write(' A  B  C  D  E  F  G  H', font=(self.font, self.font_size))

        # draw player's rows
        for i in range(0, 9):
            self.t.setposition(-self.half_width + 100, self.half_height - 100 - (i * self.size))
            for j in range(0, 8):
                self.t.pendown()
                self.t.forward(self.size)
                self.t.penup()
        self.t.right(90)

        # draw player's columns
        for i in range(0, 9):
            self.t.setposition(-self.half_width + 100 + (i * self.size), self.half_height - 100)
            for j in range(0, 8):
                self.t.pendown()
                self.t.forward(self.size)
                self.t.penup()
        self.t.left(90)

        # write numbers to the left of the player's board
        for i in range(0, 8):
            self.t.setposition(-self.half_width + 80, self.half_height - (100 + self.size)  - (i * self.size))
            self.t.write(str(i + 1), font=(self.font, self.font_size))
        self.t.penup()

        # draw the computer's board (top right board)
        self.t.setposition(130, self.half_height - 60)
        self.t.write("Computer's Board", font=(self.font, self.font_size))
        self.t.setposition(100, self.half_height - 90)
        self.t.write(' A  B  C  D  E  F  G  H', font=(self.font, self.font_size))

        # draw computer's rows
        for i in range(0, 9):
            self.t.setposition(100, self.half_height - 100 - i * self.size)
            for j in range(0, 8):
                self.t.pendown()
                self.t.forward(self.size)
                self.t.penup()

        self.t.right(90)
        # draw computer's columns
        for i in range(0, 9):
            self.t.setposition(100 + i * self.size, self.half_height - 100)
            for j in range(0, 8):
                self.t.pendown()
                self.t.forward(self.size)
                self.t.penup()

        # write numbers to the left of the computer's board
        for i in range(0, 8):
            self.t.setposition(80, self.half_height - (100 + self.size)  - (i * self.size))
            self.t.write(str(i + 1), font=(self.font, self.font_size))
        self.t.penup()

    def player(self, ship_list):
        for ship in ship_list:
            for item in ship.coordinates:
                row = item[0]
                column = item[1]
                status = item[2]

                self.t.shape('square')
                if status == False:
                    self.t.fillcolor('yellow')
                elif status == True:
                    self.t.fillcolor('red')
                self.t.setposition(-self.half_width + 100 + (column * self.size) + self.x, self.half_height - 100 - (row * self.size) - self.y)
                self.t.pendown()
                self.t.stamp()
                self.t.penup()

    def player_miss(self, row, column):
        self.t.shape('square')
        self.t.fillcolor('lightgrey')
        self.t.setposition(100 + (column * self.size) + self.x, self.half_height - (100 + self.size) - (row * self.size) + self.y)
        self.t.pendown()
        self.t.stamp()
        self.t.penup()

    def player_hit(self, row, column):
        self.t.shape('square')
        self.t.fillcolor('red')
        self.t.setposition(100 + (column * self.size) + self.x, self.half_height - (100 + self.size) - (row * self.size) + self.y)
        self.t.pendown()
        self.t.stamp()
        self.t.penup()

    def computer_miss(self, row, column):
        self.t.shape('square')
        self.t.fillcolor('lightgrey')
        self.t.setposition(-self.half_width + 100 + (column * self.size) + self.x, self.half_height - 100 - (row * self.size) - self.y)
        self.t.pendown()
        self.t.stamp()
        self.t.penup()

    def computer_hit(self, row, column):
        self.t.shape('square')
        self.t.fillcolor('red')
        self.t.setposition(-self.half_width + 100 + (column * self.size) + self.x, self.half_height - 100 - (row * self.size) - self.y)
        self.t.pendown()
        self.t.stamp()
        self.t.penup()
