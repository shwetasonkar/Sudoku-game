from typing import Union, Tuple, List

__all__ = ['Sudoku', 'CELL_IDX']

# Constants
CELL_IDX = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# Main class
class Sudoku:
    """A Sudoku game board
    === Attributes ===
    dim: the dimension of the board
    moves: a list that stores all the previous moves made by player
    board: a 2D-list that represents a sudoku game board
    """

    _dim: int
    moves: List[Tuple[Tuple[int, int], int, bool]]
    _board: List[List[int]]

    def __init__(self, dim, board=None) -> None:
        self._dim = dim
        self.moves = []

        if board is None:
            # Create empty board
            self._board = [[0 for _ in range(dim)]
                           for _ in range(dim)]
        else:
            # Copy board grid
            self._board = [[board[row][col] for col in range(dim)]
                           for row in range(dim)]

    def __str__(self) -> str:
        """Human readable representation of the board."""
        rep = ""
        for row in range(self._dim):
            for col in range(self._dim):
                rep += str(self._board[row][col])
                if col == self._dim - 1:
                    rep += "\n"
                else:
                    rep += " | "
            if row != self._dim - 1:
                rep += "-" * (4 * self._dim - 3)
                rep += "\n"
        return rep

    def get_dim(self) -> int:
        """Return the dimension of the board
        >>> game = Sudoku(9)
        >>> game.get_dim()
        9
        >>> game = Sudoku(3)
        >>> game.get_dim()
        3
        """
        return self._dim

    def get_board(self) -> List[List[int]]:
        """Return the board as a 2-dimension list
        >>> game = Sudoku(3)
        >>> game.get_board()
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        """
        return self._board

    def get_square(self, row: int, col: int) -> int:
        """Get the contents of the board at position (row, col).
        === Attributes ===
        row: the row on the board
        col: the column on the board
        >>> game = Sudoku(9)
        >>> game.get_square(1, 1)
        0
        """
        return self._board[row][col]

    def get_last_move(self) -> Union[Tuple, None]:
        """Get the last move made by the user.
        === Returns ===
        the last ID in the moves list
        """
        if self.moves:
            return self.moves.pop()
        else:
            return None

    def set_square(self, row: int, col: int, num: int) -> None:
        """Place number on the board at position (row, col).
        === Attributes ===
        row: the row of the board
        col: the column of the board
        num: the number that is filled into the square
        >>> game = Sudoku(3)
        >>> game.set_square(1, 1, 3)
        >>> game.get_square(1, 1)
        3
        """
        self._board[row][col] = num

    def add_move(self, pos: Tuple[int, int], num: int, pencil: bool) -> None:
        """Add the ID of the square to moves list
        === Attributes ===
        pos: the position of the square
        num: the number placed on the move
        pencil: bool that indicate whether pencil is toggled
        >>> game = Sudoku(3)
        >>> game.add_move((1, 1), 3, True)
        >>> game.moves
        [((1, 1), 3, True)]
        """
        self.moves.append((pos, num, pencil))

    def get_pos_from_num(self, num: int) -> List[Tuple[int, int]]:
        """Get all number: num, positions (row, col) on the board
        === Attributes ===
        num: the number that will be searched
        === Returns ===
        a list of (row, col) positions
        """
        # initialize variable
        result = []

        # search for num
        for row in range(self._dim):
            for col in range(self._dim):
                if self._board[row][col] == num:
                    result.append((row, col))

        return result

    def get_row_col_cell(self) -> Tuple[List[list], List[list], List[list]]:
        """Get all the rows, columns, and cells from board variable
        === Returns ===
        rows, columns and cells of the board
        """
        # row
        rows = self._board.copy()

        # column
        cols = []
        for col in range(self._dim):
            column = []
            for row in range(self._dim):
                column.append(self._board[row][col])
            cols.append(column)

        # cell
        cells = []
        for idx1 in CELL_IDX:
            for idx2 in CELL_IDX:
                cell = []
                for row in idx1:
                    for col in idx2:
                        cell.append(self._board[row][col])

                cells.append(cell)

        # return row, column and cell in one 2D-list
        return rows, cols, cells

    def verify_board(self) -> Union[bool, set]:
        """Verify whether the board is complete
        === Returns ===
        the state of the board as a bool or a set of duplicated numbers
        """
        # store all rows, columns, and cells in one list
        row_col_cells = self.get_row_col_cell()
        lst = [config for item in row_col_cells for config in item]
        state = True

        # check whether the board is incomplete or not
        for row in self._board:
            if 0 in row:
                state = False

        # check for duplicate number
        duplicate_num = set([])
        for config in lst:
            for num in set(config):
                if config.count(num) > 1 and num != 0:
                    duplicate_num.add(num)

        if not duplicate_num:
            return state
        else:
            return duplicate_num


if __name__ == '__main__':
    import doctest

    doctest.testmod()
