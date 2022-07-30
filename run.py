board_marks = {
    'row-1': [' ', ' ', ' ', ' ', ' '],
    'row-2': [' ', ' ', ' ', ' ', ' '],
    'row-3': [' ', ' ', ' ', ' ', ' '],
    'row-4': [' ', ' ', ' ', ' ', ' '],
    'row-5': [' ', ' ', ' ', ' ', ' ']}



def game_board(marks):
    """
    Prints the gameboard to the console
    """

    print('┌─────┬─────┬─────┬─────┬─────┐')
    print(f"│  {marks['row-1'][0]}  │  {marks['row-1'][1]}  │  {marks['row-1'][2]}  │  {marks['row-1'][3]}  │  {marks['row-1'][4]}  │")
    print('├─────┼─────┼─────┼─────┼─────┤')
    print(f"│  {marks['row-2'][0]}  │  {marks['row-2'][1]}  │  {marks['row-2'][2]}  │  {marks['row-2'][3]}  │  {marks['row-2'][4]}  │")
    print('├─────┼─────┼─────┼─────┼─────┤')
    print(f"│  {marks['row-3'][0]}  │  {marks['row-3'][1]}  │  {marks['row-3'][2]}  │  {marks['row-3'][3]}  │  {marks['row-3'][4]}  │")
    print('├─────┼─────┼─────┼─────┼─────┤')
    print(f"│  {marks['row-4'][0]}  │  {marks['row-4'][1]}  │  {marks['row-4'][2]}  │  {marks['row-4'][3]}  │  {marks['row-4'][4]}  │")
    print('├─────┼─────┼─────┼─────┼─────┤')
    print(f"│  {marks['row-5'][0]}  │  {marks['row-5'][1]}  │  {marks['row-5'][2]}  │  {marks['row-5'][3]}  │  {marks['row-5'][4]}  │")
    print('└─────┴─────┴─────┴─────┴─────┘')


def main_menu():
    """
    Shows the menu to users, giving them the option to start the game
    or read the game instructions
    """
    print('Welcome to Tic-Tac-Toe!\n')
    print('Would you like to start the game or read the game instructions?')
    menu_options = '1. Start the game\n2. Read game instructions\n'
    menu_input = input(menu_options)

    while menu_input != '1' and menu_input != '2':
        print(f'\nYou entered {menu_input}, which is not a valid option.\n')
        print('Please select one of the two options:')
        menu_input = input(menu_options)

    if menu_input == '1':
        print('Start game')
    elif menu_input == '2':
        print('Load game instructions')


# main_menu()
game_board(board_marks)