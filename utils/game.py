import random
import re

from typing import List

class Hangman:
    """ game class. the game starts, played until 1 of the 2 conditions are satisfied:
    either player guesses the word and wins or they lose because they are out of lives
    """
    
    def __init__(self) -> None:
        """ the game constructor. Game state is being tracked here.
        """
        self._possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self._word_to_find: List[str] = []
        self._lives: int = 5
        self._correctly_guessed_letters: List[str] = []
        self._wrongly_guessed_letters: List[str] = []
        self._turn_count: int = 0
        self._error_count: int = 0

    def play(self) -> None:
        """ each round is played here. the player is asked to enter a letter, and the letter is validated.
        """
        print(" ".join(self._correctly_guessed_letters)) # initially with blank letters
        print("Enter a letter")
        letter = input().lower()
        if re.match("^[a-z]$", letter):
            self._turn_count += 1
            if letter in self._word_to_find:
                # get indexes of the matching letters, so that we can show the user if they get it right
                letter_occurances = [index for index, element in enumerate(self._word_to_find) if element == letter] 
                for i in letter_occurances: 
                  self._correctly_guessed_letters[i] = letter # the correct letters being revealed
            else : 
                self._lives -= 1
                self._wrongly_guessed_letters.append(letter)
                self._error_count += 1
            print(f"\nBad guesses: {self._wrongly_guessed_letters}" + f"\nLives: {self._lives}" + f"\nTurn count: {self._turn_count}" + f"\nError count: {self._error_count}")
        else:
            print("Please enter only one alphabetic letter")
        
    def start_game(self) -> None:
        """ will be called once, will set the game and will call the play method until the game ends.
        """
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
        """ called when player is out of lives...
        """
        print("game over...")

    def well_played(self) -> None:
        """ called when player guesses the
        """
        print(f"You found the word: {''.join(self._word_to_find)} in {self._turn_count} turns with {self._error_count} errors!")

