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
            print(f"Number: {num}, Distance: {distance},Row:{abs(row - i)},Column:{abs(column - j)}")
    return total


def hamming(puzzle):  # Ordinary manhattan distance
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


def cornertile(puzzle):  # Ordinary manhattan distance
    """
    Calculates the heuristic value of the puzzle's state. It uses a classic Manhattan distance heuristic with additional
    corner tile costs
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
            print(f"Number: {num}, Distance: {distance},Row:{abs(row - i)},Column:{abs(column - j)}")
    return total

def finished(puzzle):
    """

    :param puzzle: 2-D Matrix containing the puzzle state
    :return: True if the puzzle is solved. False otherwise
    """
    index = 1
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if not puzzle[i][j] == index:
                if puzzle[i][j] == 0:
                    continue
                return False
            else:
                index += 1
    return True


def puzzleSolver(puzzle, heuristic):
    """
    Main puzzle solving method
    :param puzzle: Initial state of 8 puzzle
    :param heuristic: Heuristic function passed as a parameter
    :return: Finished 8 puzzle
    """
    while not finished(puzzle):
        print()


def printPuzzle(puzzle):
    for i in range(len(puzzle)):
        line = ""
        for j in range(len(puzzle[0])):
            line += str(puzzle[i][j]) + " "
        print(line)


if __name__ == '__main__':
    matrix = [[3, 0, 7], [2, 8, 1], [6, 4, 5]]

    printPuzzle(matrix)

    print(hamming(matrix))

    #print(heuristic(matrix))
