"""
Code written by Salman Hussain Ali
"""
import copy
import hashlib


def manhattan(puzzle):  # Ordinary manhattan distance
    """
    Calculates the heuristic value of the puzzle's state. It uses a classic Manhattan distance heuristic
    :param puzzle: Puzzle state for which heuristic is to be calculated
    :return: Total distance by which the values are out of place
    """
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            num = puzzle[i][j]
            row = int((num - 1)/ 3)
            column = (num - 1) % 3

            if num == 0:
                continue

            if row == i and column == j:
                continue

            distance = abs(row - i) + abs(column - j)
            total += distance
    return total


def hamming(puzzle):  # Hamming distance
    """
    Calculates the heuristic value of the puzzle's state. It calculates the number of tiles out of place
    :param puzzle: Puzzle state for which heuristic is to be calculated
    :return: Total distance by which the values are out of place
    """
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            num = puzzle[i][j]
            row = int((num - 1)/ 3)
            column = (num - 1) % 3

            if num == 0:
                continue

            if row == i and column == j:
                continue

            total += 1
    return total


def permutation_inversion(puzzle):
    """
    Sum of permutation inversions
    :param puzzle: Puzzle state for which heuristic is to be calculated
    :return: For each numbered tile, count how many tiles on its right should be on its left in the goal state, and returns the sum
    """
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            value = puzzle[i][j]
            index = (3*i) + j
            while index < 9:
                row = int(index/3)
                column = index % 3
                if puzzle[row][column] < value and not puzzle[row][column] == 0:
                    total += 1
                index += 1
    return total


def manhattan_linear_conflict(puzzle):
    """
    Calculates the heuristic value of the puzzle's state. It uses a Manhattan distance heuristic with linear conflict
    :param puzzle: Puzzle state for which heuristic is to be calculated
    :return: Total distance by which the values are out of place, including linear conflicts
    """
    size = len(puzzle)
    manhattan_distance = 0
    linear_conflict = 0

    for i in range(size):
        for j in range(size):
            value = puzzle[i][j]
            if value == 0:
                continue
            goal_i = (value - 1) // size
            goal_j = (value - 1) % size
            manhattan_distance += abs(i - goal_i) + abs(j - goal_j)

            if i == goal_i:
                for k in range(j + 1, size):
                    v = puzzle[i][k]
                    if v == 0:
                        continue
                    goal_j_k = (v - 1) % size
                    if goal_j_k < goal_j:
                        linear_conflict += 1

            if j == goal_j:
                for k in range(i + 1, size):
                    v = puzzle[k][j]
                    if v == 0:
                        continue
                    goal_i_k = (v - 1) // size
                    if goal_i_k < goal_i:
                        linear_conflict += 1

    return manhattan_distance + 2 * linear_conflict


def is_goal_state(puzzle):
    """
    Checks if the puzzle is completed
    :param puzzle: 2-D Matrix containing the puzzle state
    :return: True if the puzzle is solved. False otherwise
    """
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    if puzzle == goal:
        return True
    else:
        return False


def puzzle_solver(puzzle, method,heuristic): #TODO - implement
    """
    Main puzzle solving method
    :param method:
    :param puzzle: Initial state of 8 puzzle
    :param heuristic: Heuristic function passed as a parameter
    :return: Finished 8 puzzle
    """
    while not is_goal_state(puzzle):
        print()


def printPuzzle(puzzle):
    for i in range(len(puzzle)):
        line = ""
        for j in range(len(puzzle[0])):
            line += str(puzzle[i][j]) + " "
        print(line)


def find_blank(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle)):
            if puzzle[x][y] == 0:
                return [x,y]


def is_corner_tile(location):
    x = location[0]
    y = location[1]
    if x == 0 or x == 2:
        if y == 0 or y == 2:
            return True
    return False


def get_moves(location):
    """
    Method that returns the list of possible moves from the blank tile's current position
    :param location: Current position of blank space
    :return: List of numbers: Symbolizes which direction the blank tile will be moved. 1- up, 2 - down, 3 - left, 4 - right
    """
    x = location[0]
    y = location[1]
    out = []

    if not x - 1 < 0:
        out.append(1)
    if not x + 1 >= 3:
        out.append(2)
    if not y - 1 < 0:
        out.append(3)
    if not y + 1 >= len(matrix[0]):
        out.append(4)
    return out


def generate_successors(puzzle):
    """
    Returns a successor state for the puzzle
    :param puzzle: Matrix for which successor state is to be generated
    :param num: Symbolizes which direction the blank tile will be moved. 1- up, 2 - down, 3 - left, 4 - right
    :return:
    """
    position = find_blank(puzzle)
    moves = get_moves(position)

    row = position[0]
    column = position[1]

    states = []

    for move in moves:
        result = copy.deepcopy(puzzle)

        if move == 1:
            temp = result[row -1][column]
            result[row][column] = temp
            result[row - 1][column] = 0
        elif move == 2:
            temp = result[row + 1][column]
            result[row][column] = temp
            result[row + 1][column] = 0
        elif move == 3:
            temp = result[row][column - 1]
            result[row][column] = temp
            result[row][column - 1] = 0
        elif move == 4:
            temp = result[row][column + 1]
            result[row][column] = temp
            result[row][column + 1] = 0
        states.append(result)

    return states


def hashcode(puzzle):
    # count = 0
    # result = 0
    # for row in puzzle:
    #     for value in row:
    #         result += value * (2 ** count)
    #         count += 1
    #
    # return result
    flattened_list = [str(value) for row in puzzle for value in row]
    flattened_str = "".join(flattened_list)
    hashcode = hashlib.sha256(flattened_str.encode()).hexdigest()
    return hashcode


class Node:
    def __init__(self, state, parent):
        self.state = state
        self.cost = 0
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.hashcode = hashcode(state)
        self.parent = parent


class PriorityQueue(Node):
    def __init__(self):
        self.queue = []

    def getSize(self):
        return len(self.queue)

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop(self):
        try:
            min_val = 0
            for i in range(len(self.queue)):
                if self.queue[i].cost < self.queue[min_val].cost:
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print()
            exit()


def best_first_search(puzzle, heuristic):
    """
        Best first search
        :param puzzle: Initial state of puzzle
        :param heuristic: Heuristic function
        :return: 1) Node object which contains: the goal state and a pointer to its parent node. 2) Length of path taken
        """
    node = Node(puzzle, None)
    frontier = PriorityQueue()
    frontier.insert(node)
    reached = set()

    count = 1

    while not frontier.isEmpty():
        node = frontier.pop()
        if is_goal_state(node.state):
            return [node,count]
        reached.add(tuple(map(tuple, node.state)))
        count += 1
        for matrix in generate_successors(node.state):
            if tuple(tuple(map(tuple, matrix))) not in reached:
                successor = Node(matrix, node)
                successor.cost = heuristic(successor.state)
                frontier.insert(successor)
    return None


def breadth_first_search(puzzle):
    """
        Breadth first search
        :param puzzle: Initial state of puzzle
        :return: 1) Node object which contains: the goal state and a pointer to its parent node
        """
    node = Node(puzzle, None)
    if is_goal_state(puzzle):
        return node
    frontier = []
    frontier.append(node)
    reached = {}
    while not len(frontier) == 0:
        node = frontier.pop(0)
        for matrix in generate_successors(node.state):
            successor = Node(matrix, node)
            successor.cost = node.cost + 1
            if is_goal_state(matrix):
                return successor
            if successor.hashcode not in reached:
                reached[successor.hashcode] = successor
                frontier.append(successor)
    return None


def depth_first_search(puzzle):
    """
        Depth first search
        :param puzzle: Initial state of puzzle
        :return: Node object which contains: the goal state and a pointer to its parent node
        """
    node = Node(puzzle, None)
    if is_goal_state(puzzle):
        return node
    frontier = []
    frontier.append(node)
    reached = {}
    while not len(frontier) == 0:
        node = frontier.pop(len(frontier)-1)
        if is_goal_state(node.state):
            return node
        for matrix in generate_successors(node.state):
            successor = Node(matrix, node)
            successor.cost = node.cost + 1
            if successor.hashcode not in reached:
                frontier.append(successor)
        reached[node.hashcode] = node
    return None


def a_star_search(puzzle, heuristic):
    """
    A star search
    :param puzzle: Initial state of puzzle
    :param heuristic: Heuristic function
    :return: 1) Node object which contains: the goal state and a pointer to its parent node. 2) Length of path taken
    """
    node = Node(puzzle, None)
    node.depth = 0
    frontier = PriorityQueue()
    frontier.insert(node)
    reached = set()

    count = 1

    while not frontier.isEmpty():
        node = frontier.pop()
        if is_goal_state(node.state):
            return [node,count]
        reached.add(tuple(map(tuple, node.state)))
        count += 1
        for matrix in generate_successors(node.state):
            if tuple(tuple(map(tuple, matrix))) not in reached:
                successor = Node(matrix, node)
                successor.cost = heuristic(successor.state) + successor.depth
                frontier.insert(successor)
    return None


def length_path(goal_node):
    """
    Returns the length of the path taken to the solution
    :param goal_node: Goal node returned by the search algorithms
    :return: Length of path taken
    """
    depth = 0

    node = goal_node
    while node.parent:
        depth += 1
        node = node.parent
    return depth


if __name__ == '__main__':
    challenge = [[4,1,3],[7,0,5],[8,2,6]]

    #print(breadth_first_search(matrix))

    print(best_first_search(challenge, manhattan)[1])

    print(a_star_search(challenge, manhattan)[1])

    #print(depth_first_search(matrix))