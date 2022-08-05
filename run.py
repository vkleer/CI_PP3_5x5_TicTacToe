import os
import sys
import random
import player_validation as play_val


def clear_screen():
    """
    Clear the console based on OS, see credits for more info
    """
    os.system('cls||clear')


def game_logo():
    """
    Prints out the name of the game in stylish ASCII logo format, see credits
    for more info
    """
    print(' ____           ____    _____ _         _____             _____ ')
    print('| ___|  __  __ | ___|  |_   _(_) ___   |_   _|_ _  ___   |_   _|'
          '__   ___')
    print('|___ \\  \\ \/ / |___ \    | | | |/ __|____| |/ _` |/ __|____| |'
          '/ _ \ / _ \\')
    print(' ___) |  >  <   ___) |   | | | | (_|_____| | (_| | (_|_____| | ('
          '_) |  __/')
    print('|____/  /_/\_\ |____/    |_| |_|\___|    |_|\__,_|\___|    |_|\_'
          '__/ \___|')
    print('')
    print('                         A 2 player strategy game')
    print('')


def clear_and_logo():
    """
    Calls the clear_screen and game_logo functions
    """
    clear_screen()
    game_logo()


def log_out():
    """
    Calls the clear_and_logo function and takes the players to the
    'log in' menu
    """
    clear_and_logo()
    menu('log in')


def quit_game():
    """
    Calls the clear_and_logo function, thanks the players for playing
    the game and quits the program
    """
    clear_and_logo()
    print('Thanks for playing - we hope to see you again soon!')
    sys.exit()


def continue_input():
    """
    Pauses the current interaction until any key has been entered and 
    the enter key has been pressed
    """
    input('Press any key to continue.\n')


class Grid():
    def __init__(self):
        # Create a list of lists containing all possible mark locations on the
        # grid
        self.grid_marks = [[' ' for columns in range(5)] for rows in range(5)]
        # Pick a random player to start the game
        self.player = random.randint(0, 1)

    def print_grid(self):
        """
        Prints the grid to the console
        """
        print('     │  A  │  B  │  C  │  D  │  E  │')
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        for i in range(5):
            print(f"  {i + 1}"
                  f"  │  {self.grid_marks[i][0]}  │  {self.grid_marks[i][1]}"
                  f"  │  {self.grid_marks[i][2]}  │  {self.grid_marks[i][3]}"
                  f"  │  {self.grid_marks[i][4]}  │")
            if i != 4:
                print('─────┼─────┼─────┼─────┼─────┼─────┤')
            else:
                print('─────┴─────┴─────┴─────┴─────┴─────┘')

    def change_player(self) -> int:
        """
        Changes the self.player value from 0 to 1 or vice versa
        """
        # Variable is set to 1 minus the self.player value. This means that if
        # the self.player value is equal to 0, nothing will be subtracted,
        # turning the self.player value into 1. If the self.player value is
        # equal to 1, Then 1 will be subtracted from 1, turning the self.player
        # value into 0.
        self.player = 1 - self.player

    def check_for_win(self):
        """
        Contains 4 functions that check if any player has 4 consecutive
        horizontal,vertical or diagonal marks to win the game or if the
        grid is full and the game is a tie
        """
        result = self.grid_marks
        # Rotates the list of lists result by 90 degrees, see credits
        # for more info
        result_flip = list(zip(*reversed(result)))

        def player_won() -> bool:
            """
            Checks the self.player value and prints out which player has
            won, returning True in either case
            """
            if self.player == 0:
                print(f'{play_val.player_1_username} wins!')
                play_val.update_score(play_val.player_1_username)
                print(f'You now have a total of '
                      f'{play_val.player_1_wins} wins.\n')
            else:
                print(f'{play_val.player_2_username} wins!')
                play_val.update_score(play_val.player_2_username)
                print(f'You now have a total of {play_val.player_2_wins}'
                      ' wins.\n')

            continue_input()
            return True

        def check_rows() -> bool:
            """
            Checks all rows to see if 4 consecutive marks have been placed
            in a row. If so, call the player_won function and if not, return
            False
            """
            for row in result:
                if (
                    row[0] == row[1] == row[2] == row[3] != ' ' or
                    row[1] == row[2] == row[3] == row[4] != ' '
                ):
                    return player_won()
            return False

        def check_columns() -> bool:
            """
            Checks all columns to see if 4 consecutive marks have been placed
            in a column. If so, call the player_won function and if not, return
            False
            """
            for col in result_flip:
                if (
                    col[0] == col[1] == col[2] == col[3] != ' ' or
                    col[1] == col[2] == col[3] == col[4] != ' '
                ):
                    return player_won()
            return False

        def check_diagonals() -> bool:
            """
            Checks all possible diagonals in the grid to see if 4 consecutive
            marks have been placed in a diagonal. If so, call the player_won
            function and if not, return False
            """
            # Check the diagonals from row 1, column A to row 5, column E and
            # row 5 column A to row 1, column E
            for i in range(2):
                if (
                    result[i][i] == result[i + 1][i + 1] ==
                    result[i + 2][i + 2] == result[i + 3][i + 3] != ' ' or
                    result_flip[i][i] == result_flip[i + 1][i + 1] ==
                    result_flip[i + 2][i + 2] ==
                    result_flip[i + 3][i + 3] != ' '
                ):
                    return player_won()
            # Check the diagonals from row 2, column A to row 5, column E,
            # row 1, column B to row 4, column E, row 1, column D to row 4,
            # column A and row 2, column E to row 5, column A
            if (
                result[0][1] == result[1][2] == result[2][3] ==
                result[3][4] != ' ' or
                result[1][0] == result[2][1] == result[3][2] ==
                result[4][3] != ' ' or
                result_flip[0][1] == result_flip[1][2] == result_flip[2][3] ==
                result_flip[3][4] != ' ' or
                result_flip[1][0] == result_flip[2][1] == result_flip[3][2] ==
                result_flip[4][3] != ' '
            ):
                return player_won()
            return False

        def full_grid() -> bool:
            """
            If the grid is full, print out a message to announce the game is a
            tie and returns True
            """
            total_marks = 0
            marks_used = 0
            # Check how many items there are in each row
            for row in self.grid_marks:
                for mark in row:
                    total_marks += 1
                    # If mark has been placed on the grid, increase marks_used
                    # by 1
                    if mark != ' ':
                        marks_used += 1

            if marks_used == total_marks:
                print("Grid is full, but no one won. It's a tie!")
                continue_input()
                return True

        # If a player has won the game, return True
        if check_rows() or check_columns() or check_diagonals() or full_grid():
            return True
        # If the game is not a tie and no player has won the game yet, return
        # False and keep the game running
        return False

    def place_mark(self):
        """
        Places an 'X' or 'O' mark on the grid, depending on who's turn it is.
        Validates players' input to avoid overriding another players' mark or
        entering invalid rows/columns.
        """
        if self.player == 1:
            row_text = (
                f"It's your turn, {play_val.player_1_username}.\n"
                '\nPlease select a row (1 to 5): \n'
            )
        else:
            row_text = (
                f"It's your turn, {play_val.player_2_username}.\n"
                '\nPlease select a row (1 to 5): \n'
            )

        row = input(row_text)
        # Check if row variable has a correct value or not
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

        col_text = 'Please select a column (A to E): \n'
        col_raw = input(col_text)
        # Used to see if col_raw variable is empty or not
        col_set = False
        while not col_set:
            if col_raw != '':
                try:
                    # Convert the letter into a number using ord(), then 97
                    # is subtracted to get the correct number as 'a' is 
                    # equal to 97, 'b' is equal to 98 etc.
                    col = ord(col_raw.lower()) - 97
                except TypeError:
                    print(f'You entered {col_raw}, which is not a letter.')
                    col_raw = input(col_text)
                else:
                    if col < 0 or col > 4:
                        print(f'You entered {col_raw.upper()}, which '
                              'is not a valid column.')
                        col_set = False
                        col_raw = input(col_text)
                    else:
                        col_set = True
            else:
                print(f'You entered {col_raw}, which is not a letter.')
                col_raw = input(col_text)

        if self.grid_marks[row][col] != ' ':
            print('A mark is already in place, please select a different'
                  ' location.\n')
            self.place_mark()
        else:
            # If the self.player value is equal to 0, place an 'O' mark.
            # Else, place an 'X' mark
            if self.player == 0:
                self.grid_marks[row][col] = 'O'
                self.change_player()
            else:
                self.grid_marks[row][col] = 'X'
                self.change_player()


def menu(page) -> str:
    """
    Shows a menu that changes depending on what parameter 'page' is set to.
    When set to 'log in', allow users to log in to their account, create a
    new one or log out.
    When set to 'main', allow users to start the game, read the game
    instructions, view their win count or log out.
    When set to 'play again', allow users to play another game, view their 
    wint count, log out or quit the game.
    @param page: string
    """
    clear_screen()
    if page == 'log in':
        game_logo()
        print(
            'Welcome to 5x5 Tic-Tac-Toe! Please select one of the three '
            'options:'
        )
        menu_options = '1. Log in\n2. Create new account\n3. Quit game\n'
        menu_input = input(menu_options)
    elif page == 'main':
        game_logo()
        print('Please select one of the four options:')
        menu_options = (
            '1. Start the game\n2. Game instructions\n3. View win count\n'
            '4. Log out\n'
        )
        menu_input = input(menu_options)
    elif page == 'play again':
        game_logo()
        print('Please select one of the four options:')
        menu_options = (
            '1. Play again\n2. Main menu\n3. Log out\n4. Quit game\n'
        )
        menu_input = input(menu_options)

    # The 'log in' menu only has three options, so the user will stay in
    # the while loop until one of the three options has been selected
    if page == 'log in':
        while (
            menu_input != '1' and menu_input != '2' and menu_input != '3'
        ):
            clear_and_logo()
            print(f'\nYou entered {menu_input}, which is not a valid '
                  'option.\n')
            print('Please select one of the three options:')
            menu_input = input(menu_options)
    # The 'main' and 'play again' menus both have four options, so the
    # user will stay in  the while loop until one of the four options has
    # been selected
    else:
        while (
            menu_input != '1' and menu_input != '2' and
            menu_input != '3' and menu_input != '4'
        ):
            clear_and_logo()
            print(f'\nYou entered {menu_input}, which is not a valid '
                  'option.\n')
            print('Please select one of the four options:')
            menu_input = input(menu_options)

    if menu_input == '1':
        if page != 'log in':
            clear_screen()
            # Create the game grid using Grid class to access its attributes
            # and methods
            grid = Grid()
            grid.print_grid()

            # Keep running the game until game_over is equal to True
            game_over = False
            while not game_over:
                # If the check_for_win method returns true, break out of while
                # loop to stop the game
                game_over = grid.check_for_win()
                if game_over:
                    menu('play again')
                grid.place_mark()
                clear_screen()
                grid.print_grid()
        else:
            clear_screen()
            play_val.log_in()
            menu('main')
    elif menu_input == '2':
        if page == 'main':
            clear_and_logo()
            game_instructions()
        elif page == 'log in':
            clear_screen()
            play_val.register_players()
            menu('log in')
        elif page == 'play again':
            clear_and_logo()
            menu('main')
    elif menu_input == '3':
        if page == 'log in':
            quit_game()
        if page == 'main':
            clear_and_logo()
            print(f'{play_val.player_1_username} has a total of '
                  f'{play_val.player_1_wins} wins.\n')
            print(f'{play_val.player_2_username} has a total of '
                  f'{play_val.player_2_wins} wins.\n')
            continue_input()
            menu('main')
        if page == 'play again':
            log_out()
    elif menu_input == '4':
        if page == 'main':
            log_out()
        elif page == 'play again':
            quit_game()         


def game_instructions():
    """
    Shows the game instructions, then call menu function
    """
    print('As the name implies, 5x5 Tic-Tac-Toe is a the same as the '
          'Tic-Tac-Toe we all know and love,')
    print('except that it uses a 5x5 grid instead of a 3x3 grid. To win '
          'the game, you have to get 4 marks')
    print('in a row, either horizontally, vertically or diagonally. If '
          'no one is able to get 4 marks in a')
    print('row, then the game is a draw.\n')
    continue_input()
    # Clear screen in between instructions
    clear_and_logo()
    print('To play the game, you first have to pick a row, then a column.'
          ' For example, if you are playing')
    print('with the X marks, picking row 2 and column D would look like '
          'this:\n')
    # Create a game grid using Grid class to access its attributes and
    # methods, used to show how the game works
    grid = Grid()
    grid_marks = grid.grid_marks
    # Set the board mark on row 2, column D to X
    grid_marks[1][3] = 'X'
    grid.print_grid()
    # Reset the board mark on row 2, column D back to a space
    grid_marks[1][3] = ' '
    continue_input()
    # Clear screen in between instructions
    clear_and_logo()
    print("You cannot overwrite another players' mark, trying to do so "
          "will result in the game asking you to pick a different "
          'location instead. Good luck and have fun playing!\n')
    continue_input()
    del grid
    clear_screen()
    menu('main')


def main():
    """
    Runs the required function to start the program
    """
    menu('log in')


if __name__ == '__main__':
    main()
