def placement(m, p, num):
    # if num is 1, the function puts 'X' in the matrix (m) (in place p)
    # if num is 2, the funciton puts 'O' in the matrix (m) (in place p)
    if num == 1:
        symbol = "X"
    elif num == 2:
        symbol = "O"
     
    if 1 <= p and p <= 3:
        r = 0 
        c = p-1
    elif 4 <= p and p <= 6:
        r = 1
        c = p-4
    elif 7 <= p and p <= 9:
        r = 2
        c = p-7
    
    if p < 1 or 9 < p:
        x = int(raw_input("You have to choose a place between 1 and 9!"))
        placement(m, x, num)
    else:
        if m[r][c] == "X" or m[r][c] == "O":
            print "That place is already taken!"
            imput(matrix, num)
        else:
            m[r][c] = symbol

def imput(matrix, num):
    if num == 1:
        x = int(raw_input("Where do you want to put the X? (place 1-9)"))
        placement(matrix, x, num)
    elif num == 2:
        o = int(raw_input("Where do you want to put the O? (place 1-9)"))
        placement(matrix, o, num)
    for item in matrix:
        print item

def checkRows(m):
    xcount = 0
    ocount = 0

    if ["X"]*3 in m:
        print "X wins!"
        return True
    elif ["O"]*3 in m:
        print "O wins!"
        return True

    return False

def checkColumns(m):
    for i in range(3):
        xcount = 0
        ocount = 0
        for row in m:
            if row[i] == "X":
                xcount += 1
            if row[i] == "O":
                ocount += 1
        if xcount == 3:
            print "X wins"
            return True
        elif ocount == 3:
            print "O wins!"
            return True
    return False


def checkDiagonals(m):
    xcount = 0
    ocount = 0
    # prime diagonal check
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                if matrix[i][j] == "X":
                    xcount += 1
                elif matrix[i][j] == "O":
                    ocount += 1
    if xcount == 3:
        print "X wins"
        return True
    elif ocount == 3:
        print "O wins!"
        return True
    
    xcount = 0
    ocount = 0 
    # secondary diagonal check
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (len(matrix[0]) - j) == i:
                if matrix[i][j] == "X":
                    xcount += 1
                elif matrix[i][j] == "O":
                    ocount += 1
    
    if xcount == 3:
        print "X wins"
        return True
    elif ocount == 3:
        print "O wins!"
        return True
    return False



matrix = [["" for x in range(3)] for x in range(3)]
for item in matrix:
    print item
i = 1
for item in matrix:
    print i, i+1, i+2
    i += 3
i = ""
while i != "X" and i != "O" and i != "x" and i != "o":
    i = str(raw_input("Who starts: X or O?"))
if i == "X" or i == "x":
    i = 1
elif i == "O" or i == "o":
    i = 2
for indx in range(9):
    imput(matrix, i)
    if i == 1:
        i = 2
    elif i == 2:
        i = 1
    if checkRows(matrix) or checkColumns(matrix) or checkDiagonals(matrix):
        break

raw_input()