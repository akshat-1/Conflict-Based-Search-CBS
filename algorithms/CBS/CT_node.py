
# class CT_node:
#     def __init__(self, constraints=[], solution=[],cost=0, left_child = None, right_child = None):
#         self.constraints = constraints
#         self.solution = solution
#         self.cost = cost
#         self.left_child= left_child
#         self.right_child = right_child

#     def get_constraints(self):
#         return self.constraints
    
#     def get_solution(self):
#         # add low level computation of paths
#         return self.solution
#     def get_cost(self):
#         self.cost =0
#         for _ in self.solution:
#             self.cost += len(_)
            
#         return self.cost
    
#     def add_left(self, child_to_add):
#         self.left_child = child_to_add

#     def add_right(self, child_to_add):
#         self.right_child = child_to_add

#     def add_constraint(self, constraint):
#         self.constraints.append(constraint)

#     def add_solution(self, solution):
#         self.solution.append(solution)
    
#     def add_cost(self, cost_to_add):
#         self.cost += cost_to_add

    
class CBSNode:

    def __init__(self):
        self.constraints = set()
        self.paths = {}
        self.cost = 0
    