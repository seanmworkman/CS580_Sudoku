#!/usr/bin/env python3
from copy import deepcopy
import time
import sys
import random

rows = 5
columns = 5
goal = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 0]
]

# rows = 3
# columns = 3
# goal = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0]
# ]

initial = []

quiet = False

# Helper function to determine if the current state matches the goal state
def goalTest(state):
    failCount = 0
    for i in range(rows):
        for j in range(columns):
            if state[i][j] != goal[i][j]:
                failCount += 1
    
    if failCount > 0:
        return False
    else:
        return True

# Helper function to get coordinates of empty space
def getEmptySpace(state):
    emptySpace = ()
    for i in range(rows):
        for j in range(columns):
            if state[i][j] == 0:
                emptySpace = (i, j)
                break
    return emptySpace

# Helper function to gather coordinates of neighbors of empty space
def getNeighbors(state):
    neighbors = []
    emptySpace = getEmptySpace(state)

    # Neighbor above
    if emptySpace[0] - 1 >= 0:
        neighbors.append((emptySpace[0] - 1, emptySpace[1]))

    # Neighbor below
    if emptySpace[0] + 1 < rows:
        neighbors.append((emptySpace[0] + 1, emptySpace[1]))

    # Neighbor left
    if emptySpace[1] - 1 >= 0:
        neighbors.append((emptySpace[0], emptySpace[1] - 1))

    # Neighbor right
    if emptySpace[1] + 1 < columns:
        neighbors.append((emptySpace[0], emptySpace[1] + 1))
    
    # print(neighbors)
    return neighbors

# Helper function to build options based on neighbors
def buildOptions(state):
    neighbors = getNeighbors(state)
    emptySpace = getEmptySpace(state)
    # print(emptySpace)
    options = []
    for i in neighbors:
        tempState = []
        tempState = deepcopy(state)
        tempElement = tempState[i[0]][i[1]]
        # print(i)
        tempState[emptySpace[0]][emptySpace[1]] = tempElement
        tempState[i[0]][i[1]] = 0
        options.append(tempState)
        # print(state)
    return options

# Helper funciton to determine if two states are the same
def areEqualStates(a, b):
    failCount = 0
    for i in range(rows):
        for j in range(columns):
            if a[i][j] != b[i][j]:
                failCount += 1
                break

    if failCount > 0:
        return False
    else:
        return True

# Helper function to determine if subject is in the queue
def isInQueue(q, subject):
    tempQ = Queue()
    tempQ = q
    while q.size() > 0:
        a = tempQ.removefromq()
        if areEqualStates(a, subject):
            return True
    return False

# Helper function to check is a neighbor is in a list 
def neighborInExplored(neighbor, explored):
    failCount = 0
    matches = False
    for exploredList in explored:
        failCount = 0
        for i in range(rows):
            for j in range(columns):
                if exploredList[i][j] != neighbor[i][j]:
                    failCount += 1
        
        if failCount == 0:
            matches = True
            break
    return matches

# Helper funciton to print the state in a readable order
def printState(state):
    print('------------')
    for i in state:
        print(i)
    print('------------')

# Helper function to generate initial state
def generateInitial():
    values = random.sample(range(0, (rows * columns)), (rows * columns))
    valuesIndex = 0
    result = []
    for i in range(rows):
        list1 = []
        for j in range(columns):
            list1.append(values[valuesIndex])
            valuesIndex += 1
        result.append(list1)
    return result


# Breadth First Search
# Queue: FIFO
def bfs(initial):
    # Create frontier queue
    frontier = Queue()
    explored = []
    frontierList = []

    # Add initial state to frontier
    frontier.addtoq(initial)
    frontierList.append(initial)

    # Go through the queue until it is empty
    while frontier.size() > 0:
        # Pop the element from the queue
        state = frontier.removefromq()

        # Add it to explored
        explored.append(state)

        if not quiet:
            printState(state)

        # Check if the current state is the goal state
        if goalTest(state):
            return "Success"

        # Get options from current state and neighbors
        options = buildOptions(state)

        for neighbor in options:
            tempFrontier = Queue()
            tempFrontier = deepcopy(frontier)
            if not neighborInExplored(neighbor, explored) and not neighborInExplored(neighbor, frontierList):
                frontier.addtoq(neighbor)
                frontierList.append(neighbor)       
    return "FAILURE"

# Depth First Search
# Stack: LIFO
def dfs(initial):
    # Create frontier stack
    frontier = Stack()
    explored = []
    frontierList = []
    # Add initial state to frontier
    frontier.add(initial)
    frontierList.append(initial)
    # Go through the stack until it is empty 
    while frontier.size() > 0:
        # Pop the element from the stack
        state = frontier.remove()

        # Add it to explored
        explored.append(state)

        if not quiet:
            printState(state)

        # Check if the current state is the goal state
        if goalTest(state):
            return "Success"

        # Get options from current state and neighbors
        options = buildOptions(state)
        # print(options)
        for neighbor in options:
            if not neighborInExplored(neighbor, explored) and not neighborInExplored(neighbor, frontierList):
                frontier.add(neighbor)
                frontierList.append(neighbor)
    return "FAILURE"

# Checks if the value will work in the puzzle
# p: The puzzle
# val: The value to check
# position: (x, y) coordinates of the puzzle
def doesValueWork(p, val, position):
    # Row constraint
    for i in p[position[0]]:
        if i == val:
            return False

    # Column constraint
    for i in p:
        if i[position[1]] == val:
            return False
    
    # 3x3 grid constraint
    x = int(position[0] / 3) * 3
    y = int(position[1] / 3) * 3
    if p[x][y] == val or p[x][y+1] == val or p[x][y+2] == val:
        return False
    if p[x+1][y] == val or p[x+1][y+1] == val or p[x+1][y+2] == val:
        return False
    if p[x+2][y] == val or p[x+2][y+1] == val or p[x+2][y+2] == val:
        return False

    return True

# Helper function to determine if the puzzle is solved
def isPuzzleSolved(puzzle):
    for i in puzzle:
        for j in i:
            if j == 0:
                return "FAILURE"
    return "SUCCESS"

# Helper function to determine if every number has been tried for that position
def triedAll(tried):
    if 1 in tried and 2 in tried and 3 in tried and 4 in tried and 5 in tried and 6 in tried and 7 in tried and 8 in tried and 9 in tried:
        return True
    return False

# Implement a naïve backtracking algorithm. The selection of variables and 
# assignment of values can be done either in order or randomly.
def nba(puzzle):
    # print(doesValueWork(puzzle, 2, (2, 1)))
    tried = []
    positionsFilled = []
    backtrack = False
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            works = False
            # Handle backtracking
            # print("BACKTRACK1", backtrack)
            if backtrack:
                if len(positionsFilled) == 0:
                    return "FAILURE"
                # Backtrack to the last filled position
                backPos = positionsFilled.pop()
                i = backPos[0]
                j = backPos[1]
                # print((i, j))
                position = backPos
                # print('POSITION1', position)
                tried = []
                tried.append(puzzle[i][j])
                puzzle[i][j] = 0
                backtrack = False
                # print("BACKTRACKING STATE")
                # printState(puzzle)
                # print("BACKTRACKING STATE")
            # print("BACKTRACK2", backtrack)

            # If the element is a 0 it hasn't been filled yet 
            if puzzle[i][j] == 0:
                # Store the position to track which have been filled
                position = (i, j)
                # print('POSITION2', position)
                

                # pick a random number 1 to 9
                val = random.randint(1, 9)
                # pick a random number that hasn't been tried yet
                while val in tried:
                    # If every number has been tried, backtrack
                    if triedAll(tried):
                        backtrack = True
                        break
                    val = random.randint(1, 9)
                if backtrack:
                    continue

                # Test to see if this random value works in that position
                works = doesValueWork(puzzle, val, position)
                tried.append(val)
                # Keep trying values until one works
                while not works:
                    # pick a random number that hasn't been tried yet
                    while val in tried:
                        if triedAll(tried):
                            backtrack = True
                            break
                        val = random.randint(1, 9)
                    # No more values to try so backtrack
                    if backtrack:
                        break
                    # Test to see if this random value works in that position
                    works = doesValueWork(puzzle, val, position)
                    tried.append(val)
                    # print(positionsFilled)
                    # print(tried)
                    # print("BACKTRACK", backtrack)
                # Backtrack
                if backtrack:
                    continue

                puzzle[i][j] = val
                positionsFilled.append(position)
                printState(puzzle)
                # if backtrack:
                #     break
                
            tried = []
    
    return isPuzzleSolved(puzzle)

# Incorporate at least one strategy of minimum remaining values (MRV), 
# least constraining value (LCV), and forward checking in your backtracking algorithm.
def sba(puzzle):

    return "FAILURE"

# Parses Sudoku.txt
def parseInput():
    f = open("Sudoku.txt", "r")
    # Read the first line to remove the 'Sudoku 01'
    f.readline()
    count = 0
    inputList = []
    result = []
    for i in f:
        inputList = []
        for j in i:
            # Make sure j is a real input and not a whitespace
            if not j.isspace():
                inputList.append(int(j))
        result.append(inputList)
    return result

def solve(mode):
    puzzle = parseInput()
    printState(puzzle)
    if mode.lower() == "nba":
        start_time = time.time()
        print(nba(puzzle))
        elapsed_time = time.time() - start_time
        print('Naive Backtracking Algorithm finished in {}'.format(elapsed_time))
    else:
        start_time = time.time()
        print(sba(puzzle))
        elapsed_time = time.time() - start_time
        print('Smart Backtracking Algorithm finished in {}'.format(elapsed_time))


quiet = False
if len(sys.argv) >= 3:
    if sys.argv[2] == "--quiet":
        quiet = True
solve(sys.argv[1])