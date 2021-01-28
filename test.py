import unittest

from soduko_board import SodukoBoard

class TestSodukoBoard(unittest.TestCase):

    def test_initialization(self):
        """
        Test that an empty 9x9 board is correctly initializied
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        soduko = SodukoBoard(board)
        self.assertEqual(len(soduko.board[0]), 9)
        self.assertEqual(len(soduko.board), 9)
    
    def test_loading_board(self):
        new_board = [[0, 1, 0, 0, 2, 0, 0, 5, 7],
                     [0, 2, 0, 0, 3, 0, 0, 5, 7],
                     [0, 3, 0, 0, 4, 0, 0, 5, 7],
                     [0, 4, 0, 0, 5, 0, 0, 5, 7], 
                     [0, 5, 0, 0, 6, 0, 0, 5, 7], 
                     [0, 6, 0, 0, 7, 0, 0, 5, 7],
                     [0, 7, 0, 0, 8, 0, 0, 5, 7],
                     [0, 8, 0, 0, 9, 0, 0, 5, 7],
                     [0, 9, 0, 0, 1, 0, 0, 5, 7]]
        soduko = SodukoBoard(new_board)
        self.assertEqual(soduko.board[0][1], 1) 
    
    def test_entry_validity(self):
        new_board = [[0, 1, 0, 0, 2, 0, 0, 5, 7],
                     [0, 2, 0, 0, 3, 0, 0, 5, 7],
                     [0, 3, 0, 0, 4, 0, 0, 5, 7],
                     [0, 4, 0, 0, 5, 0, 0, 5, 7], 
                     [0, 5, 0, 0, 6, 0, 0, 5, 7], 
                     [0, 6, 0, 0, 7, 0, 0, 5, 7],
                     [0, 7, 0, 0, 8, 0, 0, 5, 7],
                     [0, 8, 0, 0, 9, 0, 0, 5, 7],
                     [0, 9, 0, 0, 1, 0, 0, 5, 7]]
        soduko = SodukoBoard(new_board)
        self.assertTrue(soduko.is_box_valid((1, 1), 4))
        self.assertFalse(soduko.is_row_valid((0, 3), 2))
        self.assertFalse(soduko.is_column_valid((0, 1), 1))
        self.assertTrue(soduko.is_valid_move((0,0), 4))

    def test_get_square(self):
        new_board = [[0, 1, 0, 0, 2, 0, 0, 5, 7],
                     [0, 2, 0, 0, 3, 0, 0, 5, 7],
                     [0, 3, 0, 0, 4, 0, 0, 5, 7],
                     [0, 4, 0, 0, 5, 0, 0, 5, 7], 
                     [0, 5, 0, 0, 6, 0, 0, 5, 7], 
                     [0, 6, 0, 0, 7, 0, 0, 5, 7],
                     [0, 7, 0, 0, 8, 0, 0, 5, 7],
                     [0, 8, 0, 0, 9, 0, 0, 5, 7],
                     [0, 9, 0, 0, 1, 0, 0, 5, 7]]
        soduko = SodukoBoard(new_board)
        self.assertEqual(soduko.get_square(7), 5)
        self.assertEqual(soduko.get_square(80), 7)
    
    def test_to_coordinates(self):
        s = SodukoBoard([[]])
        self.assertEqual(s.index_to_coordinates(9), (1, 0))
        self.assertEqual(s.index_to_coordinates(80), (8, 8))
        self.assertEqual(s.index_to_coordinates(19), (2, 1))

    def test_entry_validity2(self):
        easy_soduko = [
            [3, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0],
        ]
        soduko = SodukoBoard(easy_soduko)
        self.assertTrue(soduko.is_valid_move((0, 2), 5))

    def test_is_solved(self):
        easy_soduko = [
            [3, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0],
        ]
        soduko = SodukoBoard(easy_soduko)
        self.assertFalse(soduko.is_solved())

if __name__ == '__main__':
    unittest.main() 
        
