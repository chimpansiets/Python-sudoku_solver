## Searches for the first zero available on the field.
def find_next_zero(puzzle):
    for i in range(len(puzzle)):
        for x in range(len(puzzle[i])):
            if puzzle[i][x] == 0:
                return [i, x]

def check_box(value, box, puzzle):
    occurences = 0
    for i in range(0, 3):
        for x in range(0, 3):
            if value == puzzle[box[0] + i][box[1] + x]:
                occurences += 1
                if occurences > 1:
                    return 1
    return 0

def which_box(y_x):
    if 0 <= y_x[0] and y_x[0] <= 2:
        if 0 <= y_x[1] and y_x[1] <= 2:
            return [0, 0]
        elif 3 <= y_x[1] and y_x[1] <= 5:
            return [0, 3]
        elif 6 <= y_x[1] and y_x[1] <= 8:
            return [0, 6]
    elif 3 <= y_x[0] and y_x[0] <= 5:
        if 0 <= y_x[1] and y_x[1] <= 2:
            return [3, 0]
        elif 3 <= y_x[1] and y_x[1] <= 5:
            return [3, 3]
        elif 6 <= y_x[1] and y_x[1] <= 8:
            return [3, 6]
    elif 6 <= y_x[0] and y_x[0] <= 8:
        if 0 <= y_x[1] and y_x[1] <= 2:
            return [6, 0]
        elif 3 <= y_x[1] and y_x[1] <= 5:
            return [6, 3]
        elif 6 <= y_x[1] and y_x[1] <= 8:
            return [6, 6]

## Checks if there are multiple occurences in the same row/column as the value
## If there are, returns False, else it is valid.
def is_valid(y_x, puzzle):
    value = puzzle[y_x[0]][y_x[1]]
    for i in range(0, 9):
        if value == puzzle[y_x[0]][i] and i != y_x[1]:
            return 0
    for i in range(0, 9):
        if value == puzzle[i][y_x[1]] and i != y_x[0]:
            return 0
    box = which_box(y_x)
    if check_box(value, box, puzzle) == 1:
        return 0
    return 1

## Finds the first available zero on the field, then checks values 1-9 for validity.
## If 1-9 are all invalid, goes back on the recursive stack to edit it's LAST filled in value.
## When the last filled in value is valid AND the whole map has been filled (find_next_zero == None),
## Then it returns the Sudoku.
def solve_puzzle(puzzle):
    y_x = find_next_zero(puzzle)
    if y_x == None:
        return puzzle
    for i in range(1, 10):
        puzzle[y_x[0]][y_x[1]] = i
        if is_valid(y_x, puzzle):
            if find_next_zero(puzzle) == None:
                return puzzle
            solve_puzzle(puzzle)
    puzzle[y_x[0]][y_x[1]] = 0


def sudoku(puzzle):
    _puzzle = None
    while _puzzle == None:
        _puzzle = solve_puzzle(puzzle)
    return _puzzle