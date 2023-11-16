# username = input('enter name:')
# print(f'username is: {username}')

def title():
    print("---------------------")
    print("Let's play Py-Pac-Poe")
    print("---------------------")

state = {'board': {}, 'turn': 'X', 'count': 0}

def init_game():
    state['board'] = {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }

def print_board(board):
    print('')
    print('   A   B   C')
    print('1) ' + state['board']['a1'] + ' | ' + state['board']['b1'] + ' | ' + state['board']['c1'])
    print('   ----------')
    print('2) ' + state['board']['a2'] + ' | ' + state['board']['b2'] + ' | ' + state['board']['c2'])
    print('   ----------')
    print('3) ' + state['board']['a3'] + ' | ' + state['board']['b3'] + ' | ' + state['board']['c3'])
    print('      ')

def get_move():
    state['turn'] = 'X' if state['count'] % 2 == 0 else 'O'
    print('PLAYER ' + state['turn'] + ' TURN')
    print_board(state)
 
    move = input('Pick a square: ')
    for key in state['board']:
        if key == move and state['board'][key] == ' ':
            state['board'][key] = state['turn']
            # print(f'this key is {key}', state['board'][key])
            state['count'] += 1
            # print(state['count'])  

title()
init_game()
while state['count'] < 9:
    if state['board']['a1'] != ' ' and state['board']['a1'] == state['board']['b1'] == state['board']['c1']:
        print_board(state)
        print('WINNER IS ' + state['board']['a1'])
        break
    elif state['board']['a2'] != ' ' and state['board']['a2'] == state['board']['b2'] == state['board']['c2']:
        print_board(state)
        print('WINNER IS ' + state['board']['a2'])
        break
    elif state['board']['a3'] != ' ' and state['board']['a3'] == state['board']['b3'] == state['board']['c3']:
        print_board(state)
        print('WINNER IS ' + state['board']['a3'])
        break
    elif state['board']['a1'] != ' ' and state['board']['a1'] == state['board']['a2'] == state['board']['a3']:
        print_board(state)
        print('WINNER IS ' + state['board']['a1'])
        break
    elif state['board']['b1'] != ' ' and state['board']['b1'] == state['board']['b2'] == state['board']['b3']:
        print_board(state)
        print('WINNER IS ' + state['board']['b1'])
        break
    elif state['board']['c1'] != ' ' and state['board']['c1'] == state['board']['c2'] == state['board']['c3']:
        print_board(state)
        print('WINNER IS ' + state['board']['c1'])
        break
    elif state['board']['a1'] != ' ' and state['board']['a1'] == state['board']['b2'] == state['board']['c3']:
        print_board(state)
        print('WINNER IS ' + state['board']['a1'])
        break
    elif state['board']['c1'] != ' ' and state['board']['c1'] == state['board']['b2'] == state['board']['a3']:
        print_board(state)
        print('WINNER IS ' + state['board']['c1'])
        break
    else:
        get_move()

if state['count'] == 9:
    print("IT'S A TIE!")
