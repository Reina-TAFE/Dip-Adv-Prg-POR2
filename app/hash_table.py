from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class PlayerHashMap:
    def __init__(self, table_size=10):
        self.size = 0
        self.__TABLE_SIZE = table_size
        self.__table = [PlayerList() for _ in range(self.__TABLE_SIZE)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.__TABLE_SIZE
        else:
            return Player.hash(key) % self.__TABLE_SIZE

    def __setitem__(self, key, value):
        index = self.get_index(key)
        player_list = self.__table[index]
        if not player_list.is_empty():
            player_node = player_list.find(key)
            if player_node is not None:
                player_node.player.name = value
                return
        player = Player(key, value)
        player_list.insert_last(player)
        return

    def get(self, player):
        pass

    def remove(self, player):
        pass

    def size(self):
        pass

    def __hash(self, key):
        return hash(key) % self.__TABLE_SIZE