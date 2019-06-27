def test():
  raise ValueError("Eroare 1")

try:
  test()
except BaseException as e:
  print (e)
