class check_conflicts:
    def __init__(self, solution):
        self.solution = solution
        self.conflicts = []
        self.max_len = -1
        for it in self.solution:
            self.max_len = max(self.max_len , len(it))

    def solve(self):
        for i in range(self.max_len):
            mp = {}
            for j in range(len(self.solution)):
                if len(self.solution[j]) > i:
                    if self.solution[j][i] in mp:
                        self.conflicts.append((mp[self.solution[j][i]], j,self.solution[j][i] ))
                        return self.conflicts
                    else:
                        mp[self.solution[j][i]] = j
            
            return None
                    
