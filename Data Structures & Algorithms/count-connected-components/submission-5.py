class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        class union_find:
            def __init__(self,n):
                self.parent = [i for i in range(n)]
                self.rank = [1]*n
                self.count = n

            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]  # path compression
                    x = self.parent[x]
                return x
            
            def union(self, x, y):
                parent_x = self.find(x)
                parent_y = self.find(y)

                if parent_x == parent_y :
                    return 
                
                if self.rank[parent_x] < self.rank[parent_y]:
                    parent_x, parent_y = parent_y, parent_x
                
                
                self.parent[parent_y] = parent_x
                if  self.rank[parent_x] == self.rank[parent_y]:
                
                    self.rank[parent_x] += 1
                
                self.count -=  1
                
                return parent_x 
        
        unf = union_find(n)

        for e in edges:
            unf.union(e[0],e[1])
            
        
        print(unf.parent)
        
        return unf.count