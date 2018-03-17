class DS():
    def __init__(self, ins_matrix, con_ver, mst, v_a, v_b):
        self.Insidence_Matrix = ins_matrix
        self.mst = mst
        self.con_ver = con_ver
        self.set = []


        def get_edge(a, b):   
            for i in range(len(self.Insidence_Matrix[0])):
                if (self.Insidence_Matrix[a][i]==1) and\
                   (self.Insidence_Matrix[b][i]==1):
                   return i

        # check 'a', 'b' connected => 'a', 'b' are in same set
        def conn(a, b):
            for i in range(len(self.set)):
                if a in self.set[i]:
                    a_set = self.set[i]

            for j in range(len(a_set)):
                e = get_edge(a_set[j], b)
                if e in self.mst:
                    return True

            return False

        def partion(v):
            flag = False
            # find which set the vertex belong
            for i in range(len(self.set)):
                if conn(self.set[i][0], v):
                    # 'v' belong set_i
                    self.set[i].append(v)
                    flag = True
            if not flag: # new partion
                self.set.append([v])


        # repartition
        for i in range(len(self.con_ver)):
            partion(self.con_ver[i])

        if len(self.set) == 1:
            flag = False
        else:
            flag = True

        while flag:
            flag = False
            for j in range(1, len(self.set)):
                for k in range(0, j-1):
                    if conn(self.set[k][0], self.set[j]):
                        # merge set
                        self[k] = put_all(self.set[j], self.set[k])
                        self.set[j] = []
                        flag = True

            self.set = list(filter(lambda x: x != [], self.set))

        partion(v_a)
        partion(v_b)

    def get_set(self):
        return self.set


    def same_set(self, v_a, v_b):
        """
        Parameters:
            v_a(int): Vertex No.

            v_b(int): Vertex No.

        Returns:
            bool.:If v_a and v_b belong same set, return True.
        """
        for i in range(len(self.set)):
            if v_a in self.set[i]:
                if v_b in self.set[i]:
                    return True

        return False
        

def put_all(a, b):
    for i in a:
        b.append(i)
    return b
