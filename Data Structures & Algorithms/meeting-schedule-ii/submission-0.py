"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        free_rooms = []
        heapq.heappush(free_rooms, intervals[0].end)
        for i in range(1, len(intervals)):
            curr_start = intervals[i].start
            curr_end = intervals[i].end
            earliest_end_time = free_rooms[0]

            if curr_start >= earliest_end_time:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, curr_end)

        return len(free_rooms)
