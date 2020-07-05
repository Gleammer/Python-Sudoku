from tkinter import *
root = Tk()

large_font = ('Verdana',30)
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

def show():
    for i in maze:
        for j in i:
            print(j, end=" ")
        print()

def get_maze():
    for i in range(0, 9):
        for j in range(0, 9):
            command = "maze[" + str(i) + "][" + str(j) + "] = in" + str(i) + str(j) + ".get()"
            exec(command)

for i in range(0,9):
    for j in range(0,9):
        command = "in" + str(i) + str(j) + " = Entry(root, width=3, font=large_font)"
        exec(command)
        command = "in" + str(i) + str(j) + ".grid(row=" + str(i) + ",column=" + str(j) + ")"
        exec(command)

def get_values():
    get_maze()
    show()


myButton = Button(root, text="Get the maze", command=get_values)
myButton.grid(row=9)

root.mainloop()