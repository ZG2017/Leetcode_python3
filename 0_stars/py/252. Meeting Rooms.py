class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        previous_end = 0
        for start, end in sorted(intervals, key=lambda x:x[0]):
            if start < previous_end:
                return False
            else:
                previous_end = end
        return True
