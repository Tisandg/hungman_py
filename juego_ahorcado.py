from archivos import read_general
from hangmanwordbank import HANGMANPICS
import random
import os

discovered = []
word = ""
completado = False

def get_word():
  #Get word
  filepath = "./archivos/lista_palabras.txt"
  lines = read_general(filepath)
  indice = random.randint(0, len(lines)-1)
  return lines[indice].upper()

def clean_window():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)

def run():
  global word, discovered, completado
  word = get_word()
  discovered = [0] * len(word)

  while completado == False:
    show_interface()
    read_value()
    if check_word():
      completado = True
      show_interface()
    else:
      clean_window()
  print("Finished")

def calculate_progress():
  global discovered
  ones = 0
  for i in discovered:
    if i == 1:
      ones = ones + 1
  progress = int(ones * 100 / len(discovered))
  return progress

def draw_to_print():
  progress = calculate_progress()
  print(progress)
  range_size = 100/len(HANGMANPICS)
  index = 0
  for i in range(len(HANGMANPICS) - 1):
    if progress <= (int(range_size) * (index+1)):
      break
    else:
      index = index+1
  return index

def show_interface():
  line = ""
  for i in range(len(word)):
    if discovered[i] == 1:
      line = line + word[i] +" "
    else:
      line = line + "_ "
  index = draw_to_print()
  print(HANGMANPICS[index])
  print(line+ '\n')

def read_value():
  try:
    letter = input("Type a letter and press enter:")
    if letter.isnumeric():
      raise ValueError("Only letters allowed")
    if letter == '':
      raise ValueError("You must type a letter")
    print()
    letter = letter.upper()
    if letter in word:
      for position, char in enumerate(word):
        if char == letter:
          discovered[position] = 1

  except ValueError as ve:
    print(ve)

def check_word():
  equal = True
  for i in discovered:
    if i != 1:
      equal = False                           
      break
  return equal

if __name__ == '__main__':
  run()