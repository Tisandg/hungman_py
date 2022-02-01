def read():
  numbers = []
  with open("./archivos/numeros.txt", "r", encoding="utf-8") as f:
    for line in f:
      numbers.append(int(line))
  print(numbers)

def read_general(filepath):
  lineas = []
  with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
      lineas.append(clean_strings(line))
  return lineas

def clean_strings(text):
  return text.rstrip("\n")

def write():
  names = ["Facundo", "Miguel", "Pepe", "Cristina", "Rocío"]
  with open("./archivos/names.txt", "a", encoding="utf-8") as f:
    for name in names:
      f.write(name)
      f.write("\n")
  

def run():
  read()
  write()

if __name__ == '__main__':
  run()