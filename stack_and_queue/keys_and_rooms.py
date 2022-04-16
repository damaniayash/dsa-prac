class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        can_visit = [0 for _ in range(len(rooms))] 
        visited = set()
        can_visit[0] = 1
        self.dfs(rooms[0], can_visit, visited, rooms)
        if 0 in can_visit: return False
        else: return True
        
    def dfs(self, room, can_visit, visited, rooms):  
        # perform a DFS starting from room 0 and update can_visit as 1. If can_visit has all 1's all room can be visited 
        for i in room:
            if i not in visited:
                can_visit[i] = 1
                visited.add(i)
                self.dfs(rooms[i], can_visit, visited, rooms)