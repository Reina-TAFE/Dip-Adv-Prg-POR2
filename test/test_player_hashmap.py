import unittest

from app.player import Player
from app.hash_table import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = PlayerHashMap(table_size=10)
        self.hashmap.__setitem__("player-1", "John Smith")
        self.hashmap.__setitem__("player-2", "Jane Doe")
        self.hashmap.__setitem__("player-3", "James Roberts")

    def testHashmapLen(self):
        length = self.hashmap.__len__()
        self.assertEqual(length, 3)
        self.assertEqual(length, self.hashmap.size)
        self.assertEqual(self.hashmap.size, 3)

    def testGetIndex(self):
        test_index = self.hashmap.get_index("player-1")
        index = Player.hash("player-1") % 10

        self.assertEqual(test_index, index)

    def testGetPlayer(self):
        player = self.hashmap.__getitem__("player-3")

        self.assertIsInstance(player, Player)
        self.assertEqual(player.uid, "player-3")
        self.assertEqual(player.name, "James Roberts")

    def testGetNonExistentPlayer(self):
        player = self.hashmap.__getitem__("player-5")

        self.assertEqual(player, None)


    def testAddPlayer(self):
        player_added = self.hashmap.__setitem__("player-4", "Jack Rivers")

        self.assertEqual(player_added, 0)

    def testUpdatePlayer(self):
        player_id = "player-1"
        player_name = "John Rivers"
        player_updated = self.hashmap.__setitem__(player_id, player_name)
        player = self.hashmap.__getitem__(player_id)

        self.assertEqual(player_updated, 1)
        self.assertEqual(player.uid, player_id)
        self.assertEqual(player.name, player_name)

    def testDeletePlayer(self):
        player_deleted = self.hashmap.__delitem__("player-2")

        self.assertEqual(player_deleted, 1)
        self.assertEqual(self.hashmap.__getitem__("player-2"), None)




