import sys
import time

import taqqin
import stack
import queue

goal_list = [1, 2, 3, 8, 0, 4, 7, 6, 5]


def dfs_search(begin_state, zero_pos):
    print("-----------------------depth first search--------------------------")
    puzzle_state = taqqin.Taqqin(begin_state, zero_pos)
    stck = stack.Stack()

    depth_limit = 25
    i = 0
    explored = set()
    stck.push(puzzle_state)
    state = puzzle_state
    t = time.time()
    while (state.cost < depth_limit) or (not stck.isEmpty()):
        state = stck.pop()
        print("iteration : ", i)
        print(state.list)
        explored.add(tuple(state.list))

        if state.list == goal_list:
            print("\n=========GOAL REACHED=========")
            duration = time.time() - t
            print("\n=========Problem Solved in:", duration, " seconds=========")
            write_to_file(state, i, duration, "depth first search")
            return 1

        children = []
        children.extend(state.expand())
        children.reverse()

        if state.cost < depth_limit:
            for states in children:
                if tuple(states.list) not in (explored.union(stck.state)):
                    stck.push(states)

        i = i + 1


def bfs_search(begin_state, zero_pos):
    print("------------------------breadth first search----------------------------")
    puzzle_state = taqqin.Taqqin(begin_state, zero_pos)

    q = queue.Queue()
    q.enqueue(puzzle_state)
    explored = set()  # to store already explored puzzle lists
    i = 0
    t = time.time()
    while not q.isEmpty():
        state = q.dequeue()
        print("iteration : ", i)
        print(state.list)
        explored.add(tuple(state.list))

        if state.list == goal_list:
            print("\n=========GOAL REACHED=========")
            duration = time.time() - t
            print("\n=========Problem Solved in:", duration, "seconds=========")
            write_to_file(state, i, duration, "breadth first search")
            return 1

        children = state.expand()
        for states in children:
            if tuple(states.list) not in (explored.union(q.state)):
                q.enqueue(states)
        i = i + 1


def write_to_file(state, i, duration, string):
    cost = "path_cost : " + str(state.cost)
    nodes = "nodes_expanded :" + str(i)
    action_list = []
    for i in range(state.cost):
        action_list.append(state.action)
        state = state.parent
    action_list.reverse()

    Text = [cost + "\n", nodes + "\n"]
    with open(f"{string}search_details.txt", "w") as file1:

        file1.write("Search technique = " + string + "\n")
        file1.write("Problem solved in " + str(duration) + "seconds" + "\n")
        for line in Text:
            file1.write(line)
        file1.write("action = [ ")
        for each in action_list:
            file1.write(each + ", ")
        file1.write("]")


def main():
    begin_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    begin_state = list(map(int, begin_state))

    if not len(begin_state) == 9:
        print("Error: enter 9 numbers in arg2")
        sys.exit()
    zero_pos = None
    for i, state in enumerate(begin_state):
        if state == 0:
            zero_pos = i

    bfs_search(begin_state, zero_pos)
    dfs_search(begin_state, zero_pos)


if __name__ == '__main__':
    main()
