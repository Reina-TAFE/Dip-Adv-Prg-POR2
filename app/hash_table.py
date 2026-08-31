from app.player_list import PlayerList
from app.player import Player



class PlayerHashMap:
    def __init__(self, table_size=10):
        self.__size = 0
        self.__TABLE_SIZE = table_size
        self.__table = {i: PlayerList() for i in range(self.__TABLE_SIZE)}

    @property
    def size(self):
        """
        Size of the hash table tracked by adding/deleting players.
        """
        return self.__size

    # User should not be able to set size manually
    #
    # @size.setter
    # def size(self, value):
    #     if value != self.__size:
    #         self.__size = value

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

    def add_player(self, key: str, value: str):
        """
        Updates the player in the hash table. Returns True if successfully updated,
        else returns False.

        Parameters
        ----------
        key : str
        value : str

        Returns
        -------
        True | False
        """
        return True if self.__setitem__(key, value) is True else False

    def update_player(self, key: str, value: str):
        """
        Updates the player in the hash table. Returns True if successfully updated,
        else raises a KeyError.

        Parameters
        ----------
        key : str
        value : str

        Returns
        -------
        True
        """
        if self.__setitem__(key, value, update_only=True) is True:
            return True
        else:
            raise KeyError

    def __setitem__(self, key: str, value: str, update_only=False) -> True | False :
        """
        Finds and updates the player whose id corresponds to the key.
        If player is found, updates player's name and returns True.
        If no player is found and:

        -update_only is True:
            returns False

        -update_only is False:
            If no player with a corresponding id is found, creates and adds a new player with an
            id of key and name of value, and returns True.


        Parameters
        ----------
        key : str
        value : str
        update_only : bool

        Returns
        -------
        True | False
        """
        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        # check for collisions
        if not hashed_player_list.is_empty():    # (PlayerList empty: no collisions | PlayerList not empty: collision)
            # if there are collisions, attempt to update player
            if hashed_player_list.update_by_key(key, value): # Successfully updated: True | Player not found: False
                return True
        # if player list is empty (no collisions), or player doesn't exist in player list
        # if function is not in update-only mode, add as new player
        if update_only is False:
            # create new player object and insert at end of player list
            hashed_player_list.update_by_key(key, value)
            player = Player(key, value)
            hashed_player_list.insert_last(player)
            self.__size += 1
            return True
        return False

    def get_player(self, key: str | Player) -> Player | None:
        """
        Finds and returns a player from the hash table by its id.

        Parameters
        ----------
        key: str

        Returns
        -------
        Player | None
        """
        return self.__getitem__(key)

    def __getitem__(self, key: str | Player) -> Player | None:
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

    def delete_player(self, key: str | Player) -> True | False:
        """
        Deletes the player from the hash table by its id.

        Parameters
        ----------
        key : str | Player

        Returns
        -------
        True | False
        """
        return True if self.__delitem__(key) is True else False

    def __delitem__(self, key: str | Player) -> True | False:
        """
        Finds and deletes the player whose id corresponds to the key from the table.
        If no player has a corresponding id, returns None.

        Parameters
        ----------
        key

        Returns
        -------
        True | False
        """

        index = self.get_index(key)                 # find hashtable index for key
        hashed_player_list = self.__table[index]  # Get PlayerList object at hashtable index
        deleted_node = hashed_player_list.delete_by_key(key)
        if deleted_node is not None:
            print(f"Successfully deleted player: {deleted_node.player}")
            self.__size -= 1
            return True
        else:
            print(f"No player found with ID: {key}")
            return False

    def length(self):
        """
        Calculates the length of the hash table.
        """
        return self.__len__()

    def __len__(self):
        """
        Calculates the combined length of PlayerLists stored in the hash table.
        Returns
        -------

        """
        size = 0
        for player_list in self.__table.values():
            size += len(player_list)
        return size
