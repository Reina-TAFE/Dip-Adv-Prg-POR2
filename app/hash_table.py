from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class PlayerHashMap:
    def __init__(self, table_size=10):
        self.__size = 0
        self.__TABLE_SIZE = table_size
        self.__table = {i: PlayerList() for i in range(self.__TABLE_SIZE)}

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value != self.__size:
            self.__size = value

    def get_index(self, key: str | Player) -> int:
        """
        Hashes the key and returns the index that the hash value will map to
        in the table.

        Parameters
        ----------
        key: str | Player

        Returns
        -------
        int
        """
        if isinstance(key, Player):
            return hash(key) % self.__TABLE_SIZE  # map hash value of player object onto table size to get index
        else:
            return Player.hash(key) % self.__TABLE_SIZE # find the hash value of the key and map onto table size to get index

    def __setitem__(self, key: str, value) -> int :
        """
        Finds and updates the player whose id corresponds to the key. If player is found, updates
        player's name and returns 1.

        If no player with a corresponding id is found, creates and adds a new player with an
        id of key and name of value, and returns 0.


        Parameters
        ----------
        key
        value

        Returns
        -------

        """
        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        # check for collisions
        if not hashed_player_list.is_empty():    # (PlayerList empty: no collisions | PlayerList not empty: collision)
            # if there are collisions, attempt to update player
            if hashed_player_list.update_by_key(key, value): # Successfully updated: True | Player not found: False
                return 1
        # if player list is empty (no collisions), or player doesn't exist in player list
        # create new player object and insert at end of player list
        player = Player(key, value)
        hashed_player_list.insert_last(player)
        self.size += 1
        return 0

    def __getitem__(self, key: str) -> Player | None:
        """
        Finds and returns the player whose id corresponds to the key.
        If no player has a corresponding id, returns None.

        Parameters
        ----------
        key: str

        Returns
        -------
        Player | None
        """
        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        if not hashed_player_list.is_empty():
            player_node = hashed_player_list.find(key)
            if player_node is not None:
                return player_node.player
        return None

    def __delitem__(self, key: str) -> int:
        """
        Finds and deletes the player whose id corresponds to the key from the table.
        If no player has a corresponding id, returns None.

        Parameters
        ----------
        key

        Returns
        -------
        int
        """
        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        deleted_node = hashed_player_list.delete_by_key(key)
        if deleted_node is not None:
            print(f"Successfully deleted player: {deleted_node.player}")
            self.size -= 1
            return 1
        else:
            print(f"No player found with ID: {key}")
            return 0

    def __len__(self):
        """
        Returns the number of players stored in the hash table
        Returns
        -------

        """
        size = 0
        for player_list in self.__table.values():
            size += len(player_list)
        return size

    # def __hash(self, key):
    #     return hash(key) % self.__TABLE_SIZE