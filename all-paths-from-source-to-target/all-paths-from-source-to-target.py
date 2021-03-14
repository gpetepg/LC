class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        
        adj_list = dict(zip([x for x in range(len(graph))], graph))
        
        n = len(graph)
        stack = [(0, [0])] 
        res = []
        while stack:
            node, path = stack.pop()
            if node == n - 1:
                res.append(path)
            for neighbor in adj_list[node]:
                stack.append((neighbor, path+[neighbor]))
        return res
    
        