from .get_imformation import GI
from .disjoint_set import DS

import math

class MST():
    def __init__(self, adj_matrix, ins_matrix):
        """
        Parameters:
            adj_matrix(list):
                The adjacency matrix of the graph.

            ins_matrix(list):
                The incidence matrix of the graph.
                Auto creat if the graph is undirect.

        Returns:
            Min spanning tree.

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError 
        """
        self.Adjacency_Matrix = adj_matrix
        self.N = len(self.Adjacency_Matrix)
        self.Insidence_Matrix = ins_matrix

        self.con_ver = [] # contain vertices list now
        self.mst = []     # min spanning tree now


    def kruskal_algo(self):
        """
        Returns: Min spanning tree.

        Raises:
            ValueError, TypeError
        """
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        E = [(i, gi.get_weight(i)) for i in range(len(self.Insidence_Matrix[0]))]

        # edges sorted by weight
        E = sorted(E, key = lambda x: x[1])
        for i in range(len(E)):
            E[i] = E[i][0]

        for i in range(len(E)):
            (v_a, v_b) = gi.edge_term(E[i])
            
            # from disjoint_set
            ds = DS(self.Insidence_Matrix, self.con_ver, self.mst, v_a, v_b)
            if ds.same_set(v_a, v_b):
                pass # the edge could make circle
            else:
                self.mst.append(E[i])
                if not (v_a in self.con_ver):
                    self.con_ver.append(v_a)
                if not (v_b in self.con_ver): 
                    self.con_ver.append(v_b)

        return self.mst


    def prims_algo(self, root):
        """
        Parameters:
            root(list):
                The root of the min spanning tree.
                Plays mst in interation.
                Input [root] first generally.

        Returns:
            Min spanning tree.

        Raises:
            ValueError, TypeError
        """
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)

        # all neighbors of mst
        min_  = math.inf
        for i in range(len(root)):
            root_nb = gi.get_nb(root[i])
            # find which edges weight is min
            for j in range(len(root_nb)):
                if not(root_nb[j] in self.con_ver):
                    e = gi.get_edge(root[i], root_nb[j])
                    if gi.get_weight(e) < min_:
                        min_ = gi.get_weight(e)
                        min_term = root_nb[j]
                        min_edge = e

        if len(root) == self.N:
            return self.mst

        root.append(min_term)
        self.con_ver = root
        self.mst.append(min_edge)

        ### unnecessary check loop ###

        return self.prims_algo(root)
        

def put_all(a, b):
    for i in a:
        if not(i in b):
            b.append(i)
    return b
