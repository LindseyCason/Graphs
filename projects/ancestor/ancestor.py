class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    s=Stack() #make a stack
    s.push(starting_node) #add initial node
    visited=list() #make visited list

    while s.size()>0:
        v=s.pop()#pop off the top
        if v not in visited:
            visited.append(v)
        # print(ancestors)
        for i in range(len(ancestors)):
            if v == ancestors[i][1]:
                s.push(ancestors[i][0])
        # print(visited)
    else:
        if len(visited) == 1:
            return -1
        else:
            return visited[-1]    