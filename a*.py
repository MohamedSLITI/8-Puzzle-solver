import time


class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        x, y = self.find(self.data, '0')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, taq, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_taq = self.copy(taq)
            temp = temp_taq[x2][y2]
            temp_taq[x2][y2] = temp_taq[x1][y1]
            temp_taq[x1][y1] = temp
            return temp_taq
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, taq, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if taq[i][j] == x:
                    return i, j


class Taqqin:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '0':
                    temp += 1
        return temp

    def process(self):
        start = [["2", "8", "3"], ["1", "6", "4"], ["7", "0", "5"]]
        goal = [["1", "2", "3"], ["8", "0", "4"], ["7", "6", "5"]]

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)
        print("\n\n")
        count = 0
        t = time.time()
        while True:
            count += 1
            cur = self.open[0]
            print("itération", count, "\n ----------------------")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if self.h(cur.data, goal) == 0:
                print('problem solved in ', time.time() - t, "seconds \n ------------------------------")
                with open(f"A* search_details.txt", "w") as file1:
                    file1.write("Search technique = A* \n")
                    file1.write('Problem solved in ' + str(time.time() - t) + "seconds \n")
                    file1.write("path_cost" + str(start.fval) + "\n")
                    file1.write("nodes_expanded " + str(len(self.open)) + "\n")
                break
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            """ sort the opne list based on f value """
            self.open.sort(key=lambda x: x.fval, reverse=False)


T = Taqqin(3)
T.process()
