# Tic Tac Toe - Genetic Algorithm

**Introduction:**

This project is a simple command-line implementation of the classic Tic Tac Toe game using Python. _(The [GUI](./tictoctoe/gui.py) version contains some minor bugs, that's why we don't use it and stick to the CLI version)_.

**Table of Contents:**

1. [Usage](#usage)
2. [Game Rules](#game-rules)
3. [License](#license)

---

## Usage

You can use this code from both CLI and Script Environments.

### From CLI

To play the Tic-Tac-Toe game from the command line, use the following command:

```bash
python -m tictactoe
```

#### Command-Line Arguments

- `-v`, `--version`: Display the version information.
- `-p`, `--population`: Set the population size (default: 50).
- `-g`, `--generations`: Set the number of generations (default: 50).
- `-m`, `--mutation`: Set the mutation rate (default: 0.1).
- `-a`, `--ai`: Enable AI mode.

#### Examples

##### Play with AI

```bash
python -m tictoctoe -a
```

##### Configure Game Parameters

```bash
python -m tictoctoe -a -p 30 -g 100 -m 0.05
```

### From Python Code

To start the game, run the following command in the terminal:

```bash
python main.py
```

or

```python
from tictoctoe.cli import TicTacToeGame
from tictoctoe.genetic import GeneticAlgorithm

game = TicTacToeGame()
game.genetic_algo = GeneticAlgorithm(
    population=50, generations=50, mutation_rate=0.1
    )
game.play(with_ai=True)
```

## Game Rules

The game follows standard Tic Tac Toe rules:

- The board consists of a 3x3 grid.
- Players take turns marking an empty cell with their symbol (X or O).
- The game ends when one player has three of their symbols in a row (horizontally, vertically, or diagonally) or when the board is full (a draw).

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Mohammadreza Amani
