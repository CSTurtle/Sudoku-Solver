def prev_cell(row, col):
    if col == 0:
        return row - 1, 8
    else:
        return row, col - 1


def next_cell(row, col):
    if col == 8:
        return row + 1, 0
    else:
        return row, col + 1

def init_mat(matrix):
    given_mat = []
    not_in_row = {i: [] for i in range(9)}
    not_in_col = {i: [] for i in range(9)}
    not_in_box = {i: [] for i in range(9)}
    for row in range(0, 9):
        for col in range(0, 9):
            if matrix[row][col] != 0:
                not_in_row[row].append(matrix[row][col])
                not_in_col[col].append(matrix[row][col])
                not_in_box[row // 3 * 3 + col // 3].append(matrix[row][col])
                given_mat.append((row, col))

    return matrix, given_mat, not_in_row, not_in_col, not_in_box


def solve_sudoku(sudoku_mat):
    sudoku_board, given_board, not_in_row, not_in_col, not_in_box = init_mat(sudoku_mat)
    bactracking = False
    row, col = 0, 0
    while row < 9:
        while col < 9:
            # Check if the cell is given
            if row > 8 or row < 0:
                return sudoku_board
            if (row, col) not in given_board:
                current_cell = sudoku_board[row][col]
                # The ungiven cell is not 0, we are backtracking,
                if current_cell != 0:
                    sudoku_board[row][col] = 0
                    not_in_row[row].remove(current_cell)
                    not_in_col[col].remove(current_cell)
                    not_in_box[row // 3 * 3 + col // 3].remove(current_cell)

                for num in range(1, 10):
                    if (
                        num > current_cell
                        and num not in not_in_row[row]
                        and num not in not_in_col[col]
                        and num not in not_in_box[row // 3 * 3 + col // 3]
                    ):
                        sudoku_board[row][col] = num
                        not_in_row[row].append(num)
                        not_in_col[col].append(num)
                        not_in_box[row // 3 * 3 + col // 3].append(num)
                        break

                if sudoku_board[row][col] == 0:
                    row, col = prev_cell(row, col)
                    bactracking = True
                else:
                    row, col = next_cell(row, col)
                    bactracking = False
            else:
                if bactracking:
                    row, col = prev_cell(row, col)
                else:
                    row, col = next_cell(row, col)
    return sudoku_board


def main():
    mat = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


    print("Initial Sudoku Board:")
    for row in range(9):
        for col in range(9):
            print(mat[row][col], end=" ")
        print()

    print("Solved Sudoku Board:")
    solved_mat = solve_sudoku(mat)
    for row in range(9):
        for col in range(9):
            print(solved_mat[row][col], end=" ")
        print()

if __name__ == "__main__":
    main()
