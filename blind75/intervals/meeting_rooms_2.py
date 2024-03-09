'''
LINTCODE

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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()

        s, e = 0, 0
        cnt, max_cnt = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                s += 1
                cnt += 1
            else:
                e += 1
                cnt -= 1
            max_cnt = max(max_cnt, cnt)
        
        return max_cnt 
                