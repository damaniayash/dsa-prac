class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if intervals == []:
            res.append(newInterval)
            return res

        def overlap(curr, prev):
            front = max(curr[0], prev[0])
            back = min(curr[1], prev[1])
            return back - front >= 0

        for curr in range(0, len(intervals)):
            if overlap(intervals[curr], newInterval):
                new_front = min(intervals[curr][0], newInterval[0])
                new_back = max(intervals[curr][1], newInterval[1])
                intervals[curr] = [new_front, new_back]
        
        res = [intervals[0]]

        for curr in intervals[1:]:
            prev = res[-1]
            if overlap(curr, prev):
                new_front = min(curr[0], prev[0])
                new_back = max(curr[1], prev[1])
                res[-1] = [new_front, new_back]
            else:
                res.append(curr)

        if newInterval[1] < res[0][0]:
             res.insert(0, newInterval)

        if newInterval[0] > res[-1][1]:
            res.append(newInterval)

        for curr in range(0, len(res)-1):
            if res[curr][1] < newInterval[0] and newInterval[1] < res[curr+1][0]:
                res.insert(curr+1, newInterval)
        return res
