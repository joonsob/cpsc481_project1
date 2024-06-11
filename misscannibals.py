from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def result(self, state, action):
        m, c, onLeft = state
        new_m, new_c = m, c
        if onLeft:
            if 'M' in action:
                new_m -= action.count('M')
            if 'C' in action:
                new_c -= action.count('C')
        else:
            if 'M' in action:
                new_m += action.count('M')
            if 'C' in action:
                new_c += action.count('C')
        return (new_m, new_c, not onLeft)

    def actions(self, state):
        actions = ['MM', 'MC', 'CC', 'M', 'C']
        m, c, onLeft = state
        valid_actions = []
        for action in actions:
            new_m, new_c = m, c
            if onLeft:
                if 'M' in action:
                    new_m -= action.count('M')
                if 'C' in action:
                    new_c -= action.count('C')
            else:
                if 'M' in action:
                    new_m += action.count('M')
                if 'C' in action:
                    new_c += action.count('C')
            new_state = (new_m, new_c, not onLeft)
            if self.is_valid_state(new_state):
                valid_actions.append(action)
        return valid_actions

    def is_valid_state(self, state):
        m, c, _ = state
        if m < 0 or c < 0 or m > self.M or c > self.C:
            return False
        if m > 0 and m < c:
            return False
        if self.M - m > 0 and self.M - m < self.C - c:
            return False
        return True

    def goal_test(self, state):
        return state == self.goal

if __name__ == '__main__':
    mc = MissCannibals(3, 3)
    # Test your code as you develop! This should return ['CC', 'C', 'M']
    print(mc.actions((3, 2, True)))
    
    path = depth_first_graph_search(mc).solution() # type: ignore
    print(path)
    
    path = breadth_first_graph_search(mc).solution() # type: ignore
    print(path)
