import argparse

from tictoctoe import GeneticAlgorithm, TicTacToeGame, __version__

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="tictoctoe",
        description="Tic-Tac-Toe game with genetic algorithm.",
        epilog="Author: Mohammadreza Amani",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "-p",
        "--population",
        type=int,
        default=50,
        help="population size",
    )
    parser.add_argument(
        "-g",
        "--generations",
        type=int,
        default=50,
        help="number of generations",
    )
    parser.add_argument(
        "-m",
        "--mutation",
        type=float,
        default=0.1,
        help="mutation rate",
    )
    parser.add_argument(
        "-a",
        "--ai",
        action="store_true",
        help="AI mode",
    )
    args = parser.parse_args()
    game = TicTacToeGame()
    if args.ai:
        game.genetic_algo = GeneticAlgorithm(
            args.population,
            args.generations,
            args.mutation,
        )
    game.play(with_ai=args.ai)
