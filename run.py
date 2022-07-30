board_marks = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']


def game_board(marks):
    """
    Prints the gameboard to the console
    """

    print('┌─────┬─────┬─────┐')
    print(f'│  {marks[0]}  │  {marks[1]}  │  {marks[2]}  │')
    print('├─────┼─────┼─────┤')
    print(f'│  {marks[3]}  │  {marks[4]}  │  {marks[5]}  │')
    print('├─────┼─────┼─────┤')
    print(f'│  {marks[6]}  │  {marks[7]}  │  {marks[8]}  │')
    print('└─────┴─────┴─────┘')


def game_menu():
    """
    Shows the menu to users, allowing them to start the game
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

game_menu()
# game_board(board_marks)