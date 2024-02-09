'''
Store the first interval into res so the we can initialize prev with this value.
Start iteration from the first index.
prev = res[-1]
Check if prev and curr overlap.
if they do:
    we need to merge the intervals.
    Take the min  of the start values
    Take the max of the end values.
    These will become the bounds of our new merged interval.
    Add this new interval as the last element of res.
    This will overwrite our prev with the newly merged interval.
else:
    we can simply add curr to res since the prev and curr do not overlap so we no not need to merge them.  
return res     
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def overlap(prev, curr):
            front = max(prev[0], curr[0])
            back = min(prev[1], curr[1])
            return back - front >= 0

        result = [intervals[0]]

        for curr in intervals[1:]:
            prev = result[-1]
            if overlap(curr, prev):
                front = min(curr[0], prev[0])
                back = max(curr[1], prev[1])
                result[-1] = [front, back]
            else:
                result.append(curr)
        
        return result