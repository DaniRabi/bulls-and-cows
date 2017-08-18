class board():

    def __init__(self):
        self.board = [[0 for column in range(6)] for row in range(6)]
        self.ships = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
"""
    def temp_board(self):
        self.board = [[1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0 ,0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0 ,0, 1]]
"""
    def insert_ship(self, x, y, x2, y2): # inserts ships
        if not in_index(x, y) or not in_index(x2, y2):
            print "Out of index!"
            return
        if not self.check_ship_length(x, y, x2, y2):
            return
        if not self.valid_location(x, y, x2, y2):
            print "Invalid location! Retry: "
            self.insert_ship(int(raw_input("Enter start row index: ")), int(raw_input("Enter start column index: ")), int(raw_input("Enter end row index: ")), int(raw_input("Enter end column index: ")))
            return

        self.ships += 1
        self.board[x][y] = 1
        if x == x2:
            for c in range(y, y2+1):
                self.board[x][c] = 1
        elif y == y2:
            for r in range(x, x2+1):
                self.board[r][y] = 1
        else:
            print "Incorrect coordinates! (not on the same row nor column)"
        self.print_board()

    def check_ship_length(self, x, y, x2, y2):
        if x == x2:
            l = y2 - y
        elif y == y2:
            l = x2 - x
        else:
            print "Ship is not straight!"
            return False

        if l+1 == 4 and self.fours == 1:
            print "There can only be one length 4 ship!"
            return False
        elif l+1 == 3 and self.threes == 2:
            print "There can only be two length 3 ships!"
            return False
        elif l+1 == 2 and self.twos == 2:
            print "There can only be two length 2 ships!"
            return False
        else:
            if l+1 == 4:
                self.fours += 1
            elif l+1 == 3:
                self.threes += 1
            elif l+1 == 2:
                self.twos += 1
            return True

    def valid_location(self, x, y, x2, y2):
        if x == x2:  # if horizontal
            if x == 0:
                r = 0
            else:
                r = x - 1
            if x == 5:
                r2 = 6
            else:
                r2 = x + 2
            if y == 0:
                c = 0
            else:
                c = y - 1
            if y2 == 5:
                c2 = 6
            else:
                c2 = y2 + 2
        if y == y2:  # if vertical
            if y == 0:
                c = 0
            else:
                c = y - 1
            if y == 5:
                c2 = 6
            else:
                c2 = y + 2
            if x == 0:
                r = 0
            else:
                r = x - 1
            if x2 == 5:
                r2 = 6
            else:
                r2 = x2 + 2
        return self.valid_check(r, r2, c, c2)

    def valid_check(self, r, r2, c, c2):
        for i in range(r, r2):
            for j in range(c, c2):
                if self.board[i][j] == 1:
                    return False
        return True

    def mark_location(self, x, y, marked):
        if not in_index(x, y):
            print "Out of index!"
        elif self.board[x][y] == 1:
            self.board[x][y] = 0
            marked.board[x][y] = 1
            print "Hit!"
        elif marked.board[x][y] == 1 or marked.board[x][y] == 'X':
            print "Already guessed!"
        else:
            marked.board[x][y] = 'X'
            print "You missed!"
        marked.print_board()

    def is_empty(self):
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == 1:
                    return False
        print "You win!"
        return True

    def print_board(self):  # prints board
        for item in self.board:
            print item
        print '\n'
    def get_fours(self):
        return self.fours
    def get_threes(self):
        return self.threes
    def get_twos(self):
        return self.twos
    # class board() END


def in_index(x, y):
    if x < 0 or x > 5 or y < 0 or y > 5:
        return False
    else:
        return True
def create_board():  # inserts ships in a new board and returns it
    b = board()
    while b.get_fours() != 1 or b.get_threes() != 2 or b.get_twos() != 2:
        b.insert_ship(int(raw_input("Enter start row index: ")), int(raw_input("Enter start column index: ")), int(raw_input("Enter end row index: ")), int(raw_input("Enter end column index: ")))
    return b

"""
def create_temp_board():
     b = board()
     b.temp_board()
     return b

p1 = create_temp_board()
"""
p1 = create_board()
p1.print_board()
marked = board()

print "Guess a location: "
while not p1.is_empty():
    x = int(raw_input("Enter row: "))
    y = int(raw_input("Enter column: "))
    p1.mark_location(x, y, marked)
