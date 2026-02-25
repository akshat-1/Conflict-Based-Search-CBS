from queue import Queue, PriorityQueue

class compute_cost:
    def __init__(self, map, goals, obstacle = 0):
        #goals = list of tuples with all goal coordinates
        #map = map with obstacle with self.obstacle 
        self.map = map
        self.goals = goals
        self.move = [(-1,0), (0,-1), (0,1), (1,0)] 
        self.n = len(map)
        self.m = len(map[0])
        self.obstacle = obstacle


    def check( x,y,n,m):
        return x<n and y<m and x>=0 and y>=0

    def hcost(self):
        ans= {}
        for it in self.goals:
            cst = [[float('inf') if cell == self.obstacle else 0 for cell in row]for row in self.map]
            if cst[it[0]][it[1]] == float('inf'):
                ans[it] = None
                continue
            

            #BFS to get min cost from each cell to goal
            q = Queue()
            q.put((0, it))
            vis = [[True if cell == self.obstacle else False for cell in row]for row in self.map]
            while not q.empty():
                top = q.get()
                c = top[0]
                node = top[1]

                vis[node[0]][node[1]] = True

                for mv in self.move:
                    if compute_cost.check(node[0] + mv[0] , node[1] + mv[1], self.n,self.m) and not vis[node[0] + mv[0]][node[1] + mv[1]]:
                        cst[node[0] + mv[0]][node[1]+mv[1]] = c + 1
                        q.put((c+1, (node[0] + mv[0] , node[1] + mv[1])))
                
            ans[it] = cst

        
        return ans


class cbs:
    def __init__(self, map, start, goal, hcost, obstacle):
        # start = curr location of bot
        # hcost = dict of hcost for all bots
        self.map = map
        self.start = start
        self.goal = goal
        self.move = [(-1,0), (0,-1), (0,1), (1,0)]
        self.hcost = hcost
        self.obstacle = obstacle

        self.cost = self.hcost[self.goal]



    def sic(self): #heuristics
        cst = self.hcost[self.goal]
        if cst == None:
            return None
        
        return cst[self.start[0]][self.start[1]]
    
    def get_neighbors(self, node):
        x, y = node
        neighbors = []
        for dx, dy in self.move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.map.shape[0] and 0 <= ny < self.map.shape[1] and self.map[nx, ny] != self.obstacle:
                neighbors.append((nx, ny))
        return neighbors
    
    def A_star(self):
        path = [] 
        pq = PriorityQueue()
        pq.put((0,self.start))
        c_f = {}
        cst = {}
        
        c_f[self.start] = None
        cst[self.start] = 0
        

        while not pq.empty():
            
            _, node = pq.get()
            
            if node == self.goal:
                break
            
            for ngh in cbs.get_neighbors( node):
                c = cst[node] +1
                
                
                if ngh not in cst or c < cst[ngh]:
                    cst[ngh] = c
                    
                    h = self.cost[ngh[0]][ngh[1]]
                    f = c + h
                    
                    pq.put((f, ngh))
                    c_f[ngh] = node
                        
           
                    
        par = self.goal
        
        if par not in c_f:
            return []
            
        while par is not None:
            path.append(par)
            par = c_f[par]
            
        path.reverse()
        
        return path



        