import random

X = 'X'
O = 'O'
EMPTY = ' '

board = [EMPTY] * 9

winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('---------')

def is_board_full(board):
    return all(cell != EMPTY for cell in board)

def check_winner(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def evaluate(board):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = X
                eval = minimax(board, depth + 1, False)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = O
                eval = minimax(board, depth + 1, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -float('inf')
    best_move = -1

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = X
            eval = minimax(board, 0, False)
            board[i] = EMPTY

            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move


while True:
    print_board(board)
    
    if is_board_full(board) or check_winner(board, X) or check_winner(board, O):
        break
    
    player_move = int(input("\nEnter your move (0-8): "))
    
    if board[player_move] == EMPTY:
        board[player_move] = O
    else:
        print("Invalid move. Try again.")
        continue
    
    if is_board_full(board) or check_winner(board, X) or check_winner(board, O):
        break
    
    computer_move = find_best_move(board)
    board[computer_move] = X

print_board(board)

if check_winner(board, X):
    print("Computer wins!")
elif check_winner(board, O):
    print("You win!")
else:
    print("It's a draw!")
