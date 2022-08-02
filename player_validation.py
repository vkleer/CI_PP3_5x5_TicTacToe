import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError

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


def player_registration():
    """
    Gets name and email address from user input, which is added to the
    player 1 and player 2 worksheets
    """
    player_data = [[],[]]

    registration_complete = False
    while not registration_complete:
        for i in range(2):
            print(f"Let's start the registration proces for player {i + 1}.")
            player_name = input('Please enter your name: ')
            print(f'Great! Nice to meet you, {player_name}.')

            # Check if player added a valid email address and if the user wants
            # to use this specific email address to register
            email_set = False
            while not email_set:
                player_email = input('Please enter your email address: ')

                email_validation = False
                while not email_validation:
                    print('Email address is invalid, please try again.')
                    player_email = input('Please enter your email address: ')
                    email_validation = validate_player_email(player_email)
                    print(email_validation)
                    
                print(f'You entered: {player_email}. Is that correct?')
                confirm_input = input('1. Confirm\n2. Cancel\n')
                if confirm_input == '1':
                    email_set = True
                elif confirm_input == '2':
                    email_set = False
                else:
                    print(f'You entered {confirm_input}, please enter either 1 to'
                        'confirm or 2 to cancel: ')

            print(f'Registration complete, thanks {player_name}.')
            player_data[i] = [player_name, player_email, 0, 0]
            print(player_data)
        registration_complete = True
    # Append both lists in player_data variable to WORKSHEET
    WORKSHEET.append_row(player_data[0])
    WORKSHEET.append_row(player_data[1])


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


player_registration()