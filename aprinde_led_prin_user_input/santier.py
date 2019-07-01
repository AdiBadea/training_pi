def log(text, variable):
  print(text)
  print(variable)

def intreabaPattern():
  print("Introdu un pattern pentru led")
  print("Ghid:")
  print("q = Perioada lunga aprins (2 secunde)")
  print("w = Perioada scurta aprins (0,5 secunde)")
  print("e = Pauza de o secunda")
  print("Exemplu: qwwqwwe")

  print("Introdu pattern-ul:")
  pattern = input()

  # print("Patternul este:", pattern)

  # print(len(pattern))

  return pattern

def prelucreazaPattern(pattern):
    #scoatem spatiile goale (space-urile) din pattern
    pattern = pattern.strip()

    patternArray = []

    # i = len(pattern)
    i = 4
    while i != 0:
      log("I este", i)
      i -= i


prelucreazaPattern(intreabaPattern())