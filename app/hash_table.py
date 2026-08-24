from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class PlayerHashMap:
    def __init__(self, table_size=10):
        self.size = 0
        self.__TABLE_SIZE = table_size
        self.__table = {i: PlayerList() for i in range(self.__TABLE_SIZE)}

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.__TABLE_SIZE  # map hash value of player object onto table size to get index
        else:
            return Player.hash(key) % self.__TABLE_SIZE # find the hash value of the key and map onto table size to get index

    def __setitem__(self, key, value):
        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        # check for collisions
        if not hashed_player_list.is_empty():    # (PlayerList empty: no collisions | PlayerList not empty: collision)
            # if there are collisions, check if key already exists in PlayerList
            player_node = hashed_player_list.find(key)
            if player_node is not None:
                # if player exists in the PlayerList, update existing entry
                player_node.player.name = value
                return
        # if player list is empty (no collisions), or player doesn't exist in player list
        # create new player object and insert at end of player list
        player = Player(key, value)
        hashed_player_list.insert_last(player)
        self.size += 1
        return

    def __getitem__(self, key: str) -> Player | None:
        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        if not hashed_player_list.is_empty():
            player_node = hashed_player_list.find(key)
            if player_node is not None:
                return player_node.player
        return None

    def __delitem__(self, key: str):
        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        deleted_node = hashed_player_list.delete_by_key(key)
        if deleted_node is not None:
            print(f"Successfully deleted player: {deleted_node.player}")
        else:
            print(f"No player found with key: {key}")
        return

    def __len__(self):
        pass

    # def __hash(self, key):
    #     return hash(key) % self.__TABLE_SIZE