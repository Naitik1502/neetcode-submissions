class Solution:
    def isValid(self, s: str) -> bool:

        char_map = {')' : '(', '}' : '{', ']' : '['}

        char_stack = []

        for ch in s :

            if ch in char_map :

                if not char_stack or char_map[ch] != char_stack[-1] :
                    return False
                char_stack.pop()
            else :
                char_stack.append(ch)
        
        return True if len(char_stack) == 0 else False




        