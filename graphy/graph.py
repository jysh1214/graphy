from .get_imformation import GI
from .graph_traversal import GT
from .path_problem import PT
from .min_spanning_tree import MST
from .shortest_path_problem import SP
from .he_problem import HE
from .domination import DM
import numpy as np

class Graph():
    def __init__(self, adj_matrix, ins_matrix, V, E, region, R):
        """
        Parameters:
            adj_matrix(list):
                The adjacency matrix of the graph.

            ins_matrix(list):
                The incidence matrix of the graph.
                Auto creat if the graph is undirect.


            V(list): 
                Vertex name list.
                V = [Vertex_0 name, Vertex_1 name, ...], default 0~n if input None

            E(list): 
                Edge name list.
                E = [Edge_0 name, Edge_1 name, ...], default 0~m if input None

            region(list):
                A matrix record which edges region surrounded by .
                region = Region_0|Region_1 ...
                   Edge_0    1   |    0
                   Edge_1    1   |    1  
                       ...
                EX:
                region[a][x] = region[b][x] = region[c][x] = 1: 
                region_x surrounded by edge_a, b, c

                It's planar graph difinition.
                input None if none

            R(list):
                Region name list.
                R = [Region_0 name, Region_1 name, ...], input None if none

        Raises:
            ValueError, TypeError

       
        EX: simple undirect G = (V, E), A = adjacency matrix, B = incidence matrix

            g = Graph(A, B, None, None, None, None)
        """
        self.N = len(adj_matrix)

        for i in range(self.N):
            if len(adj_matrix[i]) != self.N:
                print('Input data error!')
                return False

        self.Adjacency_Matrix = adj_matrix

        self.Directed = False
        for i in range(self.N):
            for j in range(self.N):
                if self.Adjacency_Matrix[i][j] !=\
                   self.Adjacency_Matrix[j][i]:
                   self.Directed = True 

        total_in_degree = 0
        for i in range(self.N):
            in_degree = 0
            for j in range(self.N):
                if self.Adjacency_Matrix[i][j] != 0:
                    in_degree += 1
            total_in_degree += in_degree

        total_out_degree = 0
        for i in range(self.N):
            out_degree = 0
            for j in range(self.N):
                if self.Adjacency_Matrix[j][i] != 0:
                    out_degree += 1
            total_out_degree += out_degree

        if self.Directed:
            self.edges = total_in_degree + total_out_degree
        else:
            # total degree = total in degree = total out degree
            self.edges = int(total_in_degree/2)

        if ins_matrix != None:
            for i in range(self.N):
                if len(ins_matrix[i]) != self.edges:
                    print('Input incidence matrix error!')
                    return False

                else: self.Insidence_Matrix = ins_matrix

        else:
            ins_matrix = [[0 for i in range(self.edges)] for j in range(self.N)]
            e = 0
            while e < self.edges:
                for i in range(self.N):
                    for j in range(i, self.N):
                        if self.Adjacency_Matrix[i][j] != 0:
                            ins_matrix[i][e] = 1
                            ins_matrix[j][e] = 1
                            e += 1

        if V == None:
            V = [i for i in range(self.N)]
        else:
            if len(V) == self.N:
                self.V = V
            else:
                print('Input V error!')
                return False

        if E == None:
            E = [i for i in range(len(self.Insidence_Matrix[0]))]
        else:
            if len(E) == len(self.Insidence_Matrix[0]):
                self.E = E
            else:
                print('Input E error!')
                return False              

        self.Region = region

        if self.Region == None:
            self.R = None
        else:
            self.R = R

    def get_degree(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No. or str.

        Returns:
            self.degree[vertex](int): Degree of the input vertex.

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError
        """   
        vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_degree()

    def in_degree(self, vertex):
        """
        """
        vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_in_degree()

    def out_degree(self, vertex):
        """
        """
        vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_out_degree()

    def get_isol(self):
        """
        Returns:
            isol(list): Isolated vertices.

        Raises:
            ValueError, TypeError
        """

        isol = []
        for i in range(self.N):
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]==0) and (i!=j):
                    isol.append([i])

        return isol

    def get_nb(self, vertex):
        """
        Parameters:
            vertex(int): Vertex number.

            vertex(str): Will be changed to vertex number.

        Returns:
            nb(list): All neighbors of the vertex. 

        Raises:
            ValueError, TypeError
        """
        vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_nb(vertex)

    def get_edge(self, v_a, v_b):
        """
        Parameters:
            v_a(int): Vertex No..

            v_a(str): Vertex name.

            v_b(int): Vertex No..

            v_b(str): Vertex name.

        Returns:
            int.: Eage No. of two vertices.

        Attention:
            Two vertices must be adjacent.

        Raises:
            ValueError, TypeError
        """
        v_a = name_to_num(v_a, self.V)
        v_b = name_to_num(v_b, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_edge(v_a, v_b)

    def get_weight(self, edge):
        """
        Parameters:
            edge(int): Edge No..

            edge(str): Edge name.

        Returns: Weight of the input edge.

        Raises:
            ValueError, TypeError
        """
        edge = name_to_num(edge, self.E)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_weight(edge)

    ### Decision problem ###

    def check_con(self):
        """
        Vars:
            self.Adjacency_Matrix

        Returns:
            bool.:If the graph connected, return True.
        """

        dfs = self.DFS(0, [])
        if len(dfs) == self.N:
            return True
        else:
            return False

    def check_cycle(self):
        """
        Attention:
            Include vertex connecting to itself. 

        Returns:
            bool.:If the graph contain cycle, return True.
        """
        bool_matrix = np.matrix(self.Adjacency_Matrix)
        # matrix[x, y] = list[x][y]
        for i in range(self.N):
            for j in range(self.N):
                if self.Adjacency_Matrix[i][j] != 0:
                    bool_matrix[i, j] = 1
                else:
                    bool_matrix[i, j] = 0

        for j in range(self.edges):
            for k in range(self.N):
                if bool_matrix[k, k]:
                    return True

            bool_matrix *= bool_matrix

        return False 

    def check_compl(self):
        """
        Attention:
            Undirected graph difinition.

        Returns:
            Return True if the graph is complete.
        """
        for i in range(self.N):
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]==0) and (i!=j):
                    return False

        return True

    def check_isol(self): # done
        # if exit isolate vertex, return True

        for i in range(self.N):
            flag = True
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]!=0) and (i!=j):
                    flag = False
            if flag: return True

        return False

    """
    def check_isom(self, adj_matrix):
        # check isomorphic
        # input the other adjacency matrix
        # output True if isomorphic

    """

    def check_path(self, v_a, v_b, block):
        """
        Parameters:
            v_a(int or str): Start vertex.

            v_b(int or str): Destinated vertex.

            block(list): Banned vertices list.
                         Int. elements difinition.

        Returns:
            bool.: Return True, if exist a path from v_a to v_b.

        Raises:
            ValueError, TypeError
        """
        v_a = name_to_num(v_a, self.V)
        v_b = name_to_num(v_b, self.V)

        # from path_problem
        p = PT(self.Adjacency_Matrix)

        return p.check_path(v_a, v_b, block)

    def check_sc(self):
        """
        Returns:
            bool.: Return True, if the graph is strongly connected.

        Attention:
            Directed graph difinition.

        Raises:
            ValueError, TypeError
        """
        for i in range(self.N):
            id_ = self.get_in_degree(i)
            od_ = self.get_out_degree(i)

            if (id_==0) or (od_==0):
                return False

        return True

    def check_bi(self):
        """
        Returns:
            bool.: Return True, if the graph is bipartite.

        Raises:
            ValueError, TypeError
        """
        
        #check by theorem first
        # (G is bipartite graph) <=> (G don't cotain odd length cycle)
        c = self.cycle()
        for i in range(len(c)):
            if (len(c[i])%2): 
                return False


    ### graph traversal ###

    def DFS(self, start, block):
        """Depth first search
        Parameters:
            start(int): Start vertex number.

            start(str): Start vertex name.

        Attention:
            Small vertex No. has high priority.

        Returns:
            dfs(list):

        Raises:
            ValueError, TypeError
        """
        start = name_to_num(start, self.V)

        # from graph_traversal
        gt = GT(self.Adjacency_Matrix)
        return gt.dfs(start)

    def BFS(self, start):
        """Breadth first search
        Parameters:
            start(int): Start vertex number.

            start(str): Start vertex name.    

        Attention:
            Small vertex No. has high priority.

        Returns:
            bfs(list):
        """
        start = name_to_num(start)

        # from graph_traversal
        gt = GT(self.Adjacency_Matrix)
        return gt.bfs(start)

    ### min spainning tree ###
    
    def Kruskal_algo(self):
        # from min_spanning_tree
        mst = MST(self.Adjacency_Matrix, self.Insidence_Matrix)
        return mst.kruskal_algo()

    def Prims_algo(self, root):
        # from min_spanning_tree
        mst = MST(self.Adjacency_Matrix, self.Insidence_Matrix)
        return mst.prims_algo(root)
        
    ### shortest path problem ###

    def Dijkstra_algo(self, start):
        """
        Returns:
            dist(list): Start vertex to all the others vertices distance.

        Attention:
            Negative weight could make misjudgment.

        Raises:
            ValueError, TypeError
        """
        start = name_to_num(start, self.V)

        # from shortest_path_problem
        sp = SP(self.Adjacency_Matrix, self.Insidence_Matrix)
        return sp.dijkstra_algo(start)

    def Bellman_Ford_algo(self, start):
        """
        """
        start = name_to_num(start, self.V)

        # from shortest_path_problem
        sp = SP(self.Adjacency_Matrix, self.Insidence_Matrix)
        return sp.bellman_ford_algo(start)

    def Floyd_Warshall_algo(self):
        """
        """
        # from shortest_path_problem
        sp = SP(self.Adjacency_Matrix, self.Insidence_Matrix)
        return sp.floyd_warshall_algo()

    ### all-pairs shortest path problem ###

    def Johnson_algo(self):
        pass

        # reweight

    ### AOV problem ###

    def all_path(self,v_a, v_b, visited, block):
        """
        Parameters:
            v_a(int): Start vertex No..

            v_a(str): Start vertex name.

            v_b(int): Destinated vertex No..

            v_b(str): Destinated vertex name.

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
        v_a = name_to_num(v_a, self.V)
        v_b = name_to_num(v_b, self.V)

        # from path_problem
        p = PT(self.Adjacency_Matrix, self.Insidence_Matrix)

        return p.all_path(v_a, v_b, visited, block)  

    def bridge(self):
        # return all bridge
        pass

    def triangle(self, n=3):
        # return numbers of triangles in G

        A = np.matrix(self.Adjacency_Matrix)
        same = 1
        while n > 0:
            A *= A
            same *= n
            n -= 1

        total = 0
        for i in range(self.N):
            total += A[i,i]

        return total/same

    def SCC(self):
        # strongly connected component
        """
        Returns:
            bool.

        Attention: Directed graph difinition.

        Raises:
            ValueError, TypeError
        """

        # Kosaraju's algo.

        # DFS

        # E transfer to get Gt

        # DFS(Gt)

        pass

    def cut_point(self):
        pass

    def cut_set(self):
        pass

    ### domination ###

    def clique(self):
        """
        Attention:
            Maximal
        """
        # from domination
        dm = DM(self.Adjacency_Matrix, self.Insidence_Matrix)
        return dm.clique()

    def indp_set(self):
        """
        Attention:
            Maximal
        """
        # from domination
        dm = DM(self.Adjacency_Matrix, self.Insidence_Matrix)
        return dm.indp_set()

    def dominating_set(self):
        """
        Attention:
            Minimal
        """
        # from domination
        dm = DM(self.Adjacency_Matrix, self.Insidence_Matrix)
        return dm.dominating_set()

    def vertex_cover(self):
        """
        Attention:
            Minimal
        """
        # from domination
        dm = DM(self.Adjacency_Matrix, self.Insidence_Matrix)
        return dm.vertex_cover()

    def edge_cover(self):
        """
        Attention:
            Minimal
        """
        # from domination
        dm = DM(self.Adjacency_Matrix, self.Insidence_Matrix)
        return dm.edge_cover()

    ### PE_problem ###

    def EC(self, start):
        """
        Returns:
            list: All Eulerian circuit.

        Raises:
            ValueError, TypeError
        """
        start = name_to_num(start)

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)
        return he.ec(start)


    def HC(self, start): 
        """
        Returns:
            list: All Hamiltonian cycle.

        Vars:
            self.N(int):

        Raises:
            ValueError, TypeError
        """
        start = name_to_num(start, self.V)

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)
        return he.hc(start)

    def ET(self, start): 
        """
        Returns:
            list: All Eulerian trail(chain)

        Raises:
            ValueError, TypeError
        """
        start = name_to_num(start, self.V)

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)
        return he.et(start)

    def HP(self, v_a, v_b): 
        """
        Returns:
            list: All Hamiltonian path

        Raises:
            ValueError, TypeError
        """
        v_a = name_to_num(v_a, self.V)
        v_b = name_to_num(v_b, self.V)

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)

        return he.hp(v_a, v_b)


# the others function

def put_all(a, b):
    for i in a:
        b.append(i)

    return b

def name_to_num(name, chart):
    # input: name_str
    # output: number_int of name in chart
    try:
        int(name)
        return int(name)

    except:
        for i in range(len(chart)):
            if chart[i] == name:
                return i

        return False
