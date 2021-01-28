class SodukoBoard:

    def __init__(self, board):
        self.empty_square = 0
        self.num_rows = 9
        self.num_cols = 9
        self.box_size = 3
        self.board = board
        
    def load_board(self, board):
        """Loads a pre-made soduko board and

        Board should be a list of list, with the correct number of rows and 
        columns, and each square should be an integer with values between 0 adn 9 inclusive.
        """
        # Check for valid board state
        assert len(board) == self.num_cols, "Incorrect number of colums in soduko board"
        assert len(board[0]) == self.num_rows, "Incorrect number of rows in soduko board"
        for row in board:
            for square in row:
                assert type(square) is int, "Invalid Square type; must be integers"
                assert square >= 0 and square <= self.num_rows, 'Invalid square value; must be [0, 9]'
        self.board = board

    def is_valid_move(self, coordinates, value):
        assert type(coordinates) is tuple, "Coordinates must be a tuple"
        assert value != 0  and value <= self.num_rows, "Invalid square value; must be [1, 9]"

        return self.is_box_valid(coordinates, value) and self.is_row_valid(coordinates, value) and self.is_column_valid(coordinates, value)

    def is_box_valid(self, coordinates, value):
        """
        Assumes coordinates and value are valid.
        """
        start_coordinates = (coordinates[0] - coordinates[0] % self.box_size,
                            coordinates[1] - coordinates[1] % self.box_size)
        for i in range(self.box_size):
            for j in range(self.box_size):
                square = self.board[start_coordinates[0] + i][start_coordinates[1] + j]
                if square == value:
                    return False
        return True

    def is_row_valid(self, coordinates, value):
        """
        Assumes coordinates and value are valid.
        """
        for i in range(self.num_cols):
            square = self.board[coordinates[0]][i]
            if square == value:
                return False
        return True
    
    def is_column_valid(self, coordinates, value):
        """
        Assumes coordinates and value are valid.
        """
        for i in range(self.num_rows):
            square = self.board[i][coordinates[1]]
            if square == value:
                return False
        return True

    def get_square(self, index):
        return self.board[index // self.num_cols][index % self.num_rows]
    
    def set_square(self, index, value):
        self.board[index // self.num_cols][index % self.num_rows] = value

    def index_to_coordinates(self, index):
        return (index // self.num_cols, index % self.num_rows)