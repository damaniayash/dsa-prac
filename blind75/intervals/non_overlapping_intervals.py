'''
First sort the intervals based on the basis of start time.
Check if the intervals overlap.
    if they do we will have to remove either prev or curr.
    select the interval which ends first and remove the interval with a longer end time
    [Exact understanding of why this greedy decision works is not clear to me however it works.]
    if both the intervals are same we can remove either one. else condition takes care of that.
    each time when overlap return true increment the removal_cnt

    retur removal cnt.

'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        def overlap(curr, prev):
            front = max(curr[0], prev[0])
            back = min(curr[1], prev[1])
            return back - front > 0

        intervals.sort(key = lambda x:x[0])

        removal_cnt = 0
        res = [intervals[0]]
        
        for curr in intervals[1:]:
            prev = res[-1]
            if overlap(curr, prev):
                removal_cnt += 1
                if curr[1] > prev[1]:
                    res[-1] = prev
                else:
                    res[-1] = curr
            else:
                res.append(curr)
        
        return removal_cnt