class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < 0.001

            for i in range(0, len(nums)):
                for j in range(i+1, len(nums)):
                    op = [nums[i] * nums[j],
                            math.inf if nums[i] == 0 else nums[j] / nums[i],
                            math.inf if nums[j] == 0 else nums[i] / nums[j],
                            nums[i] + nums[j], nums[i] - nums[j], nums[j] - nums[i]]
                    for num in op:
                        nextcards = [num]
                        for k in range(len(nums)):
                            if k == i or k == j:
                                continue
                            nextcards.append(nums[k])
                        if dfs(nextcards):
                            return True                                            
            return False

        return dfs(cards)
    


    from typing import List
import math

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums, expressions):
            if len(nums) == 1:
                if abs(nums[0] - 24.0) < 0.001:
                    print(expressions[0])
                    return True

            for i in range(0, len(nums)):
                for j in range(i+1, len(nums)):
                    op = [("+", nums[i] + nums[j]),
                          ("-", nums[i] - nums[j]),
                          ("*", nums[i] * nums[j]),
                          ("/", math.inf if nums[i] == 0 else nums[j] / nums[i]),
                          ("/", math.inf if nums[j] == 0 else nums[i] / nums[j])]
                    for operator, num in op:
                        nextcards = [num]
                        nextexpressions = [f"({expressions[i]}) {operator} ({expressions[j]})"]
                        for k in range(len(nums)):
                            if k == i or k == j:
                                continue
                            nextcards.append(nums[k])
                            nextexpressions.append(expressions[k])
                        dfs(nextcards, nextexpressions)
                        #return True
            return False

        initial_expressions = [f"{num}" for num in cards]
        return dfs(cards, initial_expressions)
