class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        
        end_counter = 0
        rooms = 0
        
        for i in range(len(intervals)):
            if starts[i] < ends[end_counter]:
                rooms += 1
            else:
                end_counter += 1
            
        return rooms