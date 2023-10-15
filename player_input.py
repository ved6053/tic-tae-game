board = None
def select_board_pos(matrix, rows, cols):
    while True:
        row = row_input(rows)
        pos = pos_input(cols)
        if matrix[row][pos] != ' ':
            print('Board is occupied, please try again')
        else:
            return (row, pos)
    

def enter_sticker(player_sticker):
    while True:
        value = input('Enter your choice(0/X): ')
        if value not in player_sticker:
            print('Worng choice , please try again')
        else:
            return value
def row_input(rows):
    while True:
        row = input('Enter Row Nubmer(1, 2, 3): ').strip()
        if row.isdigit() and (int(row) in [1, 2, 3]):
            return rows[int(row)-1]
        else:
            print('Invalid Row, please try again')

def pos_input(cols):
    while True:
        pos = input('Enter Position Number(1, 2, 3): ').strip()
        if pos.isdigit() and (int(pos) in [1, 2, 3]):
            return cols[int(pos)-1]
        else:
            print('Invalid Position, please try again')


if __name__ == '__main__':
    pass
   
        