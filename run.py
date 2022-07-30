import os

board_marks = {
    'row-1': [' ', ' ', ' ', ' ', ' '],
    'row-2': [' ', ' ', ' ', ' ', ' '],
    'row-3': [' ', ' ', ' ', ' ', ' '],
    'row-4': [' ', ' ', ' ', ' ', ' '],
    'row-5': [' ', ' ', ' ', ' ', ' ']}


def clear_screen():
    """
    Clear the console based on OS, see credits for more info
    """
    os.system('cls||clear')


def game_board(marks):
    """
    Prints the gameboard to the console
    """

    print('     │  A  │  B  │  C  │  D  │  E  │')
    print('─────┼─────┼─────┼─────┼─────┼─────┤')
    print(f"  1  │  {marks['row-1'][0]}  │  {marks['row-1'][1]}  │  {marks['row-1'][2]}  │  {marks['row-1'][3]}  │  {marks['row-1'][4]}  │")
    print('─────┼─────┼─────┼─────┼─────┼─────┤')
    print(f"  2  │  {marks['row-2'][0]}  │  {marks['row-2'][1]}  │  {marks['row-2'][2]}  │  {marks['row-2'][3]}  │  {marks['row-2'][4]}  │")
    print('─────┼─────┼─────┼─────┼─────┼─────┤')
    print(f"  3  │  {marks['row-3'][0]}  │  {marks['row-3'][1]}  │  {marks['row-3'][2]}  │  {marks['row-3'][3]}  │  {marks['row-3'][4]}  │")
    print('─────┼─────┼─────┼─────┼─────┼─────┤')
    print(f"  4  │  {marks['row-4'][0]}  │  {marks['row-4'][1]}  │  {marks['row-4'][2]}  │  {marks['row-4'][3]}  │  {marks['row-4'][4]}  │")
    print('─────┼─────┼─────┼─────┼─────┼─────┤')
    print(f"  5  │  {marks['row-5'][0]}  │  {marks['row-5'][1]}  │  {marks['row-5'][2]}  │  {marks['row-5'][3]}  │  {marks['row-5'][4]}  │")
    print('─────┴─────┴─────┴─────┴─────┴─────┘')


def menu(page):
    """
    Shows a menu that changes depending on what parameter 'page' is set to.
    When set to 'main menu', allow users to start the game or read the game 
    instructions. When set to 'game instructions', allow users to start the
    game or call this function again, setting parameter 'page' to 'main menu'.
    :param page: string
    """
    if page == 'main menu':
        print('Welcome to 5x5 Tic-Tac-Toe!\n')
        print('Would you like to start the game or read the game instructions?')
        menu_options = '1. Start the game\n2. Read game instructions\n'
        menu_input = input(menu_options)
    elif page == 'game instructions':
        print('Would you like to start the game or go back to the main menu?')
        menu_options = '1. Start the game\n2. Back to main menu\n'
        menu_input = input(menu_options)

    while menu_input != '1' and menu_input != '2':
        print(f'\nYou entered {menu_input}, which is not a valid option.\n')
        print('Please select one of the two options:')
        menu_input = input(menu_options)

    if menu_input == '1':
        clear_screen()
        print('Start game')
    elif menu_input == '2':
        if page == 'main menu':
            clear_screen()
            game_instructions()
        elif page == 'game instructions':
            clear_screen()
            menu('main menu')


def game_instructions():
    """
    Shows the game instructions, then call menu function
    """
    print('As the name implies, 5x5 Tic-Tac-Toe is a the same as the Tic-Tac-Toe we all know and love,')
    print('except that it uses a 5x5 grid instead of a 3x3 grid. To win the game, you have to get 4 marks')
    print('in a row, either horizontally, vertically or diagonally. If no one is able to get 4 marks in a')
    print('row, then the game is a draw.\n')
    print('To play the game, you first have to pick a row, then a column. For example, if you are playing')
    print('with the X marks, picking row 2 and column D would look like this:\n')
    # Set the board mark on row 2, column D to X
    board_marks['row-2'][3] = 'X'
    game_board(board_marks)
    # Reset the board mark on row 2, column D back to a space
    board_marks['row-2'][3] = ' '
    print("\nYou cannot overwrite another players' mark, trying to do so will result in the game asking")
    print('you to pick a different location instead. Good luck and have fun playing!\n')
    input('Press any key to clear the screen and continue.\n')
    clear_screen()
    menu('game instructions')


main_menu('main menu')
# game_board(board_marks)