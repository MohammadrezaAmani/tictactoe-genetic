from tictoctoe.cli import TicTacToeGame
from tictoctoe.genetic import GeneticAlgorithm

game = TicTacToeGame()
game.genetic_algo = GeneticAlgorithm(population=50, generations=50, mutation_rate=0.1)
game.play(with_ai=True)
