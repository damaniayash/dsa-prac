
def some_interval_problem(intervals):

    '''
    this overlap function will return True if there is a overlap between intervals.
    >= 0 implies that touching interval boundaries are also considered as overlapping
    We take the max of the start indices of the interval.
    We take the min of the end indices ogf the interval.
    If back - front is +ve that means there is a overlap.
    if -ve then there is no overlap.
    This overlap trick takes into account the condition when curr completely overlaps prev or vice versa.
    '''

    def overlap(curr, prev):
        front = max(curr[0], prev[0])
        back = min(curr[1], prev[1])
        return back - front >= 0
    
    '''
    We store the first value of the interval into result so that 
    we have something to initialize our prev with.
    '''
    res = [intervals[0]]

    for curr in intervals[1:]:
        prev = res[-1]
        if overlap(curr, prev):
            # do some problem specific operation
            pass
        # curr and prev intervals do not overlap so we can just add the curr interval to res.
        else:
            res.append(curr)
    
    return res