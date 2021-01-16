import unittest

from soduko_board import SodukoBoard

class TestSodukoBoard(unittest.TestCase):

    def test_initialization(self):
        """
        Test that an empty 9x9 board is correctly initializied
        """
        soduko = SodukoBoard()
        self.assertEqual(len(soduko.board[0]), 9)
        self.assertEqual(len(soduko.board), 9)
    
    def test_loading_board(self):
        soduko = SodukoBoard()
        new_board = [[0, 1, 0, 0, 2, 0, 0, 5, 7],
                     [0, 2, 0, 0, 3, 0, 0, 5, 7],
                     [0, 3, 0, 0, 4, 0, 0, 5, 7],
                     [0, 4, 0, 0, 5, 0, 0, 5, 7], 
                     [0, 5, 0, 0, 6, 0, 0, 5, 7], 
                     [0, 6, 0, 0, 7, 0, 0, 5, 7],
                     [0, 7, 0, 0, 8, 0, 0, 5, 7],
                     [0, 8, 0, 0, 9, 0, 0, 5, 7],
                     [0, 9, 0, 0, 1, 0, 0, 5, 7]]
        soduko.load_board(new_board)
        self.assertEqual(soduko.board[0][1], 1) 
    
    def test_entry_validity(self):
        soduko = SodukoBoard()
        new_board = [[0, 1, 0, 0, 2, 0, 0, 5, 7],
                     [0, 2, 0, 0, 3, 0, 0, 5, 7],
                     [0, 3, 0, 0, 4, 0, 0, 5, 7],
                     [0, 4, 0, 0, 5, 0, 0, 5, 7], 
                     [0, 5, 0, 0, 6, 0, 0, 5, 7], 
                     [0, 6, 0, 0, 7, 0, 0, 5, 7],
                     [0, 7, 0, 0, 8, 0, 0, 5, 7],
                     [0, 8, 0, 0, 9, 0, 0, 5, 7],
                     [0, 9, 0, 0, 1, 0, 0, 5, 7]]
        soduko.load_board(new_board)
        self.assertTrue(soduko.is_box_valid((1, 1), 4))
        self.assertFalse(soduko.is_row_valid((0, 3), 2))
        self.assertFalse(soduko.is_column_valid((0, 1), 1))

if __name__ == '__main__':
    unittest.main()