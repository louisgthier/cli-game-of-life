# cli-game-of-life
A terminal-based implementation of Conway's Game of Life.

## Description
This project is a simple implementation of Conway's Game of Life, a cellular automaton devised by the British mathematician John Horton Conway. The game is played on a grid of cells, each of which is either alive or dead. The state of the grid evolves over time according to a set of rules based on the number of live neighbors each cell has.

In this implementation, the game is played in the terminal. The grid is displayed as a matrix of characters, with '#' representing a live cell and ' ' (a space) representing a dead cell. We added a cursor that you can move around the grid using the arrow keys. The user cursor is represented by a 'O' character.

## Controls
The user can move around the grid and toggle the state of the cell they are currently on by pressing the space bar. The user can also press the 'r' key to reset the grid to a random state, or 'c' to clear the grid. Pressing the 'p' key will start the game, and pressing it again will pause the game. The user can also press the 'esc' key to quit the game. The right and left arrow keys can be used to go forward and backward in time, stepping through the game one generation at a time.

## Running the Project
To run the project, you will need Python 3 and pip installed on your machine. You will also need to install the `colorama` and `keyboard` libraries, which can be done by running `pip install colorama keyboard`.

Once the dependencies are installed, you can run the game by executing `python game_of_life.py` in the terminal. You may need to run it with administrator privileges, depending on your system. On Unix-based systems, you can do this by running `sudo python game_of_life.py`.

## Contributing
Contributions are welcome! If you have a bug to report, a feature to suggest, or a patch to contribute, please feel free to do so.

To contribute, you can fork the repository, make your changes, and then submit a pull request. Please make sure to include a detailed description of your changes.

If you're reporting a bug, please include as much information as possible about the issue, including the steps to reproduce it, the expected behavior, and the actual behavior.

If you're suggesting a feature, please provide a detailed description of the feature and why you think it would be useful.