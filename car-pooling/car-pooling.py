class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = 0
        stops = []
        for i in trips:
            stops.append((i[1], i[0]))
            stops.append((i[2], -i[0]))
            
        stops = sorted(stops)
        
        for i in stops:
            passengers += i[1]
            if passengers > capacity:
                return False
            
        return True