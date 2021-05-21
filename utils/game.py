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
            if letter in self.word_to_find:
                letter_occurances = [i for i, x in enumerate(self.word_to_find) if x == letter] # get indexes of the matching elements
                for i in letter_occurances:
                  self.correctly_guessed_letters[i] = letter
            else :
                self.lives -= 1
                print("no")
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
        print(" ".join(self.correctly_guessed_letters))
        
    def start_game(self):
        self.word_to_find = list(random.choice(self.possible_words))
        self.correctly_guessed_letters = list("_" * len(self.word_to_find))
        print(self.word_to_find)
        while self.lives > 0:
            print(self.lives)
            self.play()

    def game_over():
        print("game over...")

    def well_played(self):
        print(f"You found the word: {self.word_to_find_here} in {self.turn_count_here} turns with {self.error_count_here} errors!")

