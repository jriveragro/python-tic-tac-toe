# ================================================================================================ #
# === User defined functions start here ========================================================== #
# ================================================================================================ #
def print_line(num):
    print('\n'*num)


def get_message(key):
    message = ''

    if key.lower() == 'welcome':
        message = '== WELCOME TO TIC-TAC-TOE =='

    elif key.lower() == 'play':
        message = 'Would you like to play? Enter Y if Yes or enter N if no:>'

    elif key.lower() == 'bye':
        message = 'Ok, good-bye!'

    elif key.lower() == 'symbol':
        message = 'Player 1, please choose your symbol: X or O:>'

    elif key.lower() == 'anounce':
        message = 'Player 1 you are %s, Player 2 you are %s.... Let\'s play!'

    elif key.lower() == 'turn':
        message = 'Player %s it\'s your turn, choose your position in the board: Top line[7, 8 ,9], Center line[4, 5, 6], Bottom line[1, 2, 3]... press Q to leave the game:>'

    elif key.lower() == 'end':
        message = 'The game has been ended by player. Good Bye!'

    elif key.lower() == 'winner':
        message = f'== >>> Player %s has won! <<< =='

    elif key.lower() == 'replay':
        message = 'Would you like to play again? Enter Y if Yes or enter N if no:>'

    elif key.lower() == 'full':
        message = 'The board is full!... no one wins.'

    return message


def prompt_user(message):
    response = input(message)

    return response


def ask_user_to_play(message):
    response = prompt_user(message)
    
    while response.lower() not in ['y', 'n']:
        response = input(message)
        
    if response.lower() == 'y':
        return True
    
    else:
        return False


def get_players_symbols(message):
    dict = {'player1': '', 'player2': ''}

    response = prompt_user(message)
    
    while response.lower() not in ['x', 'o']:
        response = prompt_user(message)
        
    if response.lower() == 'x':
        dict['player1'] = 'X'
        dict['player2'] = 'O' 

    elif response.lower() == 'o':
        dict['player1'] = 'O'
        dict['player2'] = 'X'

    return dict['player1'], dict['player2']


def announce_player_symbols(tracker, message):
    print(message %(tracker['p1_symbol'], tracker['p2_symbol']))


def display_game_turn(index, message):
    response = prompt_user(message %(index))
    
    return response


def draw_board(tracker, i, r1, r2, r3):
    if tracker[f'p{i}_position'] in ['1', '2', '3']:
        if tracker[f'p{i}_position'] == '1':
            r3[0] = f'   {tracker[f"p{i}_symbol"]}  '
        
        elif tracker[f'p{i}_position'] == '2':
            r3[1] = f'   {tracker[f"p{i}_symbol"]}  '
         
        elif tracker[f'p{i}_position'] == '3':
            r3[2] = f'   {tracker[f"p{i}_symbol"]}  '
            
    elif tracker[f'p{i}_position'] in ['4', '5', '6']:
        if tracker[f'p{i}_position'] == '4':
            r2[0] = f'   {tracker[f"p{i}_symbol"]}  '
            
        elif tracker[f'p{i}_position'] == '5':
            r2[1] = f'   {tracker[f"p{i}_symbol"]}  '
               
        elif tracker[f'p{i}_position'] == '6':
            r2[2] = f'   {tracker[f"p{i}_symbol"]}  '
            
    elif tracker[f'p{i}_position'] in ['7', '8', '9']:
         if tracker[f'p{i}_position'] == '7':
            r1[0] = f'   {tracker[f"p{i}_symbol"]}  '
             
         elif tracker[f'p{i}_position'] == '8':
            r1[1] = f'   {tracker[f"p{i}_symbol"]}  '
             
         elif tracker[f'p{i}_position'] == '9':
             r1[2] = f'   {tracker[f"p{i}_symbol"]}  '


    print('            |        |            ', f'     {r1[0]} | {r1[1]} | {r1[2]} ', '            |        |            ', '   ----------------------------', sep='\n')
    print('            |        |            ', f'     {r2[0]} | {r2[1]} | {r2[2]} ', '            |        |            ', '   ----------------------------', sep='\n')
    print('            |        |            ', f'     {r3[0]} | {r3[1]} | {r3[2]} ', '            |        |            ', sep='\n')


def is_winner(selections):
    winner_lines = [('1', '2', '3'), ('1', '5', '9'), ('1', '4', '7'), ('2', '5', '8'), 
                    ('3', '5', '7'), ('3', '6', '9'), ('4', '5', '6'), ('7', '8', '9')]
    is_winner = False

    for element in winner_lines:
        in_winner_line = 0
        for number in element:
            if number in selections:
                in_winner_line += 1
                if in_winner_line == 3:
                    is_winner = True
                    break
    
    return is_winner


def display_winner(index, message):
    print(message %(index))


def set_game():
    r1 = ['      ','      ','      ']
    r2 = ['      ','      ','      ']
    r3 = ['      ','      ','      ']
    
    tracker = {'p1_symbol': '', 'p1_position': 0, 'p1_turn': 1, 'p1_selections': [], 
                    'p2_symbol': '', 'p2_position': 0, 'p2_turn': 2, 'p2_selections': []}
    
    return r1, r2, r3, tracker
# ================================================================================================ #
# === User defined functions end  here =========================================================== #
# ================================================================================================ #


# ================================================================================================ #
# === Main program starts here =================================================================== #
# ================================================================================================ #
row1, row2, row3, game_tracker = set_game()
game_number = 0

msg = get_message('welcome')
print(msg)

msg = get_message('play')
response = ask_user_to_play(msg)

if response == False:
    msg = get_message('bye')
    print(msg)

elif response == True:
    msg = get_message('symbol')
    game_tracker['p1_symbol'], game_tracker['p2_symbol'] = get_players_symbols(msg)
    
    msg = get_message('anounce')
    announce_player_symbols(game_tracker, msg)
    print_line(1)
    
    position = ''
    play_counter = len(game_tracker['p1_selections']) + len(game_tracker['p2_selections'])
    while position.lower() != 'q':

        if  play_counter < 9:
            if (play_counter + 1) % 2 != 0:
                index = 1
            else:
                index = 2
                 
            msg = get_message('turn')     
            position = display_game_turn(index, msg)
              
            if position.lower() == 'q':
                msg = get_message('end')
                print(msg)
                break
               
            elif position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                game_tracker[f'p{index}_position'] = position
                game_tracker[f'p{index}_selections'].append(position)
                
                draw_board(game_tracker, index, row1, row2, row3)
                print_line(1)
                 
                if len(game_tracker[f"p{index}_selections"]) >= 3:
                    selections = sorted(game_tracker[f"p{index}_selections"])

                    if is_winner(selections) == True:
                        print_line(1)

                        msg = get_message('winner')
                        display_winner(index, msg)
                        print_line(1)

                        game_number += 1

                        msg = get_message('replay')
                        response = ask_user_to_play(msg)
                        if response == False:
                            msg = get_message('end')
                            print(msg)
                            break
                             
                        elif response == True:
                            row1, row2, row3, game_tracker = set_game()

                            msg = get_message('symbol')
                            game_tracker['p1_symbol'], game_tracker['p2_symbol'] = get_players_symbols(msg)
                                 
                            msg = get_message('anounce')
                            announce_player_symbols(game_tracker, msg)
                            print_line(1)
                    
        else:
            msg = get_message('full')
            print(msg)

            msg = get_message('replay')
            response = ask_user_to_play(msg)
            if response == False:
                msg = get_message('end')
                print(msg)
                break
                 
            elif response == True:
                row1, row2, row3, game_tracker = set_game()

                msg = get_message('symbol')
                game_tracker['p1_symbol'], game_tracker['p2_symbol'] = get_players_symbols(msg)
                     
                msg = get_message('anounce')
                announce_player_symbols(game_tracker, msg)
                print_line(1)
             
        play_counter = len(game_tracker['p1_selections']) + len(game_tracker['p2_selections'])

# ================================================================================================ #
# === Main program ends here ===================================================================== #
# ================================================================================================ #



    