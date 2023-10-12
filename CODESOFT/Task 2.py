import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize an empty board
        self.current_winner = None  # Keep track of the winner

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Tells us what number corresponds to what box in the board
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Assign the square to the letter on the board and then return if the move is valid
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def play(self):
        TicTacToe.print_board_nums()
        letter = 'X'  # Starting letter
        while self.empty_squares():
            move = None
            if letter == 'O':
                # AI's turn
                move = self.get_computer_move()
            else:
                # Human's turn
                valid_square = False
                while not valid_square:
                    square = input(letter + '\'s turn. Input move (0-8): ')
                    try:
                        square = int(square)
                        if 0 <= square <= 8:
                            if self.board[square] == ' ':
                                valid_square = True
                            else:
                                print('Square is occupied. Try again.')
                        else:
                            print('Invalid square. Try again.')
                    except ValueError:
                        print('Invalid input. Enter a number between 0-8.')

                move = square

            if self.make_move(move, letter):
                self.print_board()
                if self.current_winner:
                    print(letter + ' wins!')
                    return letter  # Ends the loop and exits the game
                letter = 'O' if letter == 'X' else 'X'  # Switches player

        print('It\'s a tie!')

    def get_computer_move(self):
        # Implement the Minimax algorithm with Alpha-Beta Pruning
        best_score = float('-inf')
        best_move = None
        for move in self.available_moves():
            self.make_move(move, 'O')  # Simulate the AI making a move
            score = self.minimax(self.board, 0, False)
            self.board[move] = ' '  # Reset the move
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, state, depth, maximizing_player):
        if self.current_winner:
            return {'X': -10, 'O': 10, 'tie': 0}[self.current_winner]
        if not self.empty_squares():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.make_move(move, 'O')
                eval = self.minimax(self.board, depth + 1, False)
                self.board[move] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.make_move(move, 'X')
                eval = self.minimax(self.board, depth + 1, True)
                self.board[move] = ' '
                min_eval = min(min_eval, eval)
            return min_eval


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
