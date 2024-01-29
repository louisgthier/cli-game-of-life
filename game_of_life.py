#!/usr/bin/env python
import os
import time
import random
from colorama import Fore, Back, Style
import keyboard

WIDTH = 50
HEIGHT = 25

# Create a 2D array
grid = [[random.randint(0, 1) for x in range(WIDTH)] for y in range(HEIGHT)]

player_pos = [HEIGHT // 2, WIDTH // 2]

for i in range(HEIGHT//2 - 5, HEIGHT//2 + 5):
    for j in range(WIDTH//2 - 5, WIDTH//2 + 5):
        grid[i][j] = 0

def print_grid():
    os.system('clear')
    grid_copy = [row[:] for row in grid]
    grid_copy[player_pos[0]][player_pos[1]] = 2

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

def move_player(key):
    if key.name == 'up':
        player_pos[0] = max(0, player_pos[0] - 1)
    elif key.name == 'down':
        player_pos[0] = min(HEIGHT - 1, player_pos[0] + 1)
    elif key.name == 'left':
        player_pos[1] = max(0, player_pos[1] - 1)
    elif key.name == 'right':
        player_pos[1] = min(WIDTH - 1, player_pos[1] + 1)

def place_remove_cell(key):
    grid[player_pos[0]][player_pos[1]] = (grid[player_pos[0]][player_pos[1]] + 1) % 2

def reset_grid(key):
    global grid
    if key.name == 'r':
        grid = [[random.randint(0, 1) for x in range(WIDTH)] for y in range(HEIGHT)]
    elif key.name == 'c':
        grid = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]


paused = False

def pause_and_play(key):
    global paused
    paused = not paused

keyboard.on_press_key("up", move_player)
keyboard.on_press_key("down", move_player)
keyboard.on_press_key("left", move_player)
keyboard.on_press_key("right", move_player)
keyboard.on_press_key("space", place_remove_cell)
keyboard.on_press_key("r", reset_grid)
keyboard.on_press_key("c", reset_grid)
keyboard.on_press_key("esc", exit)
keyboard.on_press_key("p", pause_and_play)

last_step = time.time()
while True:
    print_grid()
    if last_step + 0.5 < time.time() and not paused:
        update_grid()
        last_step = time.time()
    time.sleep(0.05)
    