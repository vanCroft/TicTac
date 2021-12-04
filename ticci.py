import random
 
def make_board(board):
    print("\n    1   2   3 \n")
    print("1   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("2   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("3   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")
    
def check_row(board, row):
    return (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ")
    
def check_column(board, col):
    return (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != " ")
    
def check_diagonals(board):
    return (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ") or\
            (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ")
            
def check_win(board):
    for i in range(2):
        if check_row(board, i):
            return True
        if check_column(board, i):
            return True
    if check_diagonals(board):
        return True
    return False
    
def is_board_full(board):
    for item in board:
        if " " in item:
            return False
    return True
    
def play(board):
    while True:
        row = input("Gib bitte die Nummer der Reihe ein (1,2 oder 3): ")
        while not row.isdigit() or int(row) < 1 or int(row) > 3:
            row = input("Fehlerhafte Eingabe. Gib bitte die Nummer der Reihe ein (1,2 oder 3): ")
        row = int(row)
        col = input("Gib Nummer der Spalte ein (1,2 oder 3): ")
        while not col.isdigit() or int(col) < 1 or int(col) > 3:
            col = input("Fehlerhafte Eingabe. Gib bitte die Nummer der Spalte ein (1,2 oder 3): ")
        col = int(col)
        if board[row-1][col-1] != " ":
            print("Wähle bitte ein freies Feld!")
        else:
            return (row-1, col-1)

def main():
    board = [ 
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # Erstelle Spieler x, Spieler o und Spielbrett
    players = ["x", "o"]
    turn = 0
    while not is_board_full(board):
        make_board(board)
        if turn == 0:
            # Spielzug Spieler x
            print("Spieler x ist dran!")
            row, col = play(board)
            board[row][col] = players[turn]
            
        else:
            # Spielzug Spieler o
            print("Spieler o ist dran!")
            row, col = play(board)
            board[row][col] = players[turn]
        # Auf Gewinner prüfen
        if check_win(board):
            make_board(board)
            print("Spieler x hat gewonnen!" if turn == 0 else "Spieler o hat gewonnen!")
            break
        
        # Nächster Spielzug, da noch kein Gewinner
        turn = 1 - turn
    
    else:
        make_board(board)
        print("Unentschieden!")
main()
