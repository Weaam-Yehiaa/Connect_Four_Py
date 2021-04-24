'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 | 0,6
  1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6
  2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 | 2,6
  3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5 | 3,6
  4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5 | 4,6
  5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6
'''
N, M = 6, 7
grid = []
grid = [['.' for i in range(M)] for j in range(N)]
dic={ (0,0):0,(0,1):0,(0,2):0,(0,3):0,(0,4):0,(0,5):0,(0,6):0,
      (1,0):0,(1,1):0,(1,2):0,(1,3):0,(1,4):0,(1,5):0,(1,6):0,
      (2,0):0,(2,1):0,(2,2):0,(2,3):0,(2,4):0,(2,5):0,(2,6):0,
      (3,0):0,(3,1):0,(3,2):0,(3,3):0,(3,4):0,(3,5):0,(3,6):0,
      (4,0):0,(4,1):0,(4,2):0,(4,3):0,(4,4):0,(4,5):0,(4,6):0,
      (5,0):0,(5,1):0,(5,2):0,(5,3):0,(5,4):0,(5,5):0,(5,6):0,
}

#This function prints the grid of Connect Four Game as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():
    s = ''
    for i in range(N - 3):
        h = 0
        x = i
        j = h
        while j < M and x < N:
            s += grid[x][j]
            j += 1
            x += 1
        if len(s)>=4:
            if s[:4] == 'XXXX' or s[:4]=='OOOO':return True
        if len(s)>=5:
            if s[1:5] == 'XXXX' or s[1:5]=='OOOO':return True
        if len(s)>=6:
            if s[2:6] == 'XXXX' or s[2:6]=='OOOO':return True
        s = ''

    s = ''
    for i in range(M - 3):
        h = 0
        x = i
        j = h
        while j < N and x < M:
            s += grid[j][x]
            j += 1
            x += 1
        if len(s)>=4:
            if s[:4] == 'XXXX' or s[:4]=='OOOO':return True
        if len(s)>=5:
            if s[1:5] == 'XXXX' or s[1:5]=='OOOO':return True
        if len(s)>=6:
            if s[2:6] == 'XXXX' or s[2:6]=='OOOO':return True
        s = ''
        h += 1
    s = ''
    for i in range(N):
        for j in range(M):
            s += grid[i][j]
        if s[:4] == 'XXXX' or s[:4]=='OOOO' or s[1:5] == 'XXXX' or s[1:5]=='OOOO'or s[2:6] == 'XXXX' or s[2:6]=='OOOO' or s[3:7] == 'XXXX' or s[3:7]=='OOOO':
            return True
        s = ''
    s = ''
    for i in range(M):
        for j in range(N):
            s += grid[j][i]
        if s[:4] == 'XXXX' or s[:4] == 'OOOO' or s[1:5] == 'XXXX' or s[1:5] == 'OOOO' or s[2:6] == 'XXXX' or s[2:6] == 'OOOO':
            return True
        s = ''
    s = ''
    for i in range(N - 3):
        h = 6
        x = i
        j = h
        while j >= 0 and x < N:
            s += grid[x][j]
            j -= 1
            x += 1
        if len(s)>=4:
            if s[:4] == 'XXXX' or s[:4]=='OOOO':return True
        if len(s)>=5:
            if s[1:5] == 'XXXX' or s[1:5]=='OOOO':return True
        if len(s)>=6:
            if s[2:6] == 'XXXX' or s[2:6]=='OOOO':return True
        s = ''
    s = ''
    z = 6
    for i in range(M - 3):
        h = 0
        j = h
        x = z
        while j < N and x >= 0:
            s += grid[j][x]
            j += 1
            x -= 1
        if len(s)>=4:
            if s[:4] == 'XXXX' or s[:4]=='OOOO':return True
        if len(s)>=5:
            if s[1:5] == 'XXXX' or s[1:5]=='OOOO':return True
        if len(s)>=6:
            if s[2:6] == 'XXXX' or s[2:6]=='OOOO':return True

        z -= 1
        s = ''
    return False




#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    f=0
    for i in range(N):
        for j in range(M):
            if dic[(i,j)]==0:
                f=1
                break
    if f==0 and not check_win():
        return True
    else: return False

    pass

#This function checks if given cell is empty or not
def check_empty(i):
    if dic[(0,i)]==0:return True
    else:return False

#This function checks if given position is valid or not
def check_valid_column(i):
    if i>=0 and i<=6: return True
    else: return False

#This function sets a value to a cell
def set_cell(i, mark):
    h=5
    while h>=0:
        if dic[(h,i)]==0:
            dic[(h,i)]=1
            grid[h][i]=mark
            break
        else: h-=1


#This function clears the grid
def grid_clear():
    global grid
    global dic
    grid.clear()
    dic.clear()
    grid = [['.' for i in range(M)] for j in range(N)]
    dic = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (0, 5): 0, (0, 6): 0,
           (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0,
           (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0,
           (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0,
           (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (4, 6): 0,
           (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 0, (5, 5): 0, (5, 6): 0,
           }


#MAIN FUNCTION
def play_game():
    print("Connect Four Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
        print('Player %s' % mark)
        i = int(input('Enter the column index: '))
        while not check_valid_column(i) or not check_empty(i):
            i = int(input('Enter a valid column index: '))
        #Set the input position with the mark
        set_cell(i, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        op_mark = 'O' if player == 0 else 'X'
        #Check if the state of the grid has a tie state
        if check_tie(mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break
        #Player number changes after each turn
        player = 1 - player


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		breakv