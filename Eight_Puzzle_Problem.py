import heapq
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, g=0, h=0):
        """
        Initialize a new PuzzleNode object.

        :param state: list, current state of the puzzle
        :param parent: PuzzleNode, parent node of the current node
        :param g: int, cost to reach the current node from the start node
        :param h: int, heuristic estimate of the cost to reach the goal from the current node
        """
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def __lt__(self, other):
        """
        Compare the total cost (g + h) of the current node with another node.

        :param other: PuzzleNode, another node to compare with
        :return: bool, True if the total cost of the current node is less than the other node
        """
        return (self.g + self.h) < (other.g + other.h)

def manhattan_distance(state):
    """
    Calculate the Manhattan distance of a given state.

    :param state: list, current state of the puzzle
    :return: int, Manhattan distance of the given state
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j]!= 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_blank_position(state):
    """
    Find the position of the blank tile in the given state.

    :param state: list, current state of the puzzle
    :return: tuple, (i, j) position of the blank tile
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    """
    Generate all possible neighbors of the given state.

    :param state: list, current state of the puzzle
    :return: list, list of all possible neighbors
    """
    i, j = get_blank_position(state)
    neighbors = []
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for move in moves:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    """
    Solve the 8-puzzle problem using A* search algorithm.

    :param initial_state: list, initial state of the puzzle
    :return: list, list of states from the initial state to the goal state
    """
    start_node = PuzzleNode(initial_state, None, 0, manhattan_distance(initial_state))
    open_list = [start_node]
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(tuple(map(tuple, current_node.state)))

        for neighbor_state in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) not in closed_list:
                neighbor_node = PuzzleNode(neighbor_state, current_node, current_node.g + 1, manhattan_distance(neighbor_state))
                heapq.heappush(open_list, neighbor_node)

    return None

initial_state = [
    [2, 1, 7],
    [8, 0, 6],
    [3, 4, 5]
]

goal_state = [
    [2, 3, 4],
    [7, 0, 1],
    [8, 5, 6]
]

solution = solve_puzzle(initial_state)

if solution:
    print("Solution steps:")
    for step, state in enumerate(solution):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")