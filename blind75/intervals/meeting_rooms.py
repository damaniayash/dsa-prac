'''
Lintcode
'''
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        def overlap(curr, prev):
            front = max(curr.start, prev.start)
            back = min(curr.end, prev.end)
            return back - front > 0

        intervals.sort(key = lambda x:x.start)
        
        prev = intervals[0]
        for curr in intervals[1:]:
            if overlap(curr, prev):
                return False
            prev = curr
            print(curr, prev)
        
        return True



