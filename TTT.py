import random

 
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)
        

def check_win(board,player):
    for row in board:
        if all(cell==player for cell in row):
            return True
    for col in range(3):
        if(all(board[row][col]==player for row in range(3))):
            return True
    if all(board[i][i]==player for i in range(3)):
        return True
    if all(board[i][2-i]==player for i in range(3)):
        return True
    return False


def player_move(board,player):
    while(True):
        print("Enter your move")
        r=int(input("Enter row of cell(1-3) "))
        c=int(input("Enter Column of cell(1-3) "))
        if((r<=3 and r>=1) and (c<=3 and r>=1) ): 
            board[r-1][c-1]=player
            break
        else:
            print("Enter right move")
            pass
    return board

def ai_move(board,player):
    if(player=="X"):
        for row in range(3):
            for col in range(3):
                if board[row][col]==" ":
                    board[row][col]="O"
                    if check_win(board,"O"):
                        return
                    board[row][col]=" "
        for row in range(3):
            for col in range(3):
                if board[row][col]==" ":
                    board[row][col]="X"
                    if check_win(board,"X"):
                        board[row][col]="O"
                        return
                    board[row][col]=" "
        while(True):
            row=random.randint(0,2)
            col=random.randint(0,2)
            if(board[row][col]==" "):
                board[row][col]="O"
                return
    


def playgame():
    board=[[" " for _ in range(3)]for _ in range(3)]
    current_player="X"
    Ai_player="O"
    display_board(board)

    while(True):
        board=player_move(board,current_player)
        display_board(board)
        if(check_win(board,current_player)==True):
            print(current_player," wins")
            break
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "X"
        else:
            make_ai_move(board)

        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"      

    



playgame()


