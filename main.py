from tkinter import *
board = [[0 for i in range(7)] for i in range(6)]

root = Tk()

def add_token(position):

    pass
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                Label(root,text=str(i),padx=10, bg="white").grid(row=i,column=j)
            if (board[i][j] == 1):
                Label(root, text=str(i), padx=10, bg="yellow").grid(row=i, column=j)
            if (board[i][j] == 2):
                Label(root, text=str(i), padx=10, bg="red").grid(row=i, column=j)

    Button(text="Add Piece",command=lambda:add_token(0)).grid(row = 6, column = 0)
    Button(text="Add Piece",command=lambda:add_token(1)).grid(row=6, column=1)
    Button(text="Add Piece",command=lambda:add_token(2)).grid(row=6, column=2)
    Button(text="Add Piece",command=lambda:add_token(3)).grid(row=6, column=3)
    Button(text="Add Piece",command=lambda:add_token(4)).grid(row=6, column=4)
    Button(text="Add Piece",command=lambda:add_token(5)).grid(row=6, column=5)
    Button(text="Add Piece",command=lambda:add_token(6)).grid(row=6, column=6)


print_board(board)


root.mainloop()

