class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        my_stack = []
        for ch in num:
            while my_stack and ch<my_stack[-1] and k>0:
                k -= 1
                my_stack.pop()
            my_stack.append(ch)
        while not k==0:
            k -= 1
            my_stack.pop()

        return "".join(my_stack)


tc = "112"
s = Solution()

print(s.removeKdigits(tc, 1))
