class Player:
    """
    A Player with a unique ID and name.
    """
    def __init__(self, unique_id: str, player_name: str):
        """
        Constructor for Player object
        """
        self.__uid = unique_id
        self.__name = player_name

    @property
    def uid(self):
        """
        The unique ID of the player.
        Returns
        -------
        uid: str
        """
        return self.__uid

    @property
    def name(self):
        """
        The unique ID of the player.
        Returns
        -------
        name : str
        """
        return self.__name

    def __str__(self):
        """
        A string representation of the player.
        Returns
        -------
        str
        """
        return f"{self.uid} - {self.name}"