'''
The idea is that search the value of at each index of the target
with the corresponding index for every element in the triplet list.
However, there might be certain triplets with elements higher than those 
at the target's index these triplets will override the max calculations so we want
to get rid of them in the first step.
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
            
            triplet = []
            for i in range(0, len(triplets)):
                if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                    triplet.append(triplets[i])
            print(triplet)

            t0, t1, t2 = False, False, False
            for i in range(0, len(triplet)):
                if triplet[i][0] == target[0]:
                    t0 = True
            for i in range(0, len(triplet)):
                if triplet[i][1] == target[1]:
                    t1 = True
            for i in range(0, len(triplet)):
                if triplet[i][2] == target[2]:
                    t2 = True
            print(t0, t1, t2)
            return t0 and t1 and t2