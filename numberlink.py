"""
Code written by Salman Hussain Ali
"""
import copy


class Numberlink:
    def __init__(self, state):
        self.state = state


def number_of_blankspaces(state):
    count = 0
    for row in state:
        for value in row:
            if value == '_':
                count += 1


def get_valid_neighbors(state, row, column):
    neighbors = []
    if not row - 1 < 0:
        neighbors.append([-1,0])
    if not row + 1 >= len(state):
        neighbors.append([1,0])
    if not column + 1 >= len(state):
        neighbors.append([0,1])
    if not column - 1 < 0:
        neighbors.append([0,-1])
    return neighbors


def get_moves(state, row, column):
    """
    Gets possible successor state of that index
    :param state: Current state of numberlink puzzle
    :param row: Row index
    :param column: Column index
    :return:
    """
    moves = []
    if state[row][column] == '_':
        for neighbor in get_valid_neighbors(state, row, column):
            x_cord = row + neighbor[0]
            y_cord = column + neighbor[1]
            vertical = False
            horizontal = False
            if not neighbor[0] == 0:
                vertical = True
            elif not neighbor[1] == 0:
                horizontal = True
            value = state[x_cord][y_cord]
            if value == '_':
                continue
            elif value == '-' or value == '[' or value == ']':
                if horizontal:
                    moves.append('-')
            elif value == '|':
                if vertical:
                    if x_cord - 1 < 0 or not state[x_cord - 1][column] == '_' or x_cord + 1 >= len(state):
                        moves.append('[')
                        moves.append(']')
                    else:
                        moves.append('|')
            else:
                if vertical:
                    if x_cord - 1 < 0 or not state[x_cord - 1][column] == '_':
                        moves.append('[')
                        moves.append(']')
                    else:
                        moves.append('|')
                elif horizontal:
                    moves.append('-')
    return moves


def generate_successors(state):
    successors = []
    for row in range(len(state)):
        for column in range(len(state[0])):
            moves = get_moves(state,row, column)
            #print(f"Row: {row}, Column: {column}, Value: {state[row][column]}, Moves: {moves}")
            if moves:
                for move in moves:
                    successor = copy.deepcopy(state)
                    successor[row][column] = move
                    successors.append(successor)
    return successors



if __name__ == '__main__':
    # Implementation of representation scheme from assignment 1
    puzzle = [[1,2,'_','_'],['_',1,3,'_'],[2,3,'_','_'],['_','_','_','_']]
    for successor in generate_successors(puzzle):
        for row in successor:
            print(row)
        print("-------")

