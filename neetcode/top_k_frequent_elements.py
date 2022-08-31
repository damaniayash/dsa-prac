from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        print(hashmap)
        res = [[] for i in range(0,len(nums)+1)]
        for n, c in hashmap.items():
            print(n,c)
            res[c].append(n)
        print(res)
        res = list(chain.from_iterable(res))
        return res[len(res)-k:]

        
        
        # frek = []
        # for i in Counter(nums).most_common(k):
        #     frek.append(i[0])
        # return frek
        
        # hashmap = {}
        # for i in nums:
        #     if hashmap.get(i) == None:
        #         hashmap[i] = 1
        #     else:
        #         hashmap[i] = hashmap[i] + 1
        # sor = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        # sorr =[]
        # for i in range(0,k):
        #     sorr.append(sor[i][0])
        # return sorr
    
            
        