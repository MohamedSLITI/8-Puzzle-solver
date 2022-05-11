class Queue:
    def __init__(self):
        self.list=[]
        self.state = set()
        
    def enqueue(self,item):
        self.list.append(item)
        self.state.add((tuple(item.list)))
        
    def dequeue(self):
        if not self.isEmpty():
            item = self.list[0]
            for i in range(len(self.list)-1):
                self.list[i] = self.list[i+1]
            del self.list[-1]
            self.state.remove(tuple(item.list))
            return item
        
    def isEmpty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0