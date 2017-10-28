from state import *
from astar import *
from pair import *
from queue import PriorityQueue
from heapq import *
import sys
import os

if __name__ == '__main__':
    board = [7, 5, 10, 11, 2, 12, 4, 1, 6, 13, 3, 8, 9, 15, 0, 14]
    board1 = [13, 6, 5, 2, 0, 14, 1, 3, 11, 9, 4, 12, 10, 7, 8, 15]

    a = Astar()
    st = a.search(board)
    a.print_path(st, slp=0)
