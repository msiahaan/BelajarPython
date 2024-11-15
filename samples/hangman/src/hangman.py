import random
import sys

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

class HangMan:
    def __init__(self):
      self.hangman_pics = HANGMANPICS
      self.word_list = words
      self.wordlist_len = len(self.word_list)

    def _get_random_word(self):
      ''' This method return a random word '''
      idx = random.randint(0, self.wordlist_len - 1)
      self.random_word = self.word_list[idx]
    
    def _get_guess(self):
      '''This to get a guess.'''
      print("Enter a guess character: ")
      self.guess = input()

    def run_game(self):
      self._get_random_word()
      while True:
        self._get_guess()
        if self.guess in self.random_word:
            print("Good!")
        else:
            sys.exit()
                
            

