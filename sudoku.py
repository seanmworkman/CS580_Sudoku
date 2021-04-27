#!/usr/bin/env python3
from copy import deepcopy
import time
import sys
import random

quiet = False

# Helper funciton to print the state in a readable order
def printState(state):
    print('------------')
    for i in state:
        print(i)
    print('------------')

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

# Finds an empty location (0) and returns the location
# If no empty locations return (-1, -1)
def findEmpty(puzzle):
    position = (-1, -1)
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                position = (i, j)
                return position
    return position


# Helper function to generate random list of values 1-9
def generateRandomList():
    values = random.sample(range(1, 10), 9)
    return values

# Generate a dictionary with 
def generateFCDict(puzzle):
    fcDict = {}
    emptyLocs = []
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                emptyLocs.append((i, j))
    
    randList = []
    for i in emptyLocs:
        randList = generateRandomList()
        # fcDict[i] = randList
        fcDict[i] = []
        for j in randList:
            if doesValueWork(puzzle, j, i):
                fcDict[i].append(j)
    return fcDict


# Implement a naïve backtracking algorithm. The selection of variables and 
# assignment of values can be done either in order or randomly.
def nba(puzzle):
    if not quiet:
        printState(puzzle)

    # Set an arbitrary location
    position = (-1, -1)
    
    # if no empty locations, the puzzle is solved
    position = findEmpty(puzzle)
    if position[0] == -1:
        return True
    
    # Generate list of random values 1-9 to be tried 
    randomVals = generateRandomList()
    for val in randomVals:
        # Check if the value works in the specified position
        if doesValueWork(puzzle, val, position):
            # Set the position to the val
            puzzle[position[0]][position[1]] = val

            # Success
            if nba(puzzle):
                printState(puzzle)
                return True

            # Failure, revert puzzle
            puzzle[position[0]][position[1]] = 0

    # Backtrack
    return False

# Incorporate at least one strategy of minimum remaining values (MRV), 
# least constraining value (LCV), and forward checking in your backtracking algorithm.
def sba(puzzle):
    if not quiet:
        printState(puzzle)

    # Generate dictionary for forward-checking
    fcDict = generateFCDict(puzzle)
    # Set an arbitrary location
    position = (-1, -1)
    
    # if no empty locations, the puzzle is solved
    position = findEmpty(puzzle)

    if position[0] == -1:
        return True

    # Instead of random values use the values from the forward checking dictionary
    remainingVals = fcDict[position]

    for val in remainingVals:
        # Check if the value works in the specified position
        if doesValueWork(puzzle, val, position):
            # Set the position to the val
            puzzle[position[0]][position[1]] = val

            # Success
            if nba(puzzle):
                printState(puzzle)
                return True

            # Failure, revert puzzle
            puzzle[position[0]][position[1]] = 0

    # Backtrack
    return False

# Parses Sudoku.txt
def parseInput():
    f = open("Sudoku.txt", "r")
    # f = open("SudokuMedium.txt", "r")
    # f = open("SudokuHard.txt", "r")
    # f = open("SudokuEvil.txt", "r")
    # Read the first line to remove the title line ('Sudoku 01')
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
    # printState(puzzle)
    if mode.lower() == "nba":
        start_time = time.time()
        if nba(puzzle):
            printState(puzzle)
            print("SUCCESS")
        else:
            print("FAILURE, NO SOLUTION")
        elapsed_time = time.time() - start_time
        print('Naive Backtracking Algorithm finished in {}'.format(elapsed_time))
    else:
        start_time = time.time()
        if sba(puzzle):
            printState(puzzle)
            print("SUCCESS")
        else:
            print("FAILURE, NO SOLUTION")
        elapsed_time = time.time() - start_time
        print('Smart Backtracking Algorithm finished in {}'.format(elapsed_time))


quiet = False
if len(sys.argv) >= 3:
    if sys.argv[2] == "--quiet":
        quiet = True
solve(sys.argv[1])