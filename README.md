# Tic Tac Toe - Genetic Algorithm

**Introduction:**

This project is a simple command-line implementation of the classic Tic Tac Toe game using Python. _(The [GUI](./tictoctoe/gui.py) version contains some minor bugs, that's why we don't use it and stick to the CLI version)_.

**Table of Contents:**

1. [Usage](#usage)
2. [Game Rules](#game-rules)
3. [License](#license)

---

## Usage

To start the game, run the following command in the terminal:

```bash
python main.py
```

or

```python
from tictoctoe.cli import TicTacToeGame

game = TicTacToeGame()
game.play()
```

## Game Rules

The game follows standard Tic Tac Toe rules:

- The board consists of a 3x3 grid.
- Players take turns marking an empty cell with their symbol (X or O).
- The game ends when one player has three of their symbols in a row (horizontally, vertically, or diagonally) or when the board is full (a draw).

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
