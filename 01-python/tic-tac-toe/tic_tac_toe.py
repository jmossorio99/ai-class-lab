import re
import random as random

_PLAYER = "player"
_MACHINE = "machine"
_TIE = "tie"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"


class TicTacToeGame():
    def __init__(self):
        self.board = [None] * 9
        self.turn = _PLAYER
        self.is_game_over = False
        self.winner = None

    def equals3(self, a, b, c):
        return a is not None and a == b and b == c

    def check_winner(self):

        for i in range(0, 9, 3):
            if (self.equals3(self.board[i], self.board[i + 1], self.board[i + 2])):
                self.winner = self.turn
                self.is_game_over = True
        for i in range(3):
            if (self.equals3(self.board[i], self.board[i + 3], self.board[i + 6])):
                self.winner = self.turn
                self.is_game_over = True
        if (self.equals3(self.board[0], self.board[4], self.board[8]) or self.equals3(self.board[2], self.board[4], self.board[6])):
            self.winner = self.turn
            self.is_game_over = True

        open_slots = 0
        for i in range(9):
            if (self.board[i] == None):
                open_slots += 1

        if (self.is_game_over == False and open_slots == 0):
            self.winner = _TIE
            self.is_game_over = True

    def play(self):
        if self.turn == _PLAYER:
            self.player_turn()
            self.check_winner()
            if (self.is_game_over):
                self.print_result()
            else:
                self.turn = _MACHINE
                self.print()
        else:
            self.machine_turn()
            self.check_winner()
            if (self.is_game_over):
                self.print_result()
            else:
                self.turn = _PLAYER
                self.print()

    def player_choose_cell(self):
        print("Input empty cell bewtween 0 and 8")

        player_cell = input().strip()
        match = re.search("\d", player_cell)

        if not match:
            print("Input is not a number, please try again")

            return self.player_choose_cell()

        player_cell = int(player_cell)

        if self.board[player_cell] is not None:
            print("Cell is already taken, try again")

            return self.player_choose_cell()

        return player_cell

    def player_turn(self):
        chosen_cell = self.player_choose_cell()

        self.board[chosen_cell] = _PLAYER_SYMBOL

    def machine_turn(self):

        # for i, cell in enumerate(self.board):
        #     if cell is None:
        #         self.board[i] = _MACHINE_SYMBOL
        #         break
        for i in range(9):
            random_cell = random.randint(0, 8)
            if self.board[random_cell] is None:
                self.board[random_cell] = _MACHINE_SYMBOL
                break

    def format_board(self):
        # TODO: Implement this function, it must be able to print the board in the following format:
        #  x|o|
        #   | |
        #   | |
        formated_board = ""
        for i in range(0, 9, 3):
            formated_board += self.format_string(self.board[i]) + "|" + \
                self.format_string(
                    self.board[i + 1]) + "|" + self.format_string(self.board[i + 2]) + "\n"
        return formated_board

    def format_string(self, line):
        if (line is None):
            return " "
        return line

    def print(self):
        print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
        print(self.format_board())
        print()

    def print_result(self):
        print(self.format_board())
        print(self.winner + " won!" if self.winner != _TIE else "It is a tie!")
