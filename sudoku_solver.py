# source: https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
class SudokuSolver:
    def __init__(self, board):
        self.board = board
    
    def showBoard(self):
        count = 0
        for i in self.board:
            if count % 3 == 0:
                print(("+" + "-" * 7) * 3 + "+")
            print("|", *i[:3], "|", *i[3:6], "|", *i[6:], "|")
            count += 1
        print(("+" + "-" * 7) * 3 + "+\n")

    def solve(self):
        find = self.isEmpty()
        if not find:
            return True
        
        row, col = find
        for i in range(1, 10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def isEmpty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def valid(self, number, position):
        # check row
        for i in range(len(self.board[0])):
            if self.board[position[0]][i] == number and position[1] != i:
                return False
        
        # check column
        for i in range(len(self.board)):
            if self.board[i][position[1]] == number and position[0] != i:
                return False
        
        # check box
        box_x = position[1] // 3
        box_y = position[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == number and (i,j) != position:
                    return False
        return True


if __name__ == "__main__":
    task = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    sudoku = SudokuSolver(task)
    sudoku.showBoard()
    sudoku.solve()
    sudoku.showBoard()