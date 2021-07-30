class TicTacToe():
    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.winner_set = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.end = False

    def draw(self):
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}")
        print(f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        print(f"{self.board[6]}|{self.board[7]}|{self.board[8]}")

    def player1(self):
        print('Enter the position')
        self.position = int(input("Player1('X'): "))
        self.position -= 1
        if self.board[self.position] != ' ':
            print("Already taken!")
            self.player1()
        else:
            self.board[self.position] = 'X'

    def player2(self):
        print('Enter the position')
        self.position = int(input("Player2('O'): "))
        self.position -= 1
        if self.board[self.position] != ' ':
            print("Already taken!")
            self.player1()
        else:
            self.board[self.position] = 'O'

    def validate_board(self):
        for a in self.winner_set:
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == 'X':
                print("Player 1 wins!!")
                return True
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == 'O':
                print("Player 2 wins!!")
                return True
            if self.board.count(' ') == 0:
                print("It's a Draw!")
                return True

to_continue = True
while to_continue:
    t = TicTacToe()

    while not t.end:
        t.draw()
        t.end = t.validate_board()
        if t.end == True:
            break
        t.player1()

        t.draw()
        t.end = t.validate_board()
        if t.end == True:
            break
        t.player2()

    if input('Do you want to Play again? (y/n): ') == 'y':
        to_continue=True
    else:
        print('Good Bye!')
        to_continue = False