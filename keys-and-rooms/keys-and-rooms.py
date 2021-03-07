class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [True] + [False] * (len(rooms) - 1)
        stack = [0]
        
        while stack:
            curr = stack.pop()
            
            for room in rooms[curr]:
                if not visited[room]:
                    visited[room] = True
                    stack.append(room)
        return all(visited)
        