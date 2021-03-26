class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [1] + [0] * (len(rooms) - 1)
        stack = [0]
        
        while stack:
            curr_room = stack.pop()
            for room in rooms[curr_room]:
                if not visited[room]:
                    visited[room] = True
                    stack.append(room)
                    
        return all(visited)
        