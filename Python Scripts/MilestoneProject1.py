### Tic Tac Toe ###

# Here are the requirements:
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ',9: ' ', }
tokens = {0: 'z', 1: 'z'}

def game_prompt():
    print('******************** Tic Tac Toe ********************')
    print('Alternate guesses between Player 1 and Player 2 \n')

#position is available if value is ' '. Return true if available
def is_position_available(num):
    return board[num] == ' '

def assign_position(player_token, num, board):
    board[num] = player_token

def draw_board():
    print('\n'*10)
    print(f'{board[7]} | {board[8]} | {board[9]}' )
    print('----------')
    print(f'{board[4]} | {board[5]} | {board[6]}' )
    print('----------')
    print(f'{board[1]} | {board[2]} | {board[3]}' )

def clear_board():
    for key in board: 
        board[key] = ' '

def swap_tokens(cur_token):
    if cur_token == tokens[0]:
        return tokens[1]
    elif cur_token == tokens[1]:
        return tokens[0]

def get_token_prompt():
    token = input('Select Player 1 token (X/O): ')
    while not token.upper() in ['X', 'O']:
        print('Invalid entry, try again.')
        token = input('Select Player 1 token (X/O): ')
    
    if token.upper() == 'X':
        tokens[0] = 'X'
        tokens[1] = 'O'
    elif token.upper() == 'O':
        tokens[0] = 'O'
        tokens[1] = 'X'

def get_input():
    position = ''
    position = input('Select position 1-9 to mark the board: ')
    while not position.isdigit() or int(position) not in range(1,9+1) or not is_position_available(int(position)):
        print('\nPosition is taken or invalid entry, try again.\n')
        position = input('Select position 1-9 to mark the board: ')
    return int(position)

def finish_playing_prompt():
    answer = input('Are you done playing? (Yes/No): ')
    while not answer.isalpha or answer.lower() not in ['yes', 'no']:
        print('Invalid entry, try again')
        answer = input('Are you done playing? (Yes/No): ')
    if answer.lower() == 'yes':
        return True
    elif answer.lower() == 'no':
        return False

#winning conditions
def is_winner(player_token):
      #check columns
    if(board[1] == board[4] == board[7] == player_token or
       board[2] == board[5] == board[8] == player_token or
       board[3] == board[6] == board[9] == player_token or
       #check rows
       board[1] == board[2] == board[3] ==  player_token or
       board[4] == board[5] == board[6] == player_token or
       board[7] == board[8] == board[9] == player_token or 
       #check diagonals
       board[1] == board[5] == board[9] == player_token or
       board[3] == board[5] == board[7] == player_token):
        return True
    else:
        return False

def play_game():
    is_game_done = False
    current_token = tokens[0]
    turns = 0
    final_string = 'WINNER'

    while not is_game_done:
        player_input = get_input()
        assign_position(current_token, player_input, board)
        draw_board()
        is_game_done = is_winner(current_token)
        turns += 1
        current_token = swap_tokens(current_token)
        if turns == 9 and not is_game_done:
            final_string = 'TIE GAME'
            break
    print(f'{final_string} in {turns} turns!\n')

if __name__ == '__main__':
    game_prompt()
    get_token_prompt()
    while True:
        play_game()
        if finish_playing_prompt():
            break
        clear_board()