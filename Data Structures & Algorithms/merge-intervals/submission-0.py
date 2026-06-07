class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # edge cases
        if not intervals:
            return []

        # sort the intervals
        # O(nlogn)
        intervals.sort(key=lambda x: x[0])

        # initialze
        merged = [intervals[0]]
        for curr in intervals[1:]:
            last_merged = merged[-1]

            # curr[0] is the start_bound of first interval
            # last_merged[1] is the end_bound of second interval
            if curr[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], curr[1])
            else:
                merged.append(curr)

        return merged