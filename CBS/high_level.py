from low_level_Astar import compute_cost, cbs
from queue import PriorityQueue

class CT_node:
    def __init__(self, constraints=[], solution=[],cost=0, left_child = None, right_child = None):
        self.constraints = constraints
        self.solution = solution
        self.cost = cost
        self.left_child= left_child
        self.right_child = right_child

    def get_constraints(self):
        return self.constraints
    
    def get_solution(self):
        return self.solution
    def get_cost(self):
        self.cost =0
        for _ in self.solution:
            self.cost += len(_)
            
        return self.cost
    
    def add_left(self, child_to_add):
        self.left_child = child_to_add

    def add_right(self, child_to_add):
        self.right_child = child_to_add

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def add_solution(self, solution):
        self.solution.append(solution)
    
    def add_cost(self, cost_to_add):
        self.cost += cost_to_add

    

    

class solver:
    def __init__(self,map,start,goals):
        # computes initial paths for all the bots
        self.map = map
        self.start = start
        self.goals = goals

        self.hcost = compute_cost(self.map, self.goals).hcost()
        self.paths = {}
        for i in range(len(self.start)):
            p = cbs(self.map, self.start[i],self.goals[i],self.hcost).A_star()
            self.paths[i] = p



    def generate_path(self):
        open = PriorityQueue()
        root = CT_node(solution=self.paths)
        loc_root = root
        

        open.put((root.get_cost(), len(root.get_constraints()), root))

        while not open.empty():
            p = open.get()
            sol = p[2].get_solution()












    