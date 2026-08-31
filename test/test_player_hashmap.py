import unittest

from app.player import Player
from app.hash_table import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = PlayerHashMap(table_size=10)
        self.hashmap.add_player("player-1", "John Smith")
        self.hashmap.add_player("player-2", "Jane Doe")
        self.hashmap.add_player("player-3", "James Roberts")

    def testHashmapLen(self):
        length = self.hashmap.length()
        self.assertEqual(length, 3)
        self.assertEqual(length, self.hashmap.size)
        self.assertEqual(self.hashmap.size, 3)

    def testGetIndex(self):
        test_index = self.hashmap.get_index("player-1")
        index = Player.hash("player-1") % 10

        self.assertEqual(test_index, index)

    def testGetPlayer(self):
        player = self.hashmap.get_player("player-3")

        self.assertIsInstance(player, Player)
        self.assertEqual(player.uid, "player-3")
        self.assertEqual(player.name, "James Roberts")

    def testGetNonExistentPlayer(self):
        player = self.hashmap.get_player("player-5")

        self.assertEqual(player, None)


    def testAddPlayer(self):
        result = self.hashmap.add_player("player-4", "Jack Rivers")

        self.assertEqual(result, True)

    def testUpdatePlayer(self):
        player_id = "player-1"
        player_name = "John Rivers"
        result = self.hashmap.update_player(player_id, player_name)
        player = self.hashmap.get_player(player_id)

        self.assertEqual(result, True)
        self.assertEqual(player.uid, player_id)
        self.assertEqual(player.name, player_name)

    def testDeletePlayer(self):
        player_deleted = self.hashmap.delete_player("player-2")

        self.assertEqual(player_deleted, True)
        self.assertEqual(self.hashmap.get_player("player-2"), None)




