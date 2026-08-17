from app.player_node import PlayerNode


class PlayerList:
    """
    A linked list of PlayerNodes.
    """
    def __init__(self):
        """
        Constructor for PlayerList
        """
        self.__first = None # points to the head of the list
        self.__last = None # points to the tail of the list

    @property
    def first(self):
        """
        Returns the first PlayerNode in the linked list.
        Returns
        -------
        PlayerNode | None
        """
        return self.__first

    @property
    def last(self):
        """
        Returns the last PlayerNode in the linked list.
        Returns
        -------
        PlayerNode | None
        """
        return self.__last

    def is_empty(self):
        """
        Checks if linked list is empty.
        Returns
        -------
        bool
        """
        return self.__first is None

    def find(self, key: str):
        """
        Sequentially searches for a PlayerNode by its key.
        Returns PlayerNode if found, or None if not fount.
        Parameters
        ----------
        key : str

        Returns
        -------
        PlayerNode | None
        """
        current = self.first
        while current.next is not None:
            if current.key == key:
                return current
            else:
                current = current.next
        return None

    def insert_first(self, player):
        """
        Inserts a new PlayerNode at the beginning of the linked list.
        Parameters
        ----------
        player

        Returns
        -------

        """
        new_player_node = PlayerNode(player)
        if not self.is_empty():
            new_player_node.next = self.__first
            self.__first.previous = new_player_node
        else:
            self.__last = new_player_node
        self.__first = new_player_node

    def insert_last(self, player):
        """
        Inserts a new PlayerNode at the end of the linked list.
        Parameters
        ----------
        player

        Returns
        -------

        """
        new_player_node = PlayerNode(player)
        # test if list is populated
        if not self.is_empty():
            # if list is populated
            new_player_node.previous = self.__last # set 'previous' property of new node to current __last node
            self.__last.next = new_player_node # update 'next' property of current __last node to new node
        else:
            # if list is empty, set __first to new player node
            self.__first = new_player_node
        # set __last to new node
        self.__last = new_player_node

    def delete_first(self):
        """
        Deletes the PlayerNode at the beginning of the linked list.
        Returns
        -------
        PlayerNode
        """
        popped_node = self.__first
        if self.__first is not None:
            self.__first.next.previous = None
            self.__first = self.__first.next
        return popped_node

    def delete_last(self):
        """
        Deletes the PlayerNode at the end of the linked list.
        Returns
        -------
        PlayerNode
        """
        popped_node = self.__last
        if self.__last is not None:
            self.__last.previous.next = None
            self.__last = self.__last.previous
        return popped_node

    def delete_by_key(self, key: str):
        """
        Deletes an item from the linked list according to its key.
        :param key:
        :return PlayerNode | None:
        """
        current = self.find(key)
        if current is not None:
            if current == self.first:
                self.__first = current.next
            else:
                current.previous.next = current.next
            if current == self.__last:
                self.__last = current.previous
            else:
                current.next.previous = current.previous
            return current
        return None

    def display(self, forward=True):
        """
        Prints all items in linked list. Prints from first to last by default (forward=True), or
        from last to first if 'forward' = False.
        Parameters
        ----------
        forward : bool

        Returns
        -------
        bool
        """
        # check which order to display nodes (forward/reverse)
        if forward:
            current = self.first  # start from first node
        else:
            current = self.last  # start from last node
        while current is not None: # loop until
            print(str(current))  # print current node
            current = current.next if forward else current.previous
        return True if forward else False



