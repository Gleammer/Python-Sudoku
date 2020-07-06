from tkinter import *
from sudoku import *
root = Tk()

large_font = ('Verdana', 30)

def get_maze():
    for i in range(0, 9):
        for j in range(0, 9):
            command = "maze[" + str(i) + "][" + str(j) +  "] = in" + str(i) + str(j) + ".get()"
            exec(command)
            if maze[i][j]=='':
                maze[i][j]=0
            maze[i][j]=int(maze[i][j])

for i in range(0,9):
    for j in range(0,9):
        command = "in" + str(i) + str(j) + " = Entry(root, width=3, font=large_font)"
        exec(command)
        command = "in" + str(i) + str(j) + ".grid(row=" + str(i) + ",column=" + str(j) + ")"
        exec(command)

def get_values():
    get_maze()
    solve()
    show()

myButton = Button(root, text="Solve", command=get_values)
myButton.grid(row=9)

root.mainloop()