from low_level_Astar import AStar
from CT_node import CBSNode
from conflicts import check_conflicts
from queue import PriorityQueue
import heapq
import time
from collections import defaultdict

# class high_node:
#     def __init__(self,map,start,goals):
#         # computes initial paths for all the bots
#         self.map = map
#         self.start = start
#         self.goals = goals
#         self.goal_nodes = []

#         self.hcost = compute_cost(self.map, self.goals).hcost()
#         self.paths = {}
#         for i in range(len(self.start)):
#             p = cbs(self.map, self.start[i],self.goals[i],self.hcost).A_star()
#             self.paths[i] = p



#     def generate_path(self):
#         open = PriorityQueue()
#         root = CT_node(solution=self.paths)
#         loc_root = root
        

#         open.put((root.get_cost(), len(root.get_constraints()), root))

#         while not open.empty():
#             p = open.get()
#             sol = p[2].get_solution()
#             constraints = p[2].get_constraints()
#             conflicts = check_conflicts(sol).solve()
#             if conflicts is None:
#                 self.goal_nodes.append(p[2])
#             else:
#                 left_child = CT_node(constraints=constraints.append(conflicts[0][0], conflicts[0][2]), )
#                 right_child = CT_node(constraints=constraints.append(conflicts[0][1], conflicts[0][2]))
                
#                 p.add_left(left_child)
#                 p.add_right(right_child)
                

class CBS:

    def __init__(self, grid, starts, goals):
        self.grid = grid
        self.starts = starts
        self.goals = goals
        self.num_agents = len(starts)
        self.runtime = 0

    # ------------------------------
    # Conflict Detection
    # ------------------------------

    def detect_conflict(self, paths):

        max_len = max(len(p) for p in paths.values())

        for t in range(max_len):

            positions = {}

            for agent in paths:
                path = paths[agent]
                pos = path[t] if t < len(path) else path[-1]

                # Vertex conflict
                if pos in positions:
                    return {
                        "type": "vertex",
                        "agents": (agent, positions[pos]),
                        "pos": pos,
                        "time": t
                    }

                positions[pos] = agent

            # Edge conflict
            for a1 in paths:
                for a2 in paths:
                    if a1 >= a2:
                        continue

                    p1 = paths[a1]
                    p2 = paths[a2]

                    if t+1 >= len(p1) or t+1 >= len(p2):
                        continue

                    if p1[t] == p2[t+1] and p1[t+1] == p2[t]:
                        return {
                            "type": "edge",
                            "agents": (a1, a2),
                            "edge": (p1[t], p1[t+1]),
                            "time": t+1
                        }

        return None

    # ------------------------------
    # Compute Paths
    # ------------------------------

    def compute_paths(self, node):

        node.paths = {}
        node.cost = 0

        for agent in range(self.num_agents):

            astar = AStar(self.grid, node.constraints)
            path = astar.search(agent, self.starts[agent], self.goals[agent])

            if path is None:
                return False

            node.paths[agent] = path
            node.cost += len(path)

        return True

    # ------------------------------
    # CBS Search
    # ------------------------------

    def search(self):

        start_time = time.time()

        root = CBSNode()

        if not self.compute_paths(root):
            return None

        open_list = []
        heapq.heappush(open_list, (root.cost, root))

        while open_list:

            _, node = heapq.heappop(open_list)

            conflict = self.detect_conflict(node.paths)

            if conflict is None:
                self.runtime = time.time() - start_time
                return node.paths

            for agent in conflict["agents"]:

                child = CBSNode()
                child.constraints = set(node.constraints)

                if conflict["type"] == "vertex":
                    child.constraints.add(
                        (agent, conflict["pos"], conflict["time"])
                    )
                else:
                    u, v = conflict["edge"]
                    child.constraints.add(
                        (agent, u, v, conflict["time"])
                    )

                if self.compute_paths(child):
                    heapq.heappush(open_list, (child.cost, child))

        self.runtime = time.time() - start_time
        return None












    