class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__subtree_left = None
        self.__subtree_right = None

    @property
    def player(self):
        return self.__player

    @property
    def subtree_left(self):
        return self.__subtree_left

    @subtree_left.setter
    def subtree_left(self, value):
        if value is not None:
            self.__subtree_left = value

    @property
    def subtree_right(self):
        return self.__subtree_right

    @subtree_right.setter
    def subtree_right(self, value):
        if isinstance(value, PlayerBNode):
            self.__subtree_right = value

    # @classmethod
    # def get_recursive_subtrees(cls, current_node):
    #     subtree = [current_node]
    #     subtree_left = []
    #     subtree_right = []
    #     if current_node.subtree_left is not None:
    #         subtree_left = PlayerBNode.get_recursive_subtrees(current_node.subtree_left)
    #     if current_node.subtree_right is not None:
    #         subtree_right = PlayerBNode.get_recursive_subtrees(current_node.subtree_right)
    #     return subtree + subtree_left + subtree_right


    def __repr__(self):
        return f"PlayerBNode(Player = {self.player})"

