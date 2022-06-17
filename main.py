from tkinter import *

board = [[0 for i in range(7)] for i in range(6)]
turn = True
player = {1:"Red", 0:"Yellow"}

root = Tk()

winning_label = Label(root, text=f'The winner is {"Red" if turn else "Yellow"}')


def connect_token(board, position):
    count = 0
    temp_position = position
    while board[temp_position[0] + 1][temp_position[1]] == board[temp_position[0]][temp_position[1]]:
        temp_position[0] += 1
        count += 1
        if count == 4:
            return True
    temp_position = position
    count -= 1
    while board[temp_position[0] - 1][temp_position[1]] == board[temp_position[0]][temp_position[1]]:
        temp_position[0] -= 1
        count += 1
        if count == 4:
            return True
    count = 0
    temp_position = position

    while temp_position[1]+1 <= 6 and board[temp_position[0]][temp_position[1]+1] == board[temp_position[0]][temp_position[1]]:
        temp_position[1] += 1
        count += 1
        if count == 4:
            return True
    temp_position = position
    count -= 1

    while board[temp_position[0]][temp_position[1]-1] == board[temp_position[0]][temp_position[1]]:
        temp_position[1] -= 1
        count += 1
        if count == 4:
            return True

    count = 0
    temp_position = position
    while temp_position[1]+1 <= 6 and  board[temp_position[0]+1][temp_position[1] + 1] == board[temp_position[0]][temp_position[1]]:
        temp_position[1] += 1
        temp_position[0] +=1
        count += 1
        if count == 4:
            return True
    temp_position = position
    count -= 1

    while board[temp_position[0]-1][temp_position[1] - 1] == board[temp_position[0]][temp_position[1]]:
        temp_position[1] -= 1
        temp_position[0] -=1
        count += 1
        if count == 4:
            return True


    count = 0
    temp_position = position

    while board[temp_position[0] + 1][temp_position[1] - 1] == board[temp_position[0]][temp_position[1]]:
        temp_position[1] -= 1
        temp_position[0] += 1
        count += 1
        if count == 4:
            return True
    temp_position = position
    count -= 1

    while temp_position[1]+1 <= 6 and board[temp_position[0] -1][temp_position[1] + 1] == board[temp_position[0]][temp_position[1]]:
        temp_position[1] += 1
        temp_position[0] -= 1
        count += 1
        if count == 4:
            return True
    return False

def add_token(position):
    global turn
    for i in range(1, len(board) + 1):
        if board[-i][position] == 0:
            board[-i][position] = turn + 1
            check_pos = [-i, position]
            break

    print_board(board)
    if connect_token(board, check_pos):
        winning_label = Label(root, text=f'The winner is {"Red" if turn else "Yellow"}')
        winning_label.grid(row=7, column =2)
    turn = not turn


def print_board(given_board):
    global board
    board = given_board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                Label(root, padx=10, bg="white").grid(row=i, column=j)
            if board[i][j] == 1:
                Label(root, padx=10, bg="yellow").grid(row=i, column=j)
            if board[i][j] == 2:
                Label(root, padx=10, bg="red").grid(row=i, column=j)
    winning_label.grid_remove()
    Button(text="Add Piece", command=lambda: add_token(0)).grid(row=6, column=0)
    Button(text="Add Piece", command=lambda: add_token(1)).grid(row=6, column=1)
    Button(text="Add Piece", command=lambda: add_token(2)).grid(row=6, column=2)
    Button(text="Add Piece", command=lambda: add_token(3)).grid(row=6, column=3)
    Button(text="Add Piece", command=lambda: add_token(4)).grid(row=6, column=4)
    Button(text="Add Piece", command=lambda: add_token(5)).grid(row=6, column=5)
    Button(text="Add Piece", command=lambda: add_token(6)).grid(row=6, column=6)
    Button(text="Reset Board", command=lambda: print_board([[0 for i in range(7)] for i in range(6)])).grid(row=7, column=4)



print_board(board)

root.mainloop()
