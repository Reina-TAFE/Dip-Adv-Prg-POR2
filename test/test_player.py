import unittest
from app.player import Player
class TestPlayer(unittest.TestCase):
    """
    Unit tests for Player class.
    """
    def setUp(self):
        """
        Set up player object for tests.
        """
        self.player = Player("player-1", "John Smith")

    def test_uid(self):
        """
        Test that player's id has been set correctly
        """
        player_id = self.player.uid

        self.assertEqual(player_id, "player-1")

    def test_player_name(self):
        """
        Test that player's name has been set correctly
        """
        player_name = self.player.name

        self.assertEqual(player_name, "John Smith")

    def test_player_default_score(self):
        """
        Test that player's score is set to 0 by default.
        """
        score = self.player.score

        self.assertEqual(score, 0)
        self.assertIsInstance(score, int)

    def test_player_score(self):
        new_score_valid = 10
        new_score_float = 5.5
        new_score_negative = -5

        self.player.score = new_score_valid

        self.assertEqual(self.player.score, new_score_valid)

        # test setting score to non-integer value raises ValueError
        with self.assertRaises(ValueError):
            self.player.score = new_score_float

        # test that player score has not been updated
        self.assertEqual(self.player.score, new_score_valid)

        # test setting score to negative integer value raises ValueError
        with self.assertRaises(ValueError):
            self.player.score = new_score_negative

        # test that player score has not been updated
        self.assertEqual(self.player.score, new_score_valid)

    def test_player_repr(self):
        explicit_repr = self.player.__repr__()
        implicit_repr = str(self.player)

        self.assertEqual(explicit_repr, implicit_repr)
        self.assertEqual(explicit_repr, "Player(uid='player-1', name='John Smith', score=0)")

