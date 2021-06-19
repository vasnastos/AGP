class Graph:
    def __init__(self,v,datainput):
        self.V=v
        self.adj_matrix=[[0 for _ in range(self.V)] for _ in range(self.V)]
        self.ReadSource(datainput)   
    def add_Edge(self,s,v,w):
        self.adj_matrix[s][v]=w

    def ReadSource(self,filepath):
        start=0
        with open(filepath,'r') as F:
            for line in F:
                data=[int(k) for k in line.split(',')]
                for node in data:
                    for k in range(len(data)):
                        self.add_Edge(start,k,data[k])
                start+=1
    
    def Nodes(self):
        return [str(i) for i in range(self.V)]

    def neighbors(self,node):
        return [gnode for gnode in range(self.V) if self.adj_matrix[node][gnode]!=0]
    
    def __str__(self):
        headers=[i for i in range(self.V)]
        from tabulate import tabulate
        msg='*Graph with {} Nodes\n'.format(self.V)
        msg+='*Nodes:{}\n'.format(",".join(self.Nodes()))
        msg+='--'*34+'\n'
        msg+=tabulate(self.adj_matrix,headers,tablefmt='fancy_grid',showindex='always')

        msg+='\n\n'
        
        for node in range(self.V):
            msg+=f'Node {node}:{" ".join([str(j) for j in self.neighbors(node)])}'
            msg+='\n'
        return msg


import os
def main():
   V=6
   if V==0:
       raise '0 Size Graph can not be represent'
   inputd=os.path.join('..','DATA','graph.txt')
   G=Graph(V,inputd)
   print(str(G))

if __name__=='__main__':
    main()

          
         
