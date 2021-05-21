import random
import re

from typing import List

class Hangman:
    '''the game'''
    def __init__(self) -> None:
        '''the game constructor'''
        self._possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self._word_to_find: List[str] = []
        self._lives: int = 5
        self._correctly_guessed_letters: List[str] = []
        self._wrongly_guessed_letters: List[str] = []
        self._turn_count: int = 0
        self._error_count: int = 0

    def play(self) -> None:
        print(" ".join(self._correctly_guessed_letters))
        print("enter a letter")
        letter = input().lower()
        if re.match("^[a-zA-Z]$", letter):
            self._turn_count += 1
            if letter in self._word_to_find:
                letter_occurances = [i for i, x in enumerate(self._word_to_find) if x == letter] # get indexes of the matching elements
                for i in letter_occurances:
                  self._correctly_guessed_letters[i] = letter
            else :
                self._lives -= 1
                self._wrongly_guessed_letters.append(letter)
                self._error_count += 1
            print(f"\n bad guesses: {self._wrongly_guessed_letters}" + f"\n lives: {self._lives}" + f"\n turn count: {self._turn_count}" + f"\n error count: {self._error_count}")
        else:
            print("please enter only one alphabetic letter")
        
    def start_game(self) -> None:
        self._word_to_find = list(random.choice(self._possible_words))
        self._correctly_guessed_letters = list("_" * len(self._word_to_find))
        while self._lives > 0 and "_" in self._correctly_guessed_letters:
            self.play()
        else:
            if self._lives == 0:
                self.game_over()
            elif not "_" in self._correctly_guessed_letters:
                self.well_played()

    def game_over(self) -> None:
        print("game over...")

    def well_played(self) -> None:
        print(f"You found the word: {''.join(self._word_to_find)} in {self._turn_count} turns with {self._error_count} errors!")

