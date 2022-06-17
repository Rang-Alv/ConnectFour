from tkinter import *
board = [[0 for i in range(7)] for i in range(6)]

print(board)


root = Tk()
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                Label(root,text=str(i),padx=10, bg="white").grid(row=i,column=j)
            if (board[i][j] == 1):
                Label(root, text=str(i), padx=10, bg="yellow").grid(row=i, column=j)
            if (board[i][j] == 2):
                Label(root, text=str(i), padx=10, bg="red").grid(row=i, column=j)

print_board(board)


root.mainloop()
