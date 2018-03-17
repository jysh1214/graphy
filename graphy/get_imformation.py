class GI():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.Insidence_Matrix = ins_matrix
        self.N = len(self.Adjacency_Matrix)


    def check_conn(self, v_a, v_b):
        """
        Parameters:
            v_a(int): Vertex No.

            v_b(int): Vertex No.

        Returns:
            bool: Return True, if v_a and v_b is adjacent.

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError
        """
        if self.Adjacency_Matrix[v_a][v_b] != 0:
            return True


    def get_degree(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No.

        Returns:
            self.degree[vertex](int): Degree of the input vertex.

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError
        """
        return self.get_in_degree(vertex)


    def get_in_degree(self, vertex):
        """
        """
        in_degree = 0
        for i in range(self.N):
            if self.Adjacency_Matrix[i][vertex] != 0:
                in_degree += 1

        return in_degree


    def get_out_degree(self, vertex):
        """
        """
        out_degree = 0
        for i in range(self.N):
            if self.Adjacency_Matrix[vertex][i] != 0:
                out_degree += 1

        return out_degree


    def get_nb(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No..

        Returns:
            nbs_list(list): All neighbors of the vertex. 

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError
        """
        nbs_list = []
        for i in range(len(self.Adjacency_Matrix)):
            if self.Adjacency_Matrix[vertex][i] != 0:
                nbs_list.append(i)

        return nbs_list


    def get_re(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No..

        Returns:
            nbs_list(list): All reachable vertices of the vertex. 

        Attention:
            Directed graph difinition.

        Raises:
            ValueError, TypeError
        """
        re_list = []
        for i in range(len(self.Adjacency_Matrix)):
            if self.Adjacency_Matrix[vertex][i] != 0:
                re_list.append(i)

        return re_list


    def get_pre(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No..

        Returns:
            nbs_list(list): All predecessor vertices of the vertex. 

        Attention:
            Directed graph difinition.

        Raises:
            ValueError, TypeError
        """
        pre_list = []
        for i in range(len(self.Adjacency_Matrix)):
            if self.Adjacency_Matrix[i][vertex] != 0:
                pre_list.append(i)

        return pre_list


    def get_edge(self, v_a, v_b):
        """
        Parameters:
            v_a(int): Vertex No..

            v_b(int): Vertex No..

        Returns:
            int.: Eage No. of two vertices.

        Attention:
            Two vertices must be adjacent.

            Return a edge from v_a to v_b in directed graph.

        Raises:
            ValueError, TypeError
        """
        if self.Adjacency_Matrix[v_a][v_b] == 0:
            return False

        for i in range(len(self.Insidence_Matrix[0])):
            if (self.Insidence_Matrix[v_a][i]==1) and\
               (self.Insidence_Matrix[v_b][i]==1):
                return i


    def get_inter(self, edge_1, edge_2):
        """
        Returns: Intersection verdex of two edge.
        """
        for i in range(self.N):
            if self.Insidence_Matrix[i][edge_1] and \
               self.Insidence_Matrix[i][edge_2]:
                return 


    def get_head(self, edge):
        """
        Parameters:
            edge(int): Edge No.

        Returns:
            int.: The head vertex of the edge.

        Attention:
            Directed graph difinition.

        Raises:
            ValueError, TypeError
        """
        (a, b) = self.edge_term(edge)
        if self.Adjacency_Matrix[a][b] != 0:
            return b
        else:
            return a


    def get_tail(self, edge):
        """
        Parameters:
            edge(int): Edge No.

        Returns:
            int.: The tail vertex of the edge.

        Attention:
            Directed graph difinition.

        Raises:
            ValueError, TypeError
        """
        (a, b) = self.edge_term(edge)
        if self.Adjacency_Matrix[a][b] != 0:
            return a
        else:
            return b


    def get_weight(self, edge):
        """
        Parameters:
            edge(int): Edge No..

        Returns: Weight of the input edge.

        Raises:
            ValueError, TypeError
        """
        (v_a, v_b) = self.edge_term(edge)

        if self.Adjacency_Matrix[v_a][v_b]:
            return self.Adjacency_Matrix[v_a][v_b]
        else:
            return self.Adjacency_Matrix[v_b][v_a]
            

    def edge_term(self, edge):
        """
        Attention:
            Undirected graph difinition.
        """
        temp = []
        for i in range(len(self.Insidence_Matrix)):
            if self.Insidence_Matrix[i][edge] == 1:
                temp.append(i)
            if len(temp) == 2:
                return temp
