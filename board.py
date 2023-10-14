import player_input
matrix = [
    ['| ',' ','| ',' ', '| ',' ', '|'],
    ['| ',' ','| ',' ', '| ',' ', '|'],
    ['| ',' ','| ',' ', '| ',' ', '|']
]
ROW1 = 0
ROW2 = 1
ROW3 = 2
POS1 = 1
POS2 = 3
POS3 = 5
rows = [ROW1, ROW2, ROW3]
cols = [POS1, POS2, POS3]
player_sticker = None

def is_board_full():
    for row in rows:
        for pos in cols:
            if matrix[row][pos] == ' ':
                return False
    return True

def display():
    print(' --------')
    for row in matrix:
        print(''.join(row))
        print(' --------')
def select_pos():
    return player_input.select_board_pos(matrix, rows, cols)
def fill_choice(row, pos):
    matrix[row][pos] = player_input.enter_choice(player_sticker)

def is_winner(row, pos):
    if is_center(row, pos):
        return is_top_right_corner(row, pos) or is_left_diagnal_match(row, pos) or is_vertical_match(pos) or is_horizental_match(row)
    if is_top_left_corner(row, pos) or is_bottom_right_corner(row, pos):
        return is_left_diagnal_match(row, pos) or is_vertical_match(row) or is_horizental_match(pos)
    elif is_top_right_corner(row, pos) or is_bottom_right_corner(row, pos):
        return is_right_daignal_math(row, pos) or is_vertical_match(row) or is_horizental_match(pos) 
    elif is_middle(row, pos):
        return is_vertical_match(row) or is_horizental_match(pos) 
    else:
        return False
    

def is_top_left_corner(row, pos):
    return (row == 0 and pos == 0 )
def is_top_right_corner(row, pos):
    return (row == 0 and pos == 2 )
def is_bottom_left_corner(row, pos):
    return (row == 2 and pos == 0 )
def is_bottom_right_corner(row, pos):
    return (row == 2 and pos == 2 )
def is_middle(row, pos):
     return (row == 1 and pos == 0) or (row == 1 and pos == 2) or (row == 0 and pos == 1) or (row == 2 and pos == 1)
def is_center(row, pos):
    return (row == 1 and pos == 1)
def is_left_diagnal_match(row, pos):
    for x, y in zip([-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2]):
        x += row
        y += pos
        if (x in [0, 1, 2]) and (y in [0, 1, 2]):
            if matrix[rows[x]][cols[y]] not in player_sticker:
                return False
    return True
    
def is_right_daignal_math(row, pos):
    for x, y in zip([-2, -1, 0, 1, 2], [2, 1, 0, -1, -2]):
        x += row
        y += pos
        if (x in [0, 1, 2]) and (y in [0, 1, 2]):
            if matrix[rows[x]][cols[y]] not in player_sticker:
                return False
    return True
def is_horizental_match(pos):
    for row in [0, 1, 2]:
        if matrix[rows[row]][cols[pos]] not in player_sticker:
            return False
    return True
def is_vertical_match(row):
    for pos in [0, 1, 2]:
        if matrix[rows[row]][cols[pos]] not in player_sticker:
            return False
    return True
if __name__=='__main__':
    pass

