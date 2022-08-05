import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from run import clear_and_logo, continue_input

# Constant variables SCOPE, CREDS, SCOPED_CREDS and GSPREAD_CLIENT taken from
# the love_sandwiches project walkthrough project by Code Institute
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tictactoe_player_data')
WORKSHEET = SHEET.worksheet('player_data')


def register_players():
    """
    Gets name and email address from user input, which are added to
    the worksheet, defined in the WORKSHEET constant variable, under
    column A (player_username) and B (player_email) respectively.
    The integer 0 is always added on registration too, under
    column C (total_wins).
    """
    player_data = [[], []]

    registration_complete = False
    while not registration_complete:
        clear_and_logo()
        for i in range(2):
            if i == 1:
                confirm_input_bool = False
                while not confirm_input_bool:
                    print('Player 2, would you like to create a new account,'
                          'or do you already have one?')
                    new_account = input('1. Create new account\n2. Already '
                                        'have an account, go to log in menu\n')

                    if new_account == '1':
                        confirm_input_bool = True
                        clear_and_logo()
                    elif new_account == '2':
                        registration_complete = True
                        return
                    else:
                        clear_and_logo()
                        print(f'You entered {new_account}, please enter '
                              'either 1 to confirm or 2 to cancel.')

            print("Let's start the registration process for player "
                  f"{i + 1}.")

            username_set = False
            while not username_set:
                player_username = input('Please enter your preferred '
                                        'username: \n').capitalize()

                if validate_player_username(player_username):
                    if not registered_value(player_username):
                        clear_and_logo()

                        confirm_input_bool = False
                        while not confirm_input_bool:
                            print(f'You entered: {player_username}. Is that '
                                  'correct? All usernames are automatically '
                                  'capitalized.')
                            confirm_username = input('1. Confirm\n2. Cancel\n')

                            if confirm_username == '1':
                                clear_and_logo()
                                confirm_input_bool = True
                                username_set = True
                                print(f'Great! Nice to meet you, '
                                      f'{player_username}.')
                            elif confirm_username == '2':
                                confirm_input_bool = True
                                username_set = False
                            else:
                                clear_and_logo()
                                print('Please enter either 1 to confirm or 2 '
                                      'to cancel.')
                    else:
                        clear_and_logo()
                        print(f'The username {player_username} is already in '
                              'use. Please try a different one.')
                else:
                    print(f'You entered {player_username}.')

            # Check if player added a valid email address and if the user wants
            # to use this specific email address to register
            email_set = False
            while not email_set:
                player_email = input('Please enter your email '
                                     'address: \n').lower()

                if validate_player_email(player_email):
                    if not registered_value(player_email):
                        clear_and_logo()

                        confirm_input_bool = False
                        while not confirm_input_bool:
                            print(f'You entered: {player_email}. Is that '
                                  'correct?')
                            confirm_input = input('1. Confirm\n2. Cancel\n')
                            if confirm_input == '1':
                                confirm_input_bool = True
                                email_set = True
                            elif confirm_input == '2':
                                confirm_input_bool = True
                                email_set = False
                            else:
                                clear_and_logo()
                                print('Please enter either 1 to confirm or 2 '
                                      'to cancel.')
                    else:
                        clear_and_logo()
                        print(f'The email address {player_email} is already '
                              'in use. Please try a different one.')
                else:
                    print(f'You entered {player_email}.')

            clear_and_logo()
            player_data[i] = [player_username, player_email, 0]
            WORKSHEET.append_row(player_data[i])
            print('Registration complete, your account has been successfully '
                  f'created. Thanks {player_username}.\n')
        continue_input()
        registration_complete = True


def validate_player_username(username):
    """
    Checks if player username meets the set criteria.
    Should be between 2 to 20 characters long, using letters and digits only.
    @param name: string
    """
    try:
        if len(username) <= 2 or len(username) > 20:
            clear_and_logo()
            print('Username must be between 2 to 20 characters long.')
        elif not username.isalnum():
            clear_and_logo()
            print('Username can only contain letters or digits.')
        else:
            return True
    except TypeError:
        return False


def validate_player_email(email):
    """
    Checks if email address is valid.
    Uses external library called email-validator to do this.
    The email address must follow the format of name@example.com
    @param email: string
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        clear_and_logo()
        print(str(e))


def log_in():
    """
    Allows existing players to log in to the game with their email address,
    which is checked by looking in the worksheet, defined in the WORKSHEET
    constant variable.
    If a player accidentally landed here or wants to create a new account,
    instead of log in, they can do so as well.
    Multiple global variables are set to provide feedback to the players
    while and after playing.
    """
    global player_1_username
    global player_1_email
    global player_1_wins
    global player_2_username
    global player_2_email
    global player_2_wins

    login_complete = False
    while not login_complete:
        for i in range(2):
            clear_and_logo()
            if i == 0:
                print(f'Player {i + 1}, please enter your email address '
                      'to log in to the game.')
            else:
                print(f'Welcome back, {player_1_username}!\n')
                print(f'Player {i + 1}, please enter your email address '
                      'to log in to the game.')

            get_email = False
            while not get_email:
                player_email = input('Email address: \n')

                if validate_player_email(player_email):
                    if registered_value(player_email):
                        if i == 0:
                            player_1_email = player_email
                            get_email = True
                        elif i == 1:
                            if player_1_email != player_email:
                                player_2_email = player_email
                                get_email = True
                            else:
                                clear_and_logo()
                                print(f'Cannot be the same email as Player 1'
                                      f' {player_1_username}.')
                    else:
                        clear_and_logo()
                        print(f'{player_email} is not registered, do you '
                              'want to try different email address or '
                              'create a new account?')
                        try_again = input('1. Try different email address\n'
                                          '2. Create new account\n')
                        if try_again == '1':
                            print('Ok.')
                        elif try_again == '2':
                            register_players()
                        else:
                            clear_and_logo()
                            print(f'You entered {try_again}, please enter '
                                  'either 1 to confirm or 2 to cancel: ')

            if i == 0:
                player_1_username = (
                    WORKSHEET.row_values(WORKSHEET.find(player_email).row)[0]
                )
                player_1_wins = (
                    WORKSHEET.row_values(WORKSHEET.find(player_email).row)[2]
                )
            elif i == 1:
                player_2_username = (
                    WORKSHEET.row_values(WORKSHEET.find(player_email).row)[0]
                )
                player_2_wins = (
                    WORKSHEET.row_values(WORKSHEET.find(player_email).row)[2]
                )
                player_2_email = player_email
                login_complete = True

    clear_and_logo()
    print(f'Welcome back, {player_2_username}!\n')
    input('You are now both logged in - press any key to continue to '
          'the game.\n')


def registered_value(value):
    """
    Check if the value is registered by looking in the worksheet, defined in
    the WORKSHEET constant variable, to find a match
    @param value: string
    """
    username_list = WORKSHEET.col_values(1)
    email_list = WORKSHEET.col_values(2)

    if value in username_list or value in email_list:
        return True
    else:
        return False


def update_score(player):
    """
    Add 1 to column C (total_wins) in the worksheet, defined in the WORKSHEET 
    constant variable, to the player who won the game.
    """
    if player == player_1_username:
        global player_1_wins
        player_1_wins = int(player_1_wins) + 1
        WORKSHEET.update_cell(
            WORKSHEET.find(player_1_username).row, 3, + player_1_wins
            )
    elif player == player_2_username:
        global player_2_wins
        player_2_wins = int(player_2_wins) + 1
        WORKSHEET.update_cell(
            WORKSHEET.find(player_2_username).row, 3, + player_2_wins
        )


def delete_test_data(test_username):
    username_row = WORKSHEET.find(test_username).row

    WORKSHEET.update(f'A{username_row}', '')
    WORKSHEET.update(f'B{username_row}', '')
    WORKSHEET.update(f'C{username_row}', '')
