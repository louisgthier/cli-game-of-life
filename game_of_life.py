#!/usr/bin/env python
import os
import time
import random
from colorama import Fore, Back, Style

WIDTH = 250
HEIGHT = 65

# Create a 2D array
grid = [[random.randint(0, 1) for x in range(WIDTH)] for y in range(HEIGHT)]

#grid = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]


player_pos = [WIDTH // 2, HEIGHT // 2]

def print_grid():
    os.system('clear')
    grid_copy = [row[:] for row in grid]
    # grid_copy[player_pos[1]][player_pos[0]] = 2
    for row in grid_copy:
        for cell in row:
            if cell == 2:
                print(Fore.GREEN + 'O' + Style.RESET_ALL, end='')
            elif cell:
                print('#', end='')
            else:
                print(' ', end='')
        print()

def update_grid():
    global grid
    new_grid = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            neighbours = sum(grid[(y+i)%HEIGHT][(x+j)%WIDTH] for i in range(-1, 2) for j in range(-1, 2) if (i != 0 or j != 0))
            if cell and neighbours in [2, 3]:
                new_grid[y][x] = 1
            elif not cell and neighbours == 3:
                new_grid[y][x] = 1
    grid = new_grid

while True:
    print_grid()
    update_grid()
    time.sleep(0.1)