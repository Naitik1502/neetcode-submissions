class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # def eval_exp(numbers: List[str], op: str) -> int:

        #     ans = int(numbers[-1])

        #     for i in range(len(numbers)-2, 1):

        #         if op == '+' :
        #             ans += int(numbers[i])
        #         elif op == '-' :
        #             ans -= int(numbers[i])
        #         elif op == '*' :
        #             ans *= int(numbers[i])
        #         elif op == '/' :
        #             ans //= int(numbers[i])

        #     return ans

        stack_numbers = []

        operands = ['+', '-', '*', '/']

        for token in tokens :

            if token in operands :

                token1, token2 = stack_numbers.pop(), stack_numbers.pop()

                if token == '+' :
                    stack_numbers.append(token1 + token2)

                elif token == '-' :

                    stack_numbers.append(token2 - token1)

                elif token == '*' :

                    stack_numbers.append(token1 * token2)

                elif token == '/' :

                    stack_numbers.append(int(float(token2/token1)))

            else :
                    stack_numbers.append(int(token))
                
        return int(stack_numbers[0])
                


        