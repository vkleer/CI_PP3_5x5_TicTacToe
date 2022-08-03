import unittest
from unittest.mock import patch
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


class TestPlayerRegistration(unittest.TestCase):
    """
    Tests the register_players function from player_validation.
    Verifies both valid and invalid registration input.

    """
    @patch('builtins.input')
    def test_register_players(self, mocked_input):
        mocked_input.side_effect = (
            ['Testname', '1', 'testname@test.com', '1', '1', 'Testname2', '1', 
             'testname2@test.com', '1', '1']
        )
        self.assertEqual(play_val.register_players(), None)


class TestPlayerLogIn(unittest.TestCase):
    """
    Tests the log_in function from player_validation.
    Verifies both valid and invalid registration input.
    """
    @patch('builtins.input')
    def test_login_players(self, mocked_input):
        mocked_input.side_effect = (
            ['testname@test.com', 'testname2@test.com', '1']
        )
        self.assertEqual(play_val.log_in(), None)
        play_val.delete_test_data('Testname')
        play_val.delete_test_data('Testname2')


if __name__ == '__main__':
    unittest.main()
