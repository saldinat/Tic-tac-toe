import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    The function returns true if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1, 0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    return min_value <= value <= max_value
   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.

def game_board_full(board):
    """ (str) -> bool

    The function returns true if the board's cell are full (i.e. all the cells
    have been chosen).

    >>> game_board_full('XOXXXOXOX')
    True
    >>> game_board_full('XOXXXOX-X')
    False
    """
    return '-' not in board

def get_board_size(board):
    """ (str) -> int

    The function returns the size of the given tic-tac-toe game board.
    The minimum size is 1, the maximum size is 9.
    
    >>> get_board_size('XXOX')
    2
    >>> get_board_size('XOXXXOXOX')
    3
    """
    return int(math.sqrt(len(board)))

def make_empty_board(board_size):
    """ (int) -> str

    Precondition: 1 <= value <= 9

    The function returns a string of the game board of the given size where no
    cells have been chosen yet.

    >>> make_empty_board(3)
    '---------'
    >>> make_empty_board(5) 
    '-------------------------'
    """
    return '-' * (board_size ** 2)
    
def get_position(row_index, col_index, board_size):
    """ (int, int, int) -> int

    The function returns the index of the particular cell in the game board of
    the given size.
    >>> get_position(2, 4, 4)
    7
    >>> get_position(3, 2, 4)
    9
    """
    str_index = (row_index - 1) * board_size + col_index - 1
    return str_index


def make_move(symbol, row_index, col_index, board):
    """ (str, int, int, str) -> str

    The function returns the board string with the wanted symbol placed
    instead of the given empty cell in the given board.
    >>> make_move('X', 3, 2, 'O-O-X-X--')
    'O-O-X-XX-'
    >>> make_move('0', 3, 2, 'O-OXXO--X')
    'O-OXXO-OX'
    """
    str_index = (row_index - 1) * get_board_size(board) + col_index - 1
    return board[:str_index] + symbol + board[(str_index + 1):]


def extract_line(board, direction, row_or_column):
    """ (str, str, int) -> str
    >>> extract_line('--------XXXX----', 'across', 3)
    'XXXX'
    >>> extract_line('------XXX', 'across', 3)
    'XXX'
    >>> extract_line('-O---O---O---O--', 'down', 2)
    'OOOO'
    >>> extract_line('--X--X--X', 'down', 3)
    'XXX'
    >>> extract_line('X---X---X', 'down_diagonal', 2)
    'XXX'
    >>> extract_line('O----O----O----O', 'down_diagonal', 2)
    'OOOO'
    >>> extract_line('---X--X--X--X---', 'up_diagonal', 2)
    'XXXX'
    >>> extract_line('--X-X-X--', 'up_diagonal', 2)
    'XXX'
    
    The function returns: a specified row when direction is 'across',
                          a specifued column when direction is 'down',
                          a specified diagonal when directions are
                          'down_diagonal' and 'up_diagonal'
    """                         
    
    size = get_board_size(board)
    if direction == 'across':
        return board[(row_or_column - 1) * size:(row_or_column - 1) * size + size]
    elif direction == 'down':
        return board[row_or_column - 1::size]
    elif direction == 'down_diagonal':
        return board[::size+1]
    elif direction == 'up_diagonal':
        return board[-size:-len(board):1-size]




