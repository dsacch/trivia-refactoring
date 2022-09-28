#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        Output.write(player_name + " was added"+'\n')
        Output.write("They are player number %s" % len(self.players)+'\n')

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        Output.write("%s is the current player" % self.players[self.current_player]+'\n')
        Output.write("They have rolled a %s" % roll+'\n')

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                Output.write("%s is getting out of the penalty box" % self.players[self.current_player]+'\n')
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                Output.write(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player])+'\n')
                Output.write("The category is %s" % self._current_category+'\n')
                self._ask_question()
            else:
                Output.write("%s is not getting out of the penalty box" % self.players[self.current_player]+'\n')
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            Output.write(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player])+'\n')
            Output.write("The category is %s" % self._current_category+'\n')
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': Output.write(self.pop_questions.pop(0)+'\n')
        if self._current_category == 'Science': Output.write(self.science_questions.pop(0)+'\n')
        if self._current_category == 'Sports': Output.write(self.sports_questions.pop(0)+'\n')
        if self._current_category == 'Rock': Output.write(self.rock_questions.pop(0)+'\n')

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                Output.write('Answer was correct!!!!'+'\n')
                self.purses[self.current_player] += 1
                Output.write(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.'+'\n')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            Output.write("Answer was corrent!!!!"+'\n')
            self.purses[self.current_player] += 1
            Output.write(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.'+'\n')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        Output.write('Question was incorrectly answered'+'\n')
        Output.write(self.players[self.current_player] + " was sent to the penalty box"+'\n')
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)

import random
from random import randrange

if __name__ == '__main__':
    Output = open('/Users/domenic/Desktop/softwaredev/githubstuff/trivia-refactoring/python3/Output.md', 'w')
    Output.write('')
    Output = open('/Users/domenic/Desktop/softwaredev/githubstuff/trivia-refactoring/python3/Output.md', 'a')
    
    random.seed(1234)

    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(random.randrange(5) + 1)

        if random.randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break

    Output.close()