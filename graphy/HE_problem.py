from .get_imformation import GI
from .graph_traversal import GT

class HE():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.Insidence_Matrix = ins_matrix
        self.N = len(self.Adjacency_Matrix)


    def ec(self, start):
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        dest = gi.get_pre(start)

        ec_list = []
        for i in range(len(dest)):
            temp = self.et(start, dest[i], [])
            for j in range(len(temp)):
                temp[j].append(gi.get_edge(dest[i], start))
                temp[j].append(start)
                
            ec_list = put_all(temp, ec_list)

        return ec_list


    def hc(self, start):
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        dest = gi.get_pre(start)

        hc_list = []
        for i in range(len(dest)):
            temp = self.hp(start, dest[i])
            for j in range(len(temp)):
                temp[j].append(start)
                
            hc_list = put_all(temp, hc_list)

        return hc_list


    def et(self, v_a):
        """
        Parameters:
            star(int): Start vertex No.

            passed(list): Input passed as [] first. 

        Returns:
            Eulerian tail from v_a to v_b.

        Raises:
            ValueError, TypeError
        """        
        def et_recursion(v_a, passed_vertex, passed_road):

            passed_vertex.append(v_a)
            
            if len(passed_road) == len(self.Insidence_Matrix[0]):
                temp = []
                i = 0
                j = 0
                while len(temp) < 2*len(self.Insidence_Matrix[0])+1:
                    temp.append(passed_vertex[i])
                    i += 1
                    if i != len(passed_vertex):
                        temp.append(passed_road[j])
                        j += 1

                et_list.append(temp)

            # form get_information
            gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
            re = gi.get_re(v_a)

            for i in range(len(re)):
                road = gi.get_edge(v_a, re[i])
                if road in passed_road:
                    continue

                passed_road.append(road)
                et_recursion(re[i], passed_vertex, passed_road)
                passed_vertex.remove(passed_vertex[-1]) ### backtracking ###

        et_list = []
        et_recursion(v_a, [], [])
        return et_list


    def hp(self, v_a, v_b):
        """
        Parameters:
            v_a(int): Start vertex No..

            v_b(int): Destination vertex No..

        Returns:
            Hamiltonian path from v_a to v_b.

        Raises:
            ValueError, TypeError
        """
        def hp_recursion(v_a, v_b, visited):

            visited.append(v_a)

            if v_a == v_b:
                temp = []
                temp = put_all(visited, temp)
                hp_list.append(temp)

            # from get_imformation
            gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
            re = gi.get_re(v_a)
            
            for i in range(len(re)):
                if re[i] in visited:
                    continue

                # reach v_b too early
                if (re[i]==v_b) and (len(visited)+1<self.N):
                    continue

                # maybe form two different community
                left = [i for i in range(self.N)]
                left = list(set(left)-set(visited)) 
                
                flag = True
                # from graph_traversal
                gt = GT(self.Adjacency_Matrix, self.Insidence_Matrix)
                # use 'undirected' dfs to show community
                dfs = gt.dfs(left[0], visited)
                if len(dfs) != len(left):
                    flag = False

                if not flag:
                    continue

                hp_recursion(re[i], v_b, visited)
                visited.remove(visited[-1]) ### backtracking ###

        hp_list = []
        hp_recursion(v_a, v_b, [])
        return hp_list
        

def put_all(a, b):
    for i in a:
        b.append(i)
    return b
