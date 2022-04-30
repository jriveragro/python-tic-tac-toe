# ================================================================================================ #
# === User defined functions start here ========================================================== #
# ================================================================================================ #
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


    print('            |        |            ')
    print(f'     {r1[0]} | {r1[1]} | {r1[2]} ')
    print('            |        |            ')
    print('   ----------------------------')
    print('            |        |            ')
    print(f'     {r2[0]} | {r2[1]} | {r2[2]} ')
    print('            |        |            ')
    print('   ----------------------------')
    print('            |        |            ')
    print(f'     {r3[0]} | {r3[1]} | {r3[2]} ')
    print('            |        |            ')


def print_line(num):
    print('\n'*num)


def print_welcome():
    print('============================')
    print('== WELCOME TO TIC-TAC-TOE ==')
    print('============================')


def ask_user_to_play(game):
    message = 'Would you like to play? Enter Y if Yes or enter N if no:> '
    if game > 0:
        message = 'Would you like to play again? Enter Y if Yes or enter N if no:> '
    
    response = input(message)
    
    while response.lower() not in ['y', 'n']:
        response = input(message)
        
    if response.lower() == 'y':
        return True
    
    else:
        return False


def get_players_symbols():
    dict = {'player1': '', 'player2': ''}
    response = input('Player 1, please choose your symbol: X or O:> ')
    
    while response.lower() not in ['x', 'o']:
        response = input('Player 1, please choose your symbol: X or O:> ')
        
    if response.lower() == 'x':
        dict['player1'] = 'X'
        dict['player2'] = 'O' 

    elif response.lower() == 'o':
        dict['player1'] = 'O'
        dict['player2'] = 'X'

    return dict['player1'], dict['player2']


def announce_player_symbols(tracker):
    print(f'Player 1 you are {tracker["p1_symbol"]}, Player 2 you are {tracker["p2_symbol"]}.... Let\'s play!')


def display_game_turn(i):
    response = input(f'Player {i} it\'s your turn, choose your position in the board: Top line[7, 8 ,9], Center line[4, 5, 6], Bottom line[1, 2, 3]... press Q to leave the game:> ')
    
    return response


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

print_welcome()
response = ask_user_to_play(game_number)

if response == False:
    print('Ok, good-bye!')

elif response == True:
    game_tracker['p1_symbol'], game_tracker['p2_symbol'] = get_players_symbols()
    
    announce_player_symbols(game_tracker)
    print_line(1)
    
    position = ''
    game_counter = len(game_tracker['p1_selections']) + len(game_tracker['p2_selections'])
    while position.lower() != 'q':

        if  game_counter < 9:
            if (game_counter + 1) % 2 != 0:
                index = 1
            else:
                index = 2
                 
            position = display_game_turn(index)
              
            if position.lower() == 'q':
                print('The game has been ended by player. Good Bye!')
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
                        print('===============================', f'== >>> Player {index} has won! <<< ==', '===============================', sep='\n')
                        print_line(1)
                        game_number += 1
                        response = ask_user_to_play(game_number)
                        if response == False:
                            print('Ok, good-bye!')
                            break
                             
                        elif response == True:
                            row1, row2, row3, game_tracker = set_game()
                            game_tracker['p1_symbol'], game_tracker['p2_symbol'] = get_players_symbols()
                                 
                            announce_player_symbols(game_tracker)
                            print_line(1)
                    
        else:
            print('The board is full!... no one wins.')
            
            game_number += 1
            response = ask_user_to_play(game_number)
            if response == False:
                print('Ok, good-bye!')
                break
                 
            elif response == True:
                row1, row2, row3, game_tracker = set_game()
                game_tracker['p1_symbol'], game_tracker['p2_symbol'] = get_players_symbols()
                     
                announce_player_symbols(game_tracker)
                print_line(1)
             
        game_counter = len(game_tracker['p1_selections']) + len(game_tracker['p2_selections'])


            
# ================================================================================================ #
# === Main program ends here ===================================================================== #
# ================================================================================================ #



    