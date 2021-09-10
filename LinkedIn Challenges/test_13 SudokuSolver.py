""" 
Function takes a list and recursively solves the sudoku

"""
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]
        ]

def solve(puzzle: list) -> list:
    to_check = range(1,10)

def valid_column_entry(col: int, candidate: int) -> bool:
    for eachRow in puzzle:
        if candidate == eachRow[col]:
            return False
    return True

def valid_row_entry(row: int, candidate: int) -> bool:
    return candidate not in puzzle[row]

def valid_square_entry(row: int, col: int, candidate: int) -> bool:
    square_row = int(row/3)
    square_col = int(col/3)
    square = [puzzle[row][col:col+3],
            puzzle[row+1][col:col+3],
            puzzle[row+2][col:col+3]]
    for each_row in square:
        print(each_row)
    print("\n")

    for i in range(square_row*3, square_row*3+3):
        for j in range(square_col*3, square_col*3+3):
            if candidate == puzzle[i][j]:
                return False
    return True


# solve(puzzle)

def test_valid_column_entry():
    assert valid_column_entry(0,5) == False
    assert valid_column_entry(0,9) == True
    assert valid_column_entry(2,8) == False
    assert valid_column_entry(2,9) == True

def test_valid_row_entry():
    assert valid_row_entry(0,5) == False
    assert valid_row_entry(0,9) == True
    assert valid_row_entry(8,8) == False
    assert valid_row_entry(8,1) == True

def test_valid_square_entry():
    assert valid_square_entry(0,0,5) == False
    assert valid_square_entry(0,0,8) == False
    assert valid_square_entry(0,0,1) == True
    assert valid_square_entry(3,3,2) == False
    assert valid_square_entry(3,3,3) == False
    assert valid_square_entry(3,3,4) == True
    assert valid_square_entry(6,6,2) == False
    assert valid_square_entry(6,6,9) == False
    assert valid_square_entry(6,6,3) == True