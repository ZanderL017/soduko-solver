from soduko_board import SodukoBoard
import pprint

pp = pprint.PrettyPrinter()

easy_soduko = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
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

def solve(soduko_board, current_square_i, solved):
    if current_square_i > 80:
        solved = True
        pp.pprint(soduko_board.board)
    if solved:
        print('Solved!')
        return
    else:
        #try each number
        for value in range(1, 10):
            #Put the number in
            
            # if the number is valid, move into the next empty square
            coordinates = soduko_board.index_to_coordinates(current_square_i)
            if soduko_board.is_valid_move(coordinates, value):
                soduko_board.set_square(current_square_i, value)
                solve(soduko_board, next_square_i(soduko_board, current_square_i), solved)
                if solved:
                    break
                if not solved:
                    soduko_board.set_square(current_square_i, 0)


def next_square_i(soduko_board, current_square_i):
    if current_square_i == 80:
        return 81
    next_square_i = current_square_i + 1
    while soduko_board.get_square(next_square_i) != 0:
        next_square_i += 1
        if next_square_i > 80:
            break
    return next_square_i

solve(soduko, 0, False)