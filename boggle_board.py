import random 
from random import shuffle

class BoggleBoard:
  # class attribute for empty board
  board = [['' for _ in range(4)] for _ in range(4)]
  DICE = [
    ['A ', 'A ', 'E ', 'E ', 'G ', 'N '],
    ['E ', 'L ', 'R ', 'T ', 'T ', 'Y '],
    ['A ', 'O ', 'O ', 'T ', 'T ', 'W '],
    ['A ', 'B ', 'B ', 'J ', 'O ', 'O '],
    ['E ', 'H ', 'R ', 'T ', 'V ', 'W '],
    ['C ', 'I ', 'M ', 'O ', 'T ', 'U '],
    ['D ', 'I ', 'S ', 'T ', 'T ', 'Y '],
    ['E ', 'I ', 'O ', 'S ', 'S ', 'T '],
    ['D ', 'E ', 'L ', 'R ', 'V ', 'Y '],
    ['A ', 'C ', 'H ', 'O ', 'P ', 'S '],
    ['H ', 'I ', 'M ', 'N ', 'Qu', 'U '],
    ['E ', 'E ', 'I ', 'N ', 'S ', 'U '],
    ['E ', 'E ', 'G ', 'H ', 'N ', 'W '],
    ['A ', 'F ', 'F ', 'K ', 'P ', 'S '],
    ['H ', 'L ', 'N ', 'N ', 'R ', 'Z '],
    ['D ', 'E ', 'I ', 'L ', 'R ', 'X ']
  ]
    
  def __init__(self):
    pass
  
  #print's board in proper display for game
  def display_board(self):
    for list in BoggleBoard.board:
      print(list)

  def shake(self):
    dice_assignment = self.dice_assignment()
    index = 0
    for i, list in enumerate(BoggleBoard.board):
      for j, space in enumerate(BoggleBoard.board[i]): 
        BoggleBoard.board[i][j] = dice_assignment[index]
        index += 1
    return self.display_board()
  
  def dice_assignment(self):
    shuffle(BoggleBoard.DICE)
    die_assignment = []
    for i, list in enumerate(BoggleBoard.DICE):
      die_assignment.append(random.choice(BoggleBoard.DICE[i]))
    return die_assignment
  
  def format_word(self, word):
    word = word.upper()
    letters = []
    for letter in word:
      letters.append(letter + ' ')
    return letters
  
  def check_word(self, word):
    letters = self.format_word(word)
    head = letters.pop(0)
    tail = letters
    head_indices = []
    
    for i, list in enumerate(BoggleBoard.board):
      for j, space in enumerate(BoggleBoard.board[i]):
        if BoggleBoard.board[i][j] == head:
          head_indices.append((i, j))
          
    for index in head_indices:
      for letter in tail:
        #left
        if BoggleBoard.board[index[0]][index[1] - 1] == tail[letter]:
          
          
    
    return head_indices
        
        

# game = BoggleBoard()
# print(game.shake())
# # print(game.format_word('is'))
# print(game.check_word('is'))
board = [
  ['A', 'B', 'C', 'D'],
  ['E', 'F', 'G', 'H'],
  ['I', 'J', 'K', 'L'],
  ['M', 'N', 'O', 'P'],
]

def check_word():
    head = 'F '
    tail = ['G', 'H']
    head_indices = []
    
    for i, list in enumerate(board):
      for j, space in enumerate(board[i]):
        if board[i][j] == head:
          head_indices.append((i, j))
          
    for index in head_indices:
      for letter in tail:
        #left
        if board[index[0]][index[1] - 1] == tail[letter]:

    return head_indices
  
print(check_word())