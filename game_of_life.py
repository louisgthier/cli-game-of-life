#!/usr/bin/env python
import os
import time
import random
from colorama import Fore, Back, Style
import keyboard

WIDTH = 250
HEIGHT = 65

# Create a 2D array
grid = [[random.randint(0, 1) for x in range(WIDTH)] for y in range(HEIGHT)]

#grid = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]


player_pos = [HEIGHT // 2, WIDTH // 2]

food = {(random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1)) for i in range(10)}

for i in range(HEIGHT//2 - 5, HEIGHT//2 + 5):
    for j in range(WIDTH//2 - 5, WIDTH//2 + 5):
        grid[i][j] = 0

def print_grid():
    os.system('clear')
    grid_copy = [row[:] for row in grid]
    grid_copy[player_pos[0]][player_pos[1]] = 2

    for f in food:
        grid_copy[f[0]][f[1]] = 3

    for row in grid_copy:
        for cell in row:
            if cell == 3:
                print(Fore.YELLOW + 'X' + Style.RESET_ALL, end='')
            elif cell == 2:
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

def move_player(key):
    if key.name == 'up':
        player_pos[0] = max(0, player_pos[0] - 1)
    elif key.name == 'down':
        player_pos[0] = min(HEIGHT - 1, player_pos[0] + 1)
    elif key.name == 'left':
        player_pos[1] = max(0, player_pos[1] - 1)
    elif key.name == 'right':
        player_pos[1] = min(WIDTH - 1, player_pos[1] + 1)

keyboard.on_press_key("up", move_player)
keyboard.on_press_key("down", move_player)
keyboard.on_press_key("left", move_player)
keyboard.on_press_key("right", move_player)

while True:
    print_grid()
    update_grid()
    time.sleep(0.05)