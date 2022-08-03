import unittest
import player_validation as play_val


class TestUsernameAndEmailValidation(unittest.TestCase):
    def test_validate_player_username(self):
        self.assertTrue(
            play_val.validate_player_username('Billy123'), True
        )

    def test_validate_player_email(self):
        self.assertTrue(
            play_val.validate_player_email('test@outlook.com'), True
        )

if __name__ == '__main__':
    unittest.main()
