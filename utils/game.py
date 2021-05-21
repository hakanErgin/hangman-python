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
        print(" ".join(self.correctly_guessed_letters))
        print("enter a letter")
        letter = input().lower()
        if re.match("^[a-zA-Z]$", letter):
            self.turn_count += 1
            if letter in self.word_to_find:
                letter_occurances = [i for i, x in enumerate(self.word_to_find) if x == letter] # get indexes of the matching elements
                for i in letter_occurances:
                  self.correctly_guessed_letters[i] = letter
            else :
                self.lives -= 1
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
            print(f"\n bad guesses: {self.wrongly_guessed_letters}" + f"\n lives: {self.lives}" + f"\n turn count: {self.turn_count}" + f"\n error count: {self.error_count}")
        else:
            print("please enter only one alphabetic letter")
        
    def start_game(self):
        self.word_to_find = list(random.choice(self.possible_words))
        self.correctly_guessed_letters = list("_" * len(self.word_to_find))
        while self.lives > 0 and "_" in self.correctly_guessed_letters:
            self.play()
        else:
            if self.lives == 0:
                self.game_over()
            elif not "_" in self.correctly_guessed_letters:
                self.well_played()

    def game_over(self):
        print("game over...")

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")

