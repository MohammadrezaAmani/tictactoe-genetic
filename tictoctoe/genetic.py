import random
from typing import List


class GeneticAlgorithm:
    """
    Represents a genetic algorithm for playing Tic-Tac-Toe.

    Attributes:
        winning_combinations (List[Tuple[int, int, int]]): A list of tuples representing the winning combinations on the Tic-Tac-Toe board.

    Methods:
        initialize_population(population_size: int) -> List[List[int]]: Initializes the population of chromosomes.
        evaluate_fitness(chromosome: List[int], current_board: List[int]) -> int: Evaluates the fitness of a chromosome.
        play_game(chromosome: List[int], current_board: List[int], player: int) -> int: Simulates a game using a chromosome and returns the result.
        check_winner(board: List[int], player: int) -> bool: Checks if a player has won the game.
        evaluate_move(move: int, board: List[int], player: int) -> int: Evaluates the desirability of a move.
        genetic_algorithm(population_size: int, generations: int, current_board: List[int]) -> int: Runs the genetic algorithm to find the best move.

    """

    def __init__(
        self,
        population: int = 50,
        generations: int = 50,
        mutation_rate: float = 0.1,
    ) -> None:
        self.population = population
        self.generations = generations
        self.mutation_rate = mutation_rate

        self.winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

    def initialize_population(self) -> List[List[int]]:
        """
        Initializes the population of chromosomes.

        Args:
            population_size (int): The size of the population.

        Returns:
            List[List[int]]: The initialized population of chromosomes.
        """
        return [
            [random.choice(range(9)) for _ in range(9)] for _ in range(self.population)
        ]

    def evaluate_fitness(self, chromosome: List[int], current_board: List[int]) -> int:
        """
        Evaluates the fitness of a chromosome.

        Args:
            chromosome (List[int]): The chromosome to evaluate.
            current_board (List[int]): The current state of the Tic-Tac-Toe board.

        Returns:
            int: The fitness score of the chromosome.
        """
        wins = sum(
            self.play_game(chromosome, current_board, player=-1) for _ in range(10)
        )
        return wins

    def play_game(
        self, chromosome: List[int], current_board: List[int], player: int
    ) -> int:
        """
        Simulates a game using a chromosome and returns the result.

        Args:
            chromosome (List[int]): The chromosome representing the moves to be played.
            current_board (List[int]): The current state of the Tic-Tac-Toe board.
            player (int): The player to simulate the game for.

        Returns:
            int: 1 if the player wins, 0 otherwise.
        """
        board = current_board.copy()
        current_player = 1

        for move in chromosome:
            if board[move] == 0:
                board[move] = current_player
                if self.check_winner(board, current_player):
                    return 1 if current_player == player else 0
                current_player *= -1

        return 0

    def check_winner(self, board: List[int], player: int) -> bool:
        """
        Checks if a player has won the game.

        Args:
            board (List[int]): The current state of the Tic-Tac-Toe board.
            player (int): The player to check for.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        return any(
            all(board[i] == player for i in combo)
            for combo in self.winning_combinations
        )

    def evaluate_move(self, move: int, board: List[int], player: int) -> int:
        """
        Evaluates the desirability of a move.

        Args:
            move (int): The move to evaluate.
            board (List[int]): The current state of the Tic-Tac-Toe board.
            player (int): The player making the move.

        Returns:
            int: The desirability score of the move.
        """
        temp_board = board.copy()
        temp_board[move] = player
        if self.check_winner(temp_board, player):
            return 2
        temp_board[move] = -player
        if self.check_winner(temp_board, -player):
            return 1
        return 0

    def genetic_algorithm(self, current_board: List[int]) -> int:
        """
        Runs the genetic algorithm to find the best move.

        Args:
            population_size (int): The size of the population.
            generations (int): The number of generations to run the algorithm for.
            current_board (List[int]): The current state of the Tic-Tac-Toe board.

        Returns:
            int: The best move found by the algorithm.
        """
        population = self.initialize_population()

        for _ in range(self.generations):
            fitness_scores = [
                self.evaluate_fitness(chromosome, current_board)
                for chromosome in population
            ]
            best_chromosome = population[fitness_scores.index(max(fitness_scores))]
            new_population = [best_chromosome]

            for _ in range(self.population - 1):
                parent1 = random.choice(population)
                parent2 = random.choice(population)
                crossover_point = random.randint(1, len(parent1) - 1)
                child = parent1[:crossover_point] + parent2[crossover_point:]

                if random.uniform(0, 1) < self.mutation_rate:
                    gene_to_mutate = random.randint(0, len(child) - 1)
                    child[gene_to_mutate] = random.choice(
                        [i for i in range(9) if current_board[i] == 0]
                    )

                new_population.append(child)

            population = new_population

        neutral_moves = [move for move in range(9) if current_board[move] == 0]
        move_scores = [
            self.evaluate_move(move, current_board, -1) for move in neutral_moves
        ]
        best_move = neutral_moves[move_scores.index(max(move_scores))]

        return best_move
