import unittest
from unittest.mock import Mock, patch
import player_validation as play_val


# class TestUsernameAndEmailValidation(unittest.TestCase):
#     """
#     Tests the username and email validation functions from player_validation.
#     Verifies both valid and invalid username and email input.

#     """
#     def test_validate_player_username(self):
#         self.assertTrue(
#             play_val.validate_player_username('Billy123'), True
#         )

#     def test_validate_invalid_player_username(self):
#         self.assertEqual(
#             play_val.validate_player_username('A'), None
#         )
#         self.assertEqual(
#             play_val.validate_player_username('Amber!'), None
#         )
#         self.assertEqual(
#             play_val.validate_player_username('AlfredoTheMagnificentOne'), None
#         )

#     def test_validate_player_email(self):
#         self.assertTrue(
#             play_val.validate_player_email('test@outlook.com'), True
#         )

#     def test_validate_invalid_player_email(self):
#         self.assertEqual(
#             play_val.validate_player_email('NotAnEmailAddress'), None
#         )
#         self.assertEqual(
#             play_val.validate_player_email('test@test'), None
#         )
#         self.assertEqual(
#             play_val.validate_player_email('abc@123.cba'), None
#         )


class TestPlayerRegistrationAndLogin(unittest.TestCase):
    """
    Tests the log in and registration functions from player_validation.
    Verifies both valid and invalid registration and log in input.

    """
    @patch('builtins.input')
    def test_input(self, mocked_input):
        mocked_input.side_effect = ['bib', '1', 'bib@live.nl', '1']
        play_val.register_players()


if __name__ == '__main__':
    unittest.main()
