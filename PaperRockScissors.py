import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['ROCK', 'PAPER', 'SCISSORS']

"""The Player class is the parent class for all of the Players
in this game"""


# Player SUPERCLASS
class Player:

    def __init__(self):
        self.score = 0
        self.previousGames = []

    def move(self):
        return moves

    def getScore(self):
        playerScore = self.score
        return playerScore

    def determineWin(self, my_move, their_move):
        if (my_move == "ROCK" and their_move == "SCISSORS"):
            self.score += 1
        elif (my_move == "PAPER" and their_move == "ROCK"):
            self.score += 1
        elif (my_move == "SCISSORS" and their_move == "PAPER"):
            self.score += 1
        return

    def learn(self, my_move, their_move):
        self.previousGames.append([my_move, their_move])

    def getGameHistory(self):
        return self.previousGames


# RandomPlayer SUBCLASS
class RandomPlayer(Player):
    def move(self):
        return random.choice(super().move())

    def determineWin(self, my_move, their_move):
        return super().determineWin(my_move, their_move)

    def learn(self, my_move, their_move):
        return super().learn(my_move, their_move)

    def getGameHistory(self):
        return super().getGameHistory()


# HumanPlayer SUBCLASS
class HumanPlayer(Player):
    def move(self):
        user_input = input('\nHuman Player Select: \n'
                           '1. PAPER \n2. ROCK \n3. SCISSORS\n: ')
        if(user_input == '1'):
            return "PAPER"
        elif(user_input == '2'):
            return "ROCK"
        elif(user_input == '3'):
            return "SCISSORS"
        else:
            print("Incorrect input please try again.")
            return self.move()

    def determineWin(self, my_move, their_move):
        return super().determineWin(my_move, their_move)

    def learn(self, my_move, their_move):
        return super().learn(my_move, their_move)

    def getGameHistory(self):
        return super().getGameHistory()


# ReflectPlayer SUBCLASS
class ReflectPlayer(Player):

    def move(self):
        opposite_player_move_history = self.getGameHistory()

        if (opposite_player_move_history):
            if(opposite_player_move_history[-1][1] == 'PAPER'):
                return "PAPER"
            elif(opposite_player_move_history[-1][1] == 'ROCK'):
                return "ROCK"
            elif(opposite_player_move_history[-1][1] == 'SCISSORS'):
                return "SCISSORS"
        return random.choice(super().move())

    def determineWin(self, my_move, their_move):
        return super().determineWin(my_move, their_move)

    def learn(self, my_move, their_move):
        return super().learn(my_move, their_move)

    def getGameHistory(self):
        return super().getGameHistory()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def announce_winner(self):
        p1Score = self.p1.getScore()
        p2Score = self.p2.getScore()
        if(p1Score > p2Score):
            return print("Player 1 is the winner!\n")
        else:
            return print("Player 2 is the winner!\n")

    def print_score(self):
        playerOneScore = self.p1.getScore()
        playerTwoScore = self.p2.getScore()
        stringOne = str(playerOneScore)
        stringTwo = str(playerTwoScore)
        print('     ----------SCORE----------')
        print(f"     Player 1 - {stringOne} Player 2 - {stringTwo}\n")
        return

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.determineWin(move1, move2)
        self.p2.determineWin(move2, move1)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if (move1 == move2):
            print(f"\nPlayer 1: {move1}  Player 2: {move2}")
            print('----Draw! Go Again----')
            return self.play_round()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}\n")
        return

    def play_game(self):
        print("Game start!\n")
        for round in range(7):
            print(f"** Round {round+1} **")
            self.play_round()
            self.print_score()
        self.announce_winner()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
