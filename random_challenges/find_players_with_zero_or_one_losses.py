from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        temp = []
        w = set([item[0] for item in matches])
        l = [item[1] for item in matches]
        t = list(w-set(l))
        t.sort()
        ans.append(t)
        ldict = Counter(l)
        for k,v in ldict.items():
            if v == 1:
                temp.append(k)
        temp.sort()
        ans.append(temp)
        return ans
