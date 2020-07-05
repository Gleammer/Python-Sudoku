maze = [
    [0,3,8,0,6,0,4,1,0],
    [0,0,0,4,7,0,0,2,0],
    [2,0,9,0,0,0,0,6,0],
    [0,0,5,8,0,2,3,9,0],
    [0,0,0,0,0,4,1,0,7],
    [9,1,0,3,5,0,2,0,0],
    [8,9,4,0,0,5,6,7,0],
    [5,0,7,0,4,6,8,0,0],
    [0,0,3,0,0,0,5,0,9]
]

def check_square(val,x,y):
    x=x//3
    y=y//3
    for i in range(0,3):
        for j in range(0,3):
            if maze[3*x+i][3*y+j]==val:
                return False
    return True

def check_line(val,x,y):
    for i in range(0,9):
        if (maze[i][y] == val) or (maze[x][i] == val):
            return False
    return True

def check(val,x,y):
    if check_line(val,x,y) and check_square(val,x,y): #True daca se poate scrie, False daca nu se poate
        return True
    return False

def next():
    for i in range(0,9):
        for j in range(0,9):
            if maze[i][j]==0:
                for k in range(1,10):
                    if check(k,i,j):
                        maze[i][j]=k
                        if next() == False:
                            maze[i][j]=0
                            continue
                if maze[i][j]==0:
                    return False

def solve():
    next()

def show():
    for i in maze:
        for j in i:
            print(j, end=" ")
        print()

solve()
show()