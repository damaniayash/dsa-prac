'''
Consider 4 5 6
                   []
               [g]                               [h]             [i]
         [gj]         [gk]              [gl]    [hj] [hk] [hl]   [ij][ik][il]
[gjm] [gjn] [gjo]  [gkm] [gkn] [gko]

we maintain a dict with alphabets combination for each number.
We call dfs function until our i is less than len(digits).
we loop through the possible alphabets for this number and call dfs on each number.
Use the classic backtracking loop.
If the length of curr == length of digits. We need to store that because it is a possible arrangement of the numbers.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return
            
        dig_dict = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z'],
        }

        res = []

        def dfs(i, curr):
            
            if len(curr) == len(digits):
                res.append(''.join(curr.copy()))
            if i >= len(digits):
                return

            for x in dig_dict[int(digits[i])]:
                curr.append(x)
                dfs(i + 1, curr)
                curr.pop()

        dfs(0, [])
        return res

        