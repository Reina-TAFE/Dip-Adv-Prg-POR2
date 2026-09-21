from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self, root: PlayerBNode | None = None):
        self.__root = root

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

    @classmethod
    def get_recursive_subtrees(cls, current_node: PlayerBNode) -> list[PlayerBNode]:
        subtree = [current_node]
        subtree_left = []
        subtree_right = []
        if current_node.subtree_left is not None:
            subtree_left = PlayerBNode.get_recursive_subtrees(current_node.subtree_left)
        if current_node.subtree_right is not None:
            subtree_right = PlayerBST.get_recursive_subtrees(current_node.subtree_right)
        return subtree + subtree_left + subtree_right

    def get_balanced_bst(self):
        def build_balanced_bst(nodes: list[Player]) -> PlayerBNode:
            """Creates a new PlayerBNode from center player of a Player array.
            Recursively creates left and right subtrees"""
            def center(nodes_arr: list[Player]) -> int:
                """Finds center position of Player array"""
                return len(list(nodes_arr)) // 2 # return center index of array

            def left(l_nodes: list[Player]) -> list[Player]:
                """Returns all node to the left of center."""
                return l_nodes[:center(l_nodes)] # return all nodes from start to center - 1

            def right(r_nodes: list[Player]) -> list[Player]:
                """Returns all node to the right of center."""
                return r_nodes[center(r_nodes)+1:] # return all nodes from center + 1 to end

            balanced_node = PlayerBNode(nodes[center(nodes)]) # create new node from center player

            if len(left(nodes)) >= 1: # check if any players less than
                # set left subtree to center of left players (less than)
                balanced_node.subtree_left = build_balanced_bst(left(nodes)) # recurse on left players to get center
            if len(right(nodes)) >= 1: # check if any players greater than
                # set right subtree to center of right players (greater than)
                balanced_node.subtree_right = build_balanced_bst(right(nodes)) # recurse on right players to get center
            return balanced_node # return balanced node

        if self.__root is not None:
            # get list of all nodes starting from root
            tree = PlayerBST.get_recursive_subtrees(self.__root)
            # get sorted list of players
            sorted_players = [node.player for node in sorted(tree, key=lambda node: node.player.name)]
            # create new PlayerBST using balanced root node from sorted player list
            balanced_bst = PlayerBST(root=build_balanced_bst(sorted_players))
            return balanced_bst
        return self # if PlayerBST is empty, return self




    #
    # def search_player(self, player_name: str):
    #     result = self.search_node(player_name)
    #     if result is not None:
    #         return result.player
    #     return None

