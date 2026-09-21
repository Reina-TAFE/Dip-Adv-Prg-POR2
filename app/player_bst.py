from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def __find_self_or_parent(self, name: str, current_node: PlayerBNode):
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
        if name < current_node.player.name:
            if current_node.subtree_left is not None:
                # if less than, recurse on left subtree
                return self.__find_self_or_parent(name, current_node.subtree_left)
            # if left subtree is empty, parent found
            return "parent", current_node
        elif name > current_node.player.name:
            # if greater than, recurse on right subtree
            if current_node.subtree_right is not None:
                return self.__find_self_or_parent(name, current_node.subtree_right)
            # if right subtree is empty, parent found
            return "parent", current_node
        else:
            # if equal, return match
            return "self", current_node


    def insert(self, player: Player):
        # check tree has a root node
        if self.__root is not None:
            self_or_parent, node = self.__find_self_or_parent(player.name, self.__root)
            if self_or_parent == "self": # node is self
                # update node uid
                node.player.uid = player.uid
                print(node.player)
            else: # node is parent
                # set parent subtree to node
                if player.name < node.player.name:
                    node.subtree_left = PlayerBNode(player)
                    print(node.subtree_left.player)
                elif player.name > node.player.name:
                    node.subtree_right = PlayerBNode(player)
                    print(node.subtree_right.player)
        else:  # tree has no root node
            self.__root = PlayerBNode(player) # set tree root node

    def search(self, player_name: str):
        if self.__root is not None:
            result, node = self.__find_self_or_parent(player_name, self.__root)
            if result == "self" and node.player.name == player_name:
                # if returned node is self, return node
                return node
        # if node is not found, return None
        return None
    #
    # def search_player(self, player_name: str):
    #     result = self.search_node(player_name)
    #     if result is not None:
    #         return result.player
    #     return None

