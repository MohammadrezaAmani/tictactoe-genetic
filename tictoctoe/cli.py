from ._consts import Consts
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

    @property
    def genetic_algo(self) -> GeneticAlgorithm:
        """
        Returns:
            GeneticAlgorithm: The genetic algorithm used for opponent moves.
        """
        return self._genetic_algo
    
    @genetic_algo.setter
    def genetic_algo(self, genetic_algo: GeneticAlgorithm) -> None:
        """
        Args:
            genetic_algo (GeneticAlgorithm): The genetic algorithm used for opponent moves.
        """
        if not isinstance(genetic_algo, GeneticAlgorithm):
            raise TypeError(
                Consts.GeneticAlgoTypeError % type(genetic_algo).__name__
            )
        self._genetic_algo = genetic_algo
        
    def print_board(self) -> None:
        """
        Prints the current state of the game board.
        """
        for i in range(0, 9, 3):
            print(
                Consts.Ydelemeter.join(
                    map(
                        lambda x: Consts.Player1
                        if x == 1
                        else Consts.Player2
                        if x == -1
                        else " ",
                        self.board[i : i + 3],
                    )
                )
            )
            if i < 6:
                print(Consts.Xdelemeter)

    def is_board_full(self) -> bool:
        """
        Checks if the game board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != 0 for cell in self.board)

    def get_human_move(self, name: str) -> int:
        """
        Prompts the user for their move and returns it.

        Returns:
            int: The index of the chosen move.
        """
        while True:
            try:
                move = int(input(Consts.PlayerInput % name))
                if 1 <= move <= 9 and self.board[move - 1] == 0:
                    return move - 1
                else:
                    print(Consts.InvalidMoveMessage)
            except ValueError:
                print(Consts.InvalidInputMessage)

    def play(self, with_ai: bool = True) -> None:
        """
        Starts the game loop.
        """
        while True:
            self.print_board()
            human_move = self.get_human_move(Consts.Player1)
            self.board[human_move] = 1

            if self.genetic_algo.check_winner(self.board, 1):
                self.print_board()
                print(
                    Consts.PlayerWinsMessage % Consts.Player1
                    if not with_ai
                    else Consts.YouWinMessage
                )
                break

            if self.is_board_full():
                self.print_board()
                print(Consts.DrawMessage)
                break
            if not with_ai:
                self.print_board()
                human_move = self.get_human_move(Consts.Player2)
                self.board[human_move] = -1

                if self.genetic_algo.check_winner(self.board, -1):
                    print(Consts.PlayerWinsMessage % Consts.Player2)
                    break
                continue
            opponent_move = self.genetic_algo.genetic_algorithm(
                current_board=self.board,
            )
            self.board[opponent_move] = -1

            if self.genetic_algo.check_winner(self.board, -1):
                self.print_board()
                print(Consts.AIWinsMessage)
                break
