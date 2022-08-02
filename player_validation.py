import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from run import clear_screen

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
    Gets name and email address from user input, which is added to the
    player 1 and player 2 worksheets
    """
    player_data = [[], []]

    registration_complete = False
    while not registration_complete:
        clear_screen()
        for i in range(2):
            if i == 1:
                print('Would player 2 like to register too, or do you already'
                      'have an account?')
                new_account = input('1. Register new account\n2. Already have '
                                    'an account, go to login\n')
                if new_account == '1':
                    print('Alright.')
                elif new_account == '2':
                    break
                else:
                    print(f'You entered {new_account}, please enter either 1 '
                          'to confirm or 2 to cancel: ')

            print(f"Let's start the registration proces for player {i + 1}.")

            name_set = False
            while not name_set:
                player_name = input('Please enter your name: ')

                if validate_player_name(player_name):
                    print(f'You entered: {player_name}. Is that correct?')
                    confirm_name = input('1. Confirm\n2. Cancel\n')
                    if confirm_name == '1':
                        name_set = True
                        print(f'Great! Nice to meet you, {player_name}.')
                    elif confirm_name == '2':
                        name_set = False
                    else:
                        print(f'You entered {confirm_name}, please enter '
                              'either 1 to confirm or 2 to cancel: ')
                else:
                    print('Sorry, please try again')

            # Check if player added a valid email address and if the user wants
            # to use this specific email address to register
            email_set = False
            while not email_set:
                player_email = input('Please enter your email address: ')

                if validate_player_email(player_email):
                    print(f'You entered: {player_email}. Is that correct?')
                    confirm_input = input('1. Confirm\n2. Cancel\n')
                    if confirm_input == '1':
                        email_set = True
                    elif confirm_input == '2':
                        email_set = False
                    else:
                        print(f'You entered {confirm_input}, please enter '
                              'either 1 to confirm or 2 to cancel: ')
                else:
                    print('')

            print(f'Registration complete, thanks {player_name}.')
            player_data[i] = [player_name, player_email, 0, 0]
            print(player_data)
        registration_complete = True
    # Append both lists in player_data variable to WORKSHEET
    WORKSHEET.append_row(player_data[0])
    WORKSHEET.append_row(player_data[1])


def validate_player_name(name):
    """
    Checks if player name meets the set criteria.
    Should be between 2 to 20 characters long, using letters only.
    @param name: string
    """
    try:
        if len(name) <= 2 or len(name) > 20:
            print('Name must be between 2 to 20 characters long.')
        elif not name.isalpha():
            print('Name can only contain letters.')
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
        print(str(e))


def log_in():
    player_1_name = ''
    player_2_name = ''
    player_1_email = ''
    player_2_email = ''
    login_complete = False
    while not login_complete:
        clear_screen()
        for i in range(2):
            print(f'Welcome back! Player {i}, please enter your email address'
                  'to log in to the game.')

            get_email = False
            while not get_email:
                player_email = input('Please enter your email address: ')

                if validate_player_email(player_email):
                    if registered_email(player_email):
                        if player_1_email != player_email:
                            get_email = True
                        else:
                            print(f'Cannot be the same email as Player 1'
                                  f'{player_1_name}.')
                    else:
                        print('Email not registered.')

            if i == 0:
                player_1_name = (
                    WORKSHEET.row_values(WORKSHEET.find(player_email).row)[0]
                )
                player_1_email = player_email
                print(f'Welcome back, {player_1_name.capitalize()}!')
            elif i == 1:
                player_2_name = (
                    WORKSHEET.row_values(WORKSHEET.find(player_email).row)[0]
                )
                print(f'Welcome back, {player_2_name.capitalize()}!')
                player_2_email = player_email
                login_complete = True


def registered_email(email):
    """
    Check if the email address is registered by looking
    in WORKSHEET to find a match
    @param email: string
    """
    email_list = WORKSHEET.col_values(2)

    if email in email_list:
        return True
    else:
        return False


log_in()
