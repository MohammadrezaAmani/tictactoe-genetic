import dearpygui.dearpygui as dpg

from .genetic import GeneticAlgorithm


class TicTacToeGUI:
    def __init__(self):
        self.genetic_algo = GeneticAlgorithm()
        self.board = [0] * 9
        self.human_player = 1
        self.computer_player = -1
        self.game_over = False

    def handle_button_click(self, sender, app_data):
        if not self.game_over:
            move = app_data
            if self.board[move] == 0:
                self.board[move] = self.human_player
                self.check_game_state()

                if not self.game_over:
                    computer_move = self.genetic_algo.genetic_algorithm(
                        population_size=50, generations=50, current_board=self.board
                    )
                    self.board[computer_move] = self.computer_player
                    self.check_game_state()

    def check_game_state(self):
        if self.genetic_algo.check_winner(self.board, self.human_player):
            dpg.add_text("You win! Congratulations!")
            self.game_over = True
        elif self.genetic_algo.check_winner(self.board, self.computer_player):
            dpg.add_text("You lose! Better luck next time.")
            self.game_over = True
        elif all(cell != 0 for cell in self.board):
            dpg.add_text("It's a draw!")
            self.game_over = True

    def create_gui(self):
        with dpg.handler_registry():
            dpg.add_mouse_click_handler(callback=self.handle_button_click)

        with dpg.window(label="Tic Tac Toe"):
            for row in range(3):
                with dpg.child(width=300, height=100):
                    for col in range(3):
                        move = row * 3 + col
                        dpg.add_button(
                            label=str(move + 1), width=100, height=100, user_data=move
                        )

        dpg.create_viewport(title="Tic Tac Toe", width=500, height=300)
        dpg.setup_dearpygui()

        dpg.show_viewport()

    def run_gui(self):
        dpg.show_viewport()
        dpg.set_primary_window(self.window, True)
        dpg.create_viewport(title="Tic Tac Toe", width=500, height=300)
        dpg.setup_dearpygui()

        with dpg.handler_registry():
            dpg.add_mouse_click_handler(callback=self.handle_button_click)

        with dpg.window(label="Tic Tac Toe"):
            for row in range(3):
                with dpg.child(width=300, height=100):
                    for col in range(3):
                        move = row * 3 + col
                        dpg.add_button(
                            label=str(move + 1), width=100, height=100, user_data=move
                        )

        dpg.create_viewport(title="Tic Tac Toe", width=500, height=300)
        dpg.setup_dearpygui()

        dpg.show_viewport()

        dpg.destroy_item(self.window)
