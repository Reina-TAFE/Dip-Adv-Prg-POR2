import unittest
from re import search

from app.player_bst import PlayerBST, PlayerBNode, Player

class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.tree = PlayerBST()

    def test_insert_players(self):
        """
        Tests players are inserted into the PlayerBST correctly
        """
        john = Player("007", "John")
        michael = Player("002", "Michael")
        james = Player("004", "James")
        jane = Player("002", "Jane")
        jessica = Player("008", "Jessica")
        daphne = Player("003", "Daphne")
        mary = Player("00", "Mary-Ann")


        self.tree.insert(jessica)
        self.tree.insert(james)
        self.tree.insert(mary)
        self.tree.insert(daphne)
        self.tree.insert(michael)
        self.tree.insert(jane)
        self.tree.insert(john)

        root = self.tree.root                                     # PlayerBNode(Jessica)
        root_left = root.subtree_left                             # PlayerBNode(James)
        root_left_left = root_left.subtree_left                   # PlayerBNode(Daphne)
        root_left_right = root_left.subtree_right                 # PlayerBNode(Daphne)
        root_right = root.subtree_right                           # PlayerBNode(Mary)
        root_right_left = root_right.subtree_left                 # PlayerBNode(John)
        root_right_right = root_right.subtree_right               # PlayerBNode(Michael)

        root_player = root.player                                 # Jessica
        root_left_player = root_left.player                       # James
        root_right_player = root_right.player                     # Mary
        root_left_left_player = root_left_left.player             # Daphne
        root_left_right_player = root_left_right.player           # Jane
        root_right_left_player = root_right_left.player           # John
        root_right_right_player = root_right_right.player         # Michael


        self.assertEqual(root_player, jessica)
        self.assertEqual(root_left_player, james)
        self.assertEqual(root_right_player, mary)
        self.assertEqual(root_left_left_player, daphne)
        self.assertEqual(root_left_right_player, jane)
        self.assertEqual(root_right_left_player, john)
        self.assertEqual(root_right_right_player, michael)

    def test_search_player(self):
        john = Player("007", "John")
        michael = Player("002", "Michael")
        james = Player("004", "James")
        jane = Player("002", "Jane")
        jessica = Player("008", "Jessica")
        daphne = Player("003", "Daphne")
        mary = Player("00", "Mary-Ann")

        self.tree.insert(jessica)
        self.tree.insert(james)
        self.tree.insert(mary)
        self.tree.insert(daphne)
        self.tree.insert(michael)
        self.tree.insert(jane)
        self.tree.insert(john)

        searched = self.tree.search("Michael")   # should return PlayerBNode(micheal)
        failed_search = self.tree.search("Fred") # should return None

        self.assertEqual(searched.player, michael)
        self.assertEqual(failed_search, None)

    def test_get_subtrees(self):
        john = Player("007", "John")
        michael = Player("002", "Michael")
        james = Player("004", "James")
        jane = Player("002", "Jane")
        jessica = Player("008", "Jessica")
        daphne = Player("003", "Daphne")
        mary = Player("00", "Mary")

        self.tree.insert(james)
        self.tree.insert(john)
        self.tree.insert(jessica)
        self.tree.insert(mary)
        self.tree.insert(michael)
        self.tree.insert(daphne)
        self.tree.insert(jane)


        subtrees = self.tree.get_balanced_bst()

        sorted_subtrees = sorted(subtrees, key=lambda node: node.player.name)

        for item in sorted_subtrees:
            print(item)