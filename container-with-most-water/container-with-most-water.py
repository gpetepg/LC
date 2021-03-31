class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = float("-inf")
        
        coords = []
        
        for i, v in enumerate(height):
            coords.append([i, v])
        
        start = 0
        end = len(coords) - 1
        
        while start <= end:
            l = coords[end][0] - coords[start][0]
            h = min(coords[start][1], coords[end][1])
            
            curr_water = l * h
            most_water = max(most_water, curr_water)
            
            if coords[start][1] <= coords[end][1]:
                start += 1
            else:
                end -= 1
            
        return most_water
        