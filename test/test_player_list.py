import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

class TestPlayerList(unittest.TestCase):
    """
    Unit tests for PlayerList class.
    """
    def test_insert_first_empty(self):
        """
        Test inserting a player at the start of an empty linked list
        """
        player_list = PlayerList()
        player = Player("player-1", "John Smith")

        self.assertEqual(player_list.is_empty(), True)
        player_list.insert_first(player)

        self.assertEqual(player_list.is_empty(), False)
        self.assertEqual(player_list.first.player, player) # test if list head == player
        self.assertEqual(player_list.last.player, player) # test if list tail == player

    def test_insert_first_populated(self):
        """
        Test inserting a player at the start of a populated linked list
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")

        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)

        self.assertEqual(player_list.is_empty(), False)
        self.assertEqual(player_list.first.player, player3)
        self.assertEqual(player_list.first.next.player, player2)
        self.assertEqual(player_list.last.player, player1) # check that first player inserted is now last in list

    def test_insert_last_empty(self):
        """
        Test inserting a player at the end of an empty linked list
        """
        player_list = PlayerList()
        player = Player("player-1", "John Smith")

        self.assertEqual(player_list.is_empty(), True)
        player_list.insert_last(player)

        self.assertEqual(player_list.is_empty(), False)
        self.assertEqual(player_list.first.player, player) # test if list head == player
        self.assertEqual(player_list.last.player, player) # test if list tail == player

    def test_insert_last_populated(self):
        """
        Test inserting a player at the last position of a populated linked list
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")

        # insert first 2 nodes at start
        player_list.insert_first(player1)
        player_list.insert_first(player2)

        # insert last node at end
        player_list.insert_last(player3)

        self.assertEqual(player_list.is_empty(), False)
        self.assertEqual(player_list.first.player, player2)
        self.assertEqual(player_list.first.next.player, player1)
        self.assertEqual(player_list.last.player, player3) # check that player3 is inserted at the end of the list

    def test_find(self):
        """
        Test searching for a player by its unique id.
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")
        player4 = Player("player-4", "Jennifer Madden")

        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)

        target = player_list.find("player-2")

        self.assertIsInstance(target, PlayerNode)
        self.assertEqual(target.player, player2)

    def test_find_invalid(self):
        """
        Test searching for a non-existent player.
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")
        player4 = Player("player-4", "Jennifer Madden")

        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)

        target = player_list.find("player-5")

        self.assertEqual(target, None)

    def test_delete_first(self):
        """
        Test deleting the first node in the linked list.
        """
        # Create new linked list
        player_list = PlayerList()

        # Create player objects
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")
        player4 = Player("player-4", "Jennifer Madden")

        # Add players to linked list
        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)

        # Test players added successfully
        self.assertEqual(player_list.is_empty(), False)
        self.assertEqual(player_list.first.player, player4)

        # Delete first node in linked list
        player_list.delete_first()

        # Test the first player is deleted and (previously) second player is now first
        self.assertEqual(player_list.find("player-4"), None)
        self.assertEqual(player_list.first.player, player3)

    def test_delete_last(self):
        """
        Test deleting the last node in the linked list.
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")
        player4 = Player("player-4", "Jennifer Madden")

        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)

        self.assertEqual(player_list.is_empty(), False)
        self.assertEqual(player_list.last.player, player1)

        player_list.delete_last()

        self.assertEqual(player_list.last.player, player2)

    def test_delete_by_key(self):
        """
        Test deleting a player from the linked list by its unique id.
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")
        player4 = Player("player-4", "Jennifer Madden")

        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)

        self.assertEqual(player_list.is_empty(), False)

        deleted = player_list.delete_by_key("player-2")

        self.assertEqual(deleted.player, player2)
        self.assertEqual(player_list.find("player-2"), None)

    def test_display_forward(self):
        """
        Test displaying all nodes in the linked list from first to last.
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")
        player4 = Player("player-4", "Jennifer Madden")

        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)

        result = player_list.display()

        self.assertEqual(result, True)

    def test_display_reverse(self):
        """
        Test displaying all nodes in the linked list from last to first.
        """
        player_list = PlayerList()
        player1 = Player("player-1", "John Smith")
        player2 = Player("player-2", "Jane Doe")
        player3 = Player("player-3", "James Roberts")
        player4 = Player("player-4", "Jennifer Madden")

        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)

        result = player_list.display(forward=False)

        self.assertEqual(result, False)