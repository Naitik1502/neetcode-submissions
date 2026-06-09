class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def gen(ans, n, opens, closes):
            nonlocal res
            if len(ans) == 2*n :
                res.append(ans)
                return
            if opens < n :
                gen(ans + '(', n, opens + 1, closes)
            
            if closes < n and closes < opens :
                gen(ans + ')', n, opens, closes + 1)
               
        
        gen("", n, 0, 0)
        
        return res
            

            
            


        