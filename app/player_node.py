from app.player import Player
class PlayerNode:
    """
    A node in a linked list containing a Player, as
    well as a link to the previous, and next nodes in the list
    """
    def __init__(self, player: Player):
        """
        Constructor for a new PlayerNode.
        Parameters
        ----------
        player: Player
        """
        self.__player = player      # Player object
        self.__next = None          # Reference to the next node in the list
        self.__previous = None      # Reference to the previous node in the list

    # Getter for PlayerNode.__player
    @property
    def player(self):
        """
        Returns the Player object contained at this node.
        Returns
        -------
        player: Player
        """
        return self.__player

    # Getter for PlayerNode.__next
    @property
    def next(self):
        """
        Returns the next node in the linked list.
        Returns
        -------
        next: PlayerNode
        """
        return self.__next

    # Setter for PlayerNode.__next
    @next.setter
    def next(self, node):
        """
        Sets the next node in the linked list.
        Parameters
        -------
        node: PlayerNode
        """
        self.__next = node

    # Getter for PlayerNode.__previous
    @property
    def previous(self):
        """
        Returns the previous node in the linked list.
        Returns
        -------
        previous: PlayerNode
        """
        return self.__previous

    # Setter for PlayerNode.__previous
    @previous.setter
    def previous(self, node):
        """
        Sets the previous node in the linked list.
        Parameters
        -------
        node: PlayerNode
        """
        self.__previous = node

    @property
    def key(self):
        """
        Returns the unique ID of the Player object contained at this node.
        Returns
        -------
        self.player.uid: str
        """
        return self.player.uid

    def __str__(self):
        """
        Returns the string representation of the PlayerNode
        Returns
        -------
        str
        """
        return f"Node for {self.player.uid}."