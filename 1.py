import random


def print_board(board):
    print("-" * 13)
    for i, row in enumerate(board):
        print("|", end=" ")
        print(" | ".join(row), end=" ")
        print("|")
        if i < 2:
            print("|" + "-" * 11 + "|")
    print("-" * 13)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row,col): ")
        try:
            row, col = map(int, move.split(','))

            if board[row-1][col-1] == ' ':
                board[row-1][col-1] = player
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid move in the format row,col.")

def computer_move(board, computer, player):
    print(f"Computer ({computer}) is making a move...")
    # Check for winning moves
    move = find_winning_move(board, computer)
    if move is not None:
        row, col = divmod(move, 3)
        board[row][col] = computer
        return
    
    # Check for blocking opponent
    move_blocked = defensive_move(board, player, computer)
    if move_blocked:
        return

    # fork move
    fork_move = find_fork_move(board, player, computer)
    if fork_move is not None:
        row, col = divmod(fork_move, 3)
        board[row][col] = computer
        return
    
    # Check for blocking opponent's fork
    block_fork = block_fork_move(board, player, computer)
    if block_fork is not None:
        row, col = divmod(block_fork, 3)
        board[row][col] = computer
        return
    
    # random move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = computer
        
def find_winning_move(board, symbol):
    # Check rows
    for i in range(3):
        if board[i].count(symbol) == 2 and ' ' in board[i]:
            return i * 3 + board[i].index(' ')

    # Check columns
    for i in range(3):
        column = [board[j][i] for j in range(3)]
        if column.count(symbol) == 2 and ' ' in column:
            return column.index(' ') * 3 + i

    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]

    if diagonal1.count(symbol) == 2 and ' ' in diagonal1:
        return diagonal1.index(' ') * 3 + diagonal1.index(' ')
    
    if diagonal2.count(symbol) == 2 and ' ' in diagonal2:
        return diagonal2.index(' ') * 3 + (2 - diagonal2.index(' '))

    return None


def defensive_move(board, player, computer):
    # Check rows
    for i in range(3):
        row = board[i]
        if row.count(player) == 2 and ' ' in row:
            col = row.index(' ')
            board[i][col] = computer
            return True

    # Check columns
    for i in range(3):
        column = [board[j][i] for j in range(3)]
        if column.count(player) == 2 and ' ' in column:
            row = column.index(' ')
            board[row][i] = computer
            return True

    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]

    if diagonal1.count(player) == 2 and ' ' in diagonal1:
        index = diagonal1.index(' ')
        board[index][index] = computer
        return True
    
    if diagonal2.count(player) == 2 and ' ' in diagonal2:
        index = diagonal2.index(' ')
        board[index][2 - index] = computer
        return True

    return False


def find_fork_move(board, player, computer):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # Simulate placing the computer's mark in an empty cell
                board[i][j] = computer

                # Check if this move creates a fork (two winning paths)
                if has_fork(board, computer):
                    board[i][j] = ' '  # Undo the move
                    return i * 3 + j  # Return the move

                board[i][j] = ' '  # Undo the move

    return None

def has_fork(board, mark):
    cnt=0
    # Check rows
    for i in range(3):
        row = board[i]
        if row.count(mark) == 2 and ' ' in row:
            cnt+=1

    # Check columns
    for i in range(3):
        column = [board[j][i] for j in range(3)]
        if column.count(mark) == 2 and ' ' in column:
            cnt+=1

    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]

    if diagonal1.count(mark) == 2 and ' ' in diagonal1:
        cnt+=1
    
    if diagonal2.count(mark) == 2 and ' ' in diagonal2:
        cnt+=1
    
    
    if cnt>=2:
        return True
    return False


def block_fork_move(board, player, computer):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # Simulate placing the player's mark in an empty cell
                board[i][j] = player

                # Check if this move creates a fork for the player
                if has_fork1(board, player):
                    board[i][j] = ' '  # Undo the move
                    return i * 3 + j  # Return the move

                board[i][j] = ' '  # Undo the move

    return None

def has_fork1(board, mark):
    # Check rows
    
    for i in range(3):
        row = board[i]
        if row.count(mark) == 2 and ' ' in row:
            return True

    # Check columns
    for i in range(3):
        column = [board[j][i] for j in range(3)]
        if column.count(mark) == 2 and ' ' in column:
            return True

    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]

    if diagonal1.count(mark) == 2 and ' ' in diagonal1:
        return True
    
    if diagonal2.count(mark) == 2 and ' ' in diagonal2:
        return True

    return False


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    mode = input("Choose a mode (1 for Player vs Player, 2 for Player vs Computer): ")

    if mode == '1':
        player1 = 'X'
        player2 = 'O'

        while True:
            print_board(board)
            player_move(board, player1)
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            print_board(board)
            player_move(board, player2)
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

    elif mode == '2':
        player = 'X'
        computer = 'O'

        while True:
            print_board(board)
            computer_move(board, computer,player)
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Computer ({winner}) wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            
            print_board(board)
            player_move(board, player)
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            

    else:
        print("Invalid mode. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
