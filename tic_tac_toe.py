def draw_board(row1, row2, row3):
    print('            |        |            ')
    print(f'     {row1[0]} | {row1[1]} | {row1[2]} ')
    print('            |        |            ')
    print('   ----------------------------')
    print('            |        |            ')
    print(f'     {row2[0]} | {row2[1]} | {row2[2]} ')
    print('            |        |            ')
    print('   ----------------------------')
    print('            |        |            ')
    print(f'     {row3[0]} | {row3[1]} | {row3[2]} ')
    print('            |        |            ')


def print_line(num):
    print('\n'*num)


def print_welcome():
    print('============================')
    print('== WELCOME TO TIC-TAC-TOE ==')
    print('============================')


def ask_user_to_play():
    response = input('Would you like to play? Enter Y if Yes or enter N if no:> ')
    
    while response.lower() not in ['y', 'n']:
        response = input('Would you like to play? Enter Y if Yes or enter N if no:> ')
        
    if response.lower() == 'y':
        return True
    
    else:
        return False


def get_players_symbols():
    dict = {'player1': '', 'player2': ''}
    response = input('PLayer 1, please choose your symbol. X or O:> ')
    
    while response.lower() not in ['x', 'o']:
        response = input('PLayer 1, please choose your symbol. X or O:> ')
        
    if response.lower() == 'x':
        dict['player1'] = 'x'
        dict['player2'] = 'o' 

    elif response.lower() == 'o':
        dict['player1'] = 'o'
        dict['player2'] = 'x'

    return dict


r1 = ['      ','      ','      ']
r2 = ['      ','      ','      ']
r3 = ['      ','      ','      ']

game_tracker = {'p1_symbol': '', 'p1_position': 0, 'p1_turn': 1, 'p2_symbol': '', 'p2_position': 0, 'p2_turn': 2}

print_welcome()
response = ask_user_to_play()

if response == False:
    print('Ok, good-bye!')

elif response == True:
    players = get_players_symbols()
    game_tracker['p1_symbol'] = players["player1"].upper()
    game_tracker['p2_symbol'] = players["player2"].upper()
    print(f'Player 1 you are {players["player1"].upper()}, Player 2 you are {players["player2"].upper()}.... Let\'s play!')
    print_line(1)
    
    position = ''
    game_counter = 1
    while position.lower() != 'q':
        if game_counter % 2 != 0:
            index = 1
        else:
            index = 2

        position = input(f'Player {index} it\'s your turn, choose your position in the board: Top line[7, 8 ,9], Center line[4, 5, 6], Bottom line[1, 2, 3]... press Q to leave the game:> ')

        if position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            game_tracker[f'p{index}_position'] = position

            if position in ['1', '2', '3']:
                if position == '1':
                    r3[0] = f'   {game_tracker[f"p{index}_symbol"]}  '

                elif position == '2':
                    r3[1] = f'   {game_tracker[f"p{index}_symbol"]}  '

                elif position == '3':
                    r3[2] = f'   {game_tracker[f"p{index}_symbol"]}  '
        
            elif position in ['4', '5', '6']:
                if position == '4':
                    r2[0] = f'   {game_tracker[f"p{index}_symbol"]}  '
        
                elif position == '5':
                    r2[1] = f'   {game_tracker[f"p{index}_symbol"]}  '
        
                elif position == '6':
                    r2[2] = f'   {game_tracker[f"p{index}_symbol"]}  '
        
            elif position in ['7', '8', '9']:
                if position == '7':
                    r1[0] = f'   {game_tracker[f"p{index}_symbol"]}  '
        
                elif position == '8':
                    r1[1] = f'   {game_tracker[f"p{index}_symbol"]}  '
        
                elif position == '9':
                    r1[2] = f'   {game_tracker[f"p{index}_symbol"]}  '

            print_line(1)
            draw_board(r1, r2, r3)
            game_counter += 1
            print_line(1)

        elif position.lower() == 'q':
           print('The game has been ended by user. Good Bye!')



    