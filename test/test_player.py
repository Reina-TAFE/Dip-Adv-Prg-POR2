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
        Test that players id has been set correctly
        """
        player_id = self.player.uid

        self.assertEqual(player_id, "player-1")

    def test_player_name(self):
        """
        Test that players name has been set correctly
        """
        player_name = self.player.name

        self.assertEqual(player_name, "John Smith")