def intreabaPattern():

  print("Introdu un pattern pentru led")
  print("Ghid:")
  print("q = Perioada lunga aprins (2 secunde)")
  print("w = Perioada scurta aprins (0,5 secunde)")
  print("e = Pauza de o secunda")
  print("Exemplu: qwwqwwe")

  print("Introdu pattern-ul:")
  pattern = input()

  print("Patternul este:", pattern)
  return pattern

def PrelucreazaPattern(pattern):

    pattern = pattern.strip()
    #scoatem spatiile goale (space-urile) din pattern

intreabaPattern()