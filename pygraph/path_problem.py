from .get_imformation import GI
from .graph_traversal import GT

class PT():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.Insidence_Matrix = ins_matrix
        self.N = len(self.Adjacency_Matrix)


    def all_path(self, v_a, v_b, visited, block):
        """
        Parameters:
            v_a(int): Start vertex No..

            v_b(int): Destinated vertex No..

            visited(list):
                Record visited vertices.
                Input empty list([]) first generally.

            block(list): Banned vertices list.

        Returns:
            all_path_list(list): All path from v_a to v_b.

        Attention:
            Could contain loop.

        Raises:
            ValueError, TypeError
        """
        def all_path_resursion(v_a, v_b, visited, block):
            visited.append(v_a)

            if v_a == v_b:
                temp = []
                temp = put_all(visited, temp)
                all_path_list.append(temp)
                # print(visited)
            
            else:
                # from get_imformation
                gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
                a_nb = gi.get_nb(v_a)
                for i in range(len(a_nb)):
                    if (not(a_nb[i] in visited)) and self.check_path(a_nb[i], v_b, visited):
                        if not (a_nb[i] in block):
                            all_path_resursion(a_nb[i], v_b, visited, block)
                            visited.remove(visited[-1]) ### backtracking ###


        all_path_list = []
        all_path_resursion(v_a, v_b, visited, block)
        return all_path_list


    def check_path(self, v_a, v_b, block):
        """
        Parameters:
            v_a(int): Vertex No..

            v_b(int): Vertex No..

            block(list): Banned vertices list.
                         Int. elements difinition.

            Returns:
                bool.: Return True, if exist a path from v_a to v_b.

            Raises:
                ValueError, TypeError
        """
        if v_a == v_b:
            return True

        # from graph_traversal
        gt = GT(self.Adjacency_Matrix, self.Insidence_Matrix)
        if v_b in gt.dfs(v_a, block):
            return True
        else:
            return False
            

def put_all(a, b):
    for i in a:
        b.append(i)
    return b
