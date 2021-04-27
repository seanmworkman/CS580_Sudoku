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

## Analysis
	NBA (Easy)	SBA (Easy)	NBA (Med)	SBA (Med)	NBA (Hard)	SBA (Hard)	NBA (Evil)	SBA (Evil)
1	0.063	    0.409	    0.556	    0.552	    0.812	    0.585	    1.592	    0.317
2	0.092	    0.243	    0.947	    0.646	    0.389	    3.04	    1.665	    0.162
3	0.351	    0.312	    0.3	        0.604	    4.312	    3.361	    0.297	    0.267
4	0.502	    0.29	    0.897	    0.486	    3.264	    3.139	    1.935	    1.763
5	0.243	    0.238	    0.591	    0.454	    1.054	    1.221	    1.74	    1.879
6	0.119	    0.178	    0.625	    0.213	    0.315	    0.105	    0.227	    0.18
7	0.06	    0.147	    0.731	    0.711	    0.508	    0.836	    1.801	    0.222
8	0.256	    0.401	    0.346	    0.862	    3.987	    0.258	    1.852	    0.278
9	0.257	    0.213	    0.824	    0.63	    1.875	    3.353	    0.228	    0.2355
10	0.106	    0.391	    0.392	    0.479	    0.329	    0.187	    1.688	    1.606
AVG	0.2049	    0.2822	    0.6209	    0.5637	    1.6845	    1.6085	    1.3025	    0.69095

The Smart Backtracking Algorithm (forward-checking) algorithm outperformed the Naive Backtracking Algorithm on each puzzle except the first (easy) one.

