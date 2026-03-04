from high_level import CBS

class MyCBS:

    def __init__(self, config):
        self.config = config
        self.paths = None
        self.step_id = 0
        self.runtime = 0

    def act(self, obs, dones, info):

        if self.paths is None:

            grid = info["global_map"].tolist()
            starts = info["starts"]
            goals = info["goals"]

            solver = CBS(grid, starts, goals)
            self.paths = solver.search()
            self.runtime = solver.runtime
            self.step_id = 0

        actions = []

        for agent_id in range(len(obs)):
            path = self.paths[agent_id]

            if self.step_id + 1 < len(path):
                curr = path[self.step_id]
                nxt = path[self.step_id + 1]
            else:
                curr = path[-1]
                nxt = path[-1]

            dx = nxt[0] - curr[0]
            dy = nxt[1] - curr[1]

            if dx == -1: action = 0
            elif dx == 1: action = 1
            elif dy == -1: action = 2
            elif dy == 1: action = 3
            else: action = 4

            actions.append(action)

        self.step_id += 1
        return actions