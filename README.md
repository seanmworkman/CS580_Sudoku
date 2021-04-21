# CS580_Sudoku
This program implements a Naive Backtacking Algorithm and a Smart Backtracking Algorithm to solve a Sudoku puzzle.

To run with output in the terminal:
- Run `python3 sudoku.py NBA` for Naive Backtracking Algorithm
- Run `python3 sudoku.py SBA` for Smart Backtracking Algorithm

To run with output in a txt file:
- Run `python3 sudoku.py NBA > nba_output.txt` for Naive Backtracking Algorithm
- Run `python3 sudoku.py SBA > sba_output.txt` for Smart Backtracking Algorithm

Options:
- Add `--quiet` to any of the above commands for a quiet run, this means each state will not be printed only the end result described below
- Example: `python3 sudoku.py NBA --quiet > nba_output.txt` `python3 sudoku.py NBA --quiet`

The end result will be `SUCCESS` or `FAILURE` followed by the elapsed time of the search

## Sudoku Rules
Puzzle is not solved if:
- Any row contains more than one of the same number from 1 to 9
- Any column contains more than one of the same number from 1 to 9
- Any 3x3 grid contains more than one of the same number from 1 to 9
