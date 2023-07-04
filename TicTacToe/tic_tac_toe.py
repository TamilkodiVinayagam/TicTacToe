def print_board(board):
    print("-------")
    for row in range(3):
        print("|",end='')
        for col in range(3):
            print(board[row][col],end='|')
        print("\n-------")

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                return False
    return True

def check_win(board,player):
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]==player:
            return True
        
    for col in range(3):
            if board[0][col]== board[1][col]== board[2][col]==player:
                return True
    if board[0][0]==board[1][1]==board[2][2]==player:
        return True
    if board[0][2]==board[1][1]==board[2][0]==player:
        return True
    return False


def play_game():
    board=[[" " for _ in range(3)]for _ in range(3)]
    current_player="X"
    
    while True:
        print_board(board)
        if current_player=="X":
            print(current_player,"'s Turn")
        else:
            print(current_player,"'s Turn")
        row=int(input("Enter row (0-2):"))
        col=int(input("Enter col (0-2):"))
        
        

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Row and column should be between 0 and 2.")
            continue

    
        if board[row][col]!=" ":
            print("It's Occupied")
            continue
        board[row][col]=current_player
        
        if check_win(board,current_player):
            print_board(board)
            print("Player",current_player,"Wins")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a Tie")
            break
        current_player="O" if current_player=="X" else "X"
play_game()