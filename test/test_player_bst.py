import unittest
from app.player_bst import PlayerBST, PlayerBNode, Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.tree = PlayerBST()

    def test_insert_players(self):
        john = Player("007", "John")
        michael = Player("002", "Michael")
        james = Player("004", "James")
        jane = Player("002", "Jane")
        jessica = Player("008", "Jessica")
        daphne = Player("003", "Daphne")
        mary = Player("00", "Mary-Ann")

        jane2 = Player("007", "Jane")

        self.tree.insert(james)
        self.tree.insert(john)
        self.tree.insert(mary)
        self.tree.insert(jessica)
        self.tree.insert(michael)
        self.tree.insert(daphne)
        self.tree.insert(jane)

        root_player = self.tree.root.player
        self.assertEqual(root_player, james)