class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        end_pointer = 0
        rooms = 0
        
        for i in range(len(intervals)):
            if starts[i] < ends[end_pointer]:
                rooms += 1
            else:
                end_pointer += 1
                
        return rooms