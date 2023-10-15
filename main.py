import player_one
import player_two
import board
def main():
    game_over = False
    board.display()
    player_turn = 0
    while game_over == False:
        player = select_player(player_turn)
        game_over = play(player)
        player_turn = (player_turn+1)%2

def select_player(player_turn):
    players = [player_one, player_two]
    return players[player_turn]

def play(player):
    if is_tie():
        print('Game Over, It is a tie')
        return True
    print(f'**********************Player {player.name} playing the game*************')
    row, pos = fill_an_empty_cell_on_board(player)
    if board.is_winner(row, pos) == True:
        print(f'Game Over, {player.name} win the Game')
        return True
    else:
        return False

def is_tie():
    return board.is_board_full()

def fill_an_empty_cell_on_board(player):
    while True:
        row , pos = board.select_pos()
        if board.matrix[row][pos] != ' ':
            print('Cell occupied on Board, please try again')
        else:
            board.player_sticker = player.sticker
            board.fill_sticker(row, pos)
            break
    board.display()
    return (board.rows.index(row), board.cols.index(pos)) 

if __name__== '__main__':
    main()



    
