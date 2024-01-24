'''
Create a hashmap with each char and its last occuring index.
We init two varaibles size and end and iterate over the list.
end denotes the fartherst index of all the chars encountered thus far.
We traverse through the list and if are current index == end ->
this means that we have covered all the chars encountered thus far and this is a valid partition.
We incrment size in every iteration and reset it when a valid group is found
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charmap = {}
        for ind, char in enumerate(s):
            charmap[char] = ind

        result = []
        size, end = 0, 0
        for ind, char in enumerate(s):
            size += 1
            if charmap[char] > end:
                end = charmap[char]
            # valid partiton found
            if ind == end:
                result.append(size)
                size = 0
                
        return result