import os
import random


def clear_screen():
    """
    Clear the console based on OS, see credits for more info
    """
    os.system('cls||clear')


class Grid():
    def __init__(self):
        self.grid_marks = [[' ' for columns in range(5)] for rows in range(5)]
        self.player = random.randint(0, 1)

    def print_grid(self):
        """
        Prints the gameboard to the console
        """

        print('     │  A  │  B  │  C  │  D  │  E  │')
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  1  │  {self.grid_marks[0][0]}  │  {self.grid_marks[0][1]}  │  {self.grid_marks[0][2]}  │  {self.grid_marks[0][3]}  │  {self.grid_marks[0][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  2  │  {self.grid_marks[1][0]}  │  {self.grid_marks[1][1]}  │  {self.grid_marks[1][2]}  │  {self.grid_marks[1][3]}  │  {self.grid_marks[1][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  3  │  {self.grid_marks[2][0]}  │  {self.grid_marks[2][1]}  │  {self.grid_marks[2][2]}  │  {self.grid_marks[2][3]}  │  {self.grid_marks[2][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  4  │  {self.grid_marks[3][0]}  │  {self.grid_marks[3][1]}  │  {self.grid_marks[3][2]}  │  {self.grid_marks[3][3]}  │  {self.grid_marks[3][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  5  │  {self.grid_marks[4][0]}  │  {self.grid_marks[4][1]}  │  {self.grid_marks[4][2]}  │  {self.grid_marks[4][3]}  │  {self.grid_marks[4][4]}  │")
        print('─────┴─────┴─────┴─────┴─────┴─────┘')
    

    def place_mark(self):
        row_text = 'Please select a row (1 to 5): '
        col_text = 'Please select a column (A to E): '
        row = input(row_text)
        # Used to see if row variable has a correct value or not
        row_set = False
        while not row_set:
            try:
                row = int(row)
            except ValueError:
                print(f'You entered {row}, which is not a number.')
                row = input(row_text)
            else:
                row_set = True
                row -= 1

        while 0 < int(row) > 4:
            print(f'You entered {row}, which is not a valid row.')
            row = input(row_text)

        col_raw = input(col_text)
        # Used to see if col_raw variable is empty or not
        col_set = False
        while not col_set:
            if len(col_raw) == 0:
                print('Empty value detected, please try again.')
                col_raw = input(col_text)
            else:
                col_set = True
                
        # Convert the letter into a number using ord(), then 97 is subtracted to
        # get the correct number as 'a' is equal to 97, 'b' is equal to 98 etc.
        col = ord(col_raw.lower()) - 97
        print(col)
        while col < 0 or col > 4:
            print(f'You entered {col_raw.upper()}, which is not a valid column.')
            col_raw = input(col_text)
            col = ord(col_raw.lower()) - 97 

        if self.grid_marks[row][col] != ' ':
            print('A mark is already in place, please select a different location.\n')
            place_mark()
        else:
            if self.player == 0:
                self.grid_marks[row][col] = 'O'
            else:
                self.grid_marks[row][col] = 'X'


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
        grid.print_grid()
        grid.place_mark()
        grid.print_grid()
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
    grid_marks[1][3] = 'X'
    grid.print_grid()
    # Reset the board mark on row 2, column D back to a space
    grid_marks[1][3] = ' '
    print("\nYou cannot overwrite another players' mark, trying to do so will result in the game asking")
    print('you to pick a different location instead. Good luck and have fun playing!\n')
    input('Press any key to clear the screen and continue.\n')
    clear_screen()
    menu('game instructions')


grid = Grid()
grid_marks = grid.grid_marks
# print(grid)
menu('main menu')