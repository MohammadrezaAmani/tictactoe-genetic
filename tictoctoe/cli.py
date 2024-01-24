from .genetic import GeneticAlgorithm


class TicTacToeGame:
    """
    Represents a Tic-Tac-Toe game.

    Attributes:
        board (list): The current state of the game board.
        genetic_algo (GeneticAlgorithm): The genetic algorithm used for opponent moves.

    Methods:
        print_board(): Prints the current state of the game board.
        is_board_full(): Checks if the game board is full.
        get_human_move(): Prompts the user for their move and returns it.
        play(): Starts the game loop.
    """

    def __init__(self) -> None:
        self.board = [0] * 9
        self.genetic_algo = GeneticAlgorithm()

    def print_board(self) -> None:
        """
        Prints the current state of the game board.
        """
        for i in range(0, 9, 3):
            print(
                " | ".join(
                    map(
                        lambda x: "X" if x == 1 else "O" if x == -1 else " ",
                        self.board[i : i + 3],
                    )
                )
            )
            if i < 6:
                print("---------")

    def is_board_full(self) -> bool:
        """
        Checks if the game board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != 0 for cell in self.board)

    def get_human_move(self) -> int:
        """
        Prompts the user for their move and returns it.

        Returns:
            int: The index of the chosen move.
        """
        while True:
            try:
                move = int(input("Enter your move (1-9): "))
                if 1 <= move <= 9 and self.board[move - 1] == 0:
                    return move - 1
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self, population_size: int = 50, generations: int = 50) -> None:
        """
        Starts the game loop.
        """
        while True:
            self.print_board()

            human_move = self.get_human_move()
            self.board[human_move] = 1

            if self.genetic_algo.check_winner(self.board, 1):
                self.print_board()
                print("You win! Congratulations!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

            opponent_move = self.genetic_algo.genetic_algorithm(
                population_size=population_size,
                generations=generations,
                current_board=self.board,
            )
            self.board[opponent_move] = -1

            if self.genetic_algo.check_winner(self.board, -1):
                self.print_board()
                print("You lose! Better luck next time.")
                break
