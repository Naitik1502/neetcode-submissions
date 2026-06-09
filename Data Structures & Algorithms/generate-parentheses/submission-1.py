class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(ans, opens, closes):

            if len(ans) == 2*n :
                res.append(ans)
                return 
            
            if opens < n :
                backtrack(ans + '(', opens + 1, closes)
            
            if closes < opens :
                backtrack(ans + ')', opens , closes + 1)
        
        backtrack("", 0, 0)
        
        return res

        