class Player:
    """
    A Player with a unique ID and name.
    """
    def __init__(self, unique_id: str, player_name: str, score: int = 0):
        """
        Constructor for Player object
        """
        self.__uid = unique_id
        self.__name = player_name
        self.__score = score

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

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if isinstance(value, int) and value >= 0:
            self.__score = value
        else:
            raise ValueError

    @classmethod
    def hash(cls, key: str) -> int:
        """
        Arbitrary hashing function.
        """
        hash_key = 0
        for i in range(len(key)):
            hash_key += int(ord(key[i]) - i) * int(ord(key[-i]) + i)
        return hash_key

    def __hash__(self):
        return self.hash(self.__uid)

    def __repr__(self):
        return f"{self.__class__.__name__}(uid='{self.uid}', name='{self.name}', score={self.score})"

    def __str__(self):
        """
        A string representation of the player.
        Returns
        -------
        str
        """
        return self.__repr__()

    def __lt__(self, other):
        """
        Less Than.
        """
        if isinstance(other, Player):
            return self.__score < other.score
        return self.score < other

    def __le__(self, other):
        """
        Less Than or Equal To.
        """
        if isinstance(other, Player):
            return self.__score <= other.score
        return self.__score <= other

    def __eq__(self, other):
        """
        Equal To.
        """
        if isinstance(other, Player):
            return self.__score == other.score
        return self.__score == other

    def __ne__(self, other):
        """
        Not Equal To.
        """
        if isinstance(other, Player):
            return self.__score != other.score
        return self.__score != other

    def __gt__(self, other):
        """
        Greater Than.
        """
        if isinstance(other, Player):
            return self.__score > other.score
        return self.__score > other

    def __ge__(self, other):
        """
        Greater Than or Equal To.
        """
        if isinstance(other, Player):
            return self.__score >= other.score
        return self.__score >= other

    @classmethod
    def sort_quickly(cls, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = lambda array: [player for player in array if player >= pivot]
        right = lambda array: [player for player in array if player < pivot]
        # for x in arr[1:]:
        #     if x < pivot:
        #         left.append(x)
        #     else:
        #         right.append(x)
        return Player.sort_quickly(left(arr[1:])) + [pivot] + Player.sort_quickly(right(arr[1:]))





