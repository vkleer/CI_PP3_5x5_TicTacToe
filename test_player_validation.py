import unittest
import player_validation as play_val


class TestUsernameAndEmailValidation(unittest.TestCase):
    """
    Tests the username and email validation functions from player_validation.
    Verifies both valid and invalid username and email input.

    """
    def test_validate_player_username(self):
        self.assertTrue(
            play_val.validate_player_username('Billy123'), True
        )

    def test_validate_invalid_player_username(self):
        self.assertEqual(
            play_val.validate_player_username('A'), None
        )
        self.assertEqual(
            play_val.validate_player_username('Amber!'), None
        )
        self.assertEqual(
            play_val.validate_player_username('AlfredoTheMagnificentOne'), None
        )

    def test_validate_player_email(self):
        self.assertTrue(
            play_val.validate_player_email('test@outlook.com'), True
        )

    def test_validate_invalid_player_email(self):
        self.assertEqual(
            play_val.validate_player_email('NotAnEmailAddress'), None
        )
        self.assertEqual(
            play_val.validate_player_email('test@test'), None
        )
        self.assertEqual(
            play_val.validate_player_email('abc@123.cba'), None
        )


if __name__ == '__main__':
    unittest.main()
