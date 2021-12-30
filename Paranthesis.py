from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            print(left, right, S)
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

    def generateParenthesisPath(self, n: int) -> List[str]:
        ans = []
        def backtrack(left = 0, right = 0, path=""):
            if left==right==n:
                ans.append(path)
                return
            if left < n:
                backtrack(left+1, right, path+'(')
            if right < left:
                backtrack(left, right+1, path+')')
        backtrack()
        return ans

c= Solution()
output = c.generateParenthesis(2)
print(output)