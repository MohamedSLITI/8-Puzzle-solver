class Stack:

    def __init__(self):
        self.list = []
        self.state = set()

    def push(self, item):
        self.list.append(item)
        self.state.add((tuple(item.list)))

    def pop(self):
        if not self.isEmpty():
            tos = self.list[-1]
            del self.list[-1]
            self.state.remove(tuple(tos.list))
            return tos
        else:
            return 0

    def isEmpty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0

    def clear_stack(self):
        self.list.clear()
        self.state.clear()
