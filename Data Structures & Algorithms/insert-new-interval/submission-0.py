class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # insert the newInterval
        target = newInterval[0]
        l, r = 0, len(intervals) - 1

        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        intervals.insert(l, newInterval)

        # merge the overlapping
        merged = [intervals[0]]
        for interval in intervals[1:]:
            last_merged = merged[-1]

            if interval[0] <= last_merged[1]:
                # there is overlapping
                last_merged[1] = max(last_merged[1], interval[1])

            else:
                merged.append(interval)


        return merged