from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def __find_self_or_parent(self, player: Player, current_node: PlayerBNode):
        """
        Finds a player's node based on its name. If a player with the same name is found,
        returns the existing node, else returns the parent node.

        Parameters
        ----------
        player : Player
        current_node : PlayerBNode

        Returns
        -------
        PlayerBNode
        """
        # check if player's name is less than/greater than/equal to player at current node
        if player.name < current_node.player.name:
            if current_node.subtree_left is not None:
                # if less than, recurse on left subtree
                return self.__find_self_or_parent(player, current_node.subtree_left)
            # if left subtree is empty, parent found
            return current_node
        elif player.name > current_node.player.name:
            # if greater than, recurse on right subtree
            if current_node.subtree_right is not None:
                return self.__find_self_or_parent(player, current_node.subtree_right)
            # if right subtree is empty, parent found
            return current_node
        else:
            # if equal, return match
            return current_node


    def insert(self, player: Player):
        if self.__root is not None:
            parent = self.__find_self_or_parent(player, self.__root)
            if player.name < parent.player.name:
                parent.subtree_left = PlayerBNode(player)
                print(parent.subtree_left.player)
            elif player.name > parent.player.name:
                parent.subtree_right = PlayerBNode(player)
                print(parent.subtree_right.player)
            else:
                parent.player.uid = player.uid
                print(parent.player)
        else:
            self.__root = PlayerBNode(player)

