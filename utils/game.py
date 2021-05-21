import random
import re

from typing import List

class Hangman:
    '''the game'''
    def __init__(self):
        '''the game constructor'''
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: List[str] = []
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = []
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def play(self):
        print("please enter a letter")
        letter = input().lower()
        if re.match("^[a-zA-Z]$", letter):
            print(self.correctly_guessed_letters)
            if letter in self.word_to_find:
                print("yes")
            else :
                self.lives -= 1
                print("no")
        
    def start_game(self):
        self.word_to_find = list(random.choice(self.possible_words))
        self.correctly_guessed_letters = "_" * len(self.word_to_find)
        print(self.word_to_find)
        while self.lives > 0:
            print(self.lives)
            self.play()

    def game_over():
        pass

    def well_played():
        pass

