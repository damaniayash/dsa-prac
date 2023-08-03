class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      
        stack = []
        ans = [0 for i in range(0, len(temperatures))]
        for index, t in temperatures:
            if not stack:
                stack.append((t, index))
            else:
                while stack and t > stack[-1][0]:
                    popped = stack.pop()
                    ans[popped[1]] = t[1] - popped[1]
                stack.append((t, index))
