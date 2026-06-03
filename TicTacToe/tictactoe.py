board=[" "," "," ",
       " "," "," ",
       " "," "," "]
def print_board():
    print()
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[6],"|",board[7],"|",board[8])
    print()
def check_win(board,player):
    win_patterns = [(0,1,2),(3,4,5),(6,7,8), 
                    (0,3,6),(1,4,7),(2,5,8), 
                    (0,4,8),(2,4,6)]  
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False
def available_moves(board):
    moves=[]
    for i in range(9):
        if board[i]==" ":
            moves.append(i)
    return moves    
def minimax(board,is_maximizing):
    if check_win(board,"O"):
        return 1
    if check_win(board,"X"):  
        return -1
    if len(available_moves(board))==0:
        return 0
    if is_maximizing:
        best_score=-1000
        for moves in available_moves(board):
            board[moves]="O"
            score=minimax(board,False)
            board[moves]=" "
            best_score=max(score,best_score)
        return best_score
    else:
        best_score=1000
        for moves in available_moves(board):
            board[moves]="X"
            score=minimax(board,True)
            board[moves]=" "
            best_score=min(score,best_score)
        return best_score     
def ai_move():
    best_score=-1000
    best_move=None
    for moves in available_moves(board):
        board[moves]="O"
        score=minimax(board,False)
        board[moves]=" "
        if score>best_score:
            best_score=score
            best_move=moves
    board[best_move]="O"
def is_draw(board):
    return len(available_moves(board))==0
while True:
    print_board()
    position=int(input("Enter your move (1-9): "))-1
    if board[position]!=" ":
        print("that position is already taken. Try again.")
        continue
    board[position]="X"
    if check_win(board,"X"):
        print_board()
        print("You win!")
        break
    if is_draw(board):
        print_board()
        print("It's a draw!")
        break
    ai_move()
    if check_win(board,"O"):
        print_board(

        )
        print("AI wins!")
        break
    if is_draw(board):
        print_board()
        print("It's a draw!")
        break