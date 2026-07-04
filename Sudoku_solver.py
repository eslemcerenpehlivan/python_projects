def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 'x':
                for num in range(1, 10):
                    char_num = str(num)
                    if is_valid(board, i, j, char_num):
                        board[i][j] = char_num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 'x'
                return False
    return True


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def print_board(board):
    print("\n" + "=" * 25 + "\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - + - - - - + - - - -")
            print()

        row_display = []
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_display.append("|")
            row_display.append(board[i][j])


        print("  " + "  ".join(row_display).replace("|", " | "))
        print()
    print("=" * 25 + "\n")


example_board = [
    ['5', '3', 'x',  'x', '7', 'x',  'x', 'x', 'x'],
    ['6', 'x', 'x',  '1', '9', '5',  'x', 'x', 'x'],
    ['x', '9', '8',  'x', 'x', 'x',  'x', '6', 'x'],

    ['8', 'x', 'x',  'x', '6', 'x',  'x', 'x', '3'],
    ['4', 'x', 'x',  '8', 'x', '3',  'x', 'x', '1'],
    ['7', 'x', 'x',  'x', '2', 'x',  'x', 'x', '6'],

    ['x', '6', 'x',  'x', 'x', 'x',  '2', '8', 'x'],
    ['x', 'x', 'x',  '4', '1', '9',  'x', 'x', '5'],
    ['x', 'x', 'x',  'x', '8', 'x',  'x', '7', '9']
]

if solve_sudoku(example_board):
    print_board(example_board)
else:
    print("Çözüm bulunamadı.")