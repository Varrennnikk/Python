def hamming_distance(s, t):

  if len(s) != len(t):
    raise ValueError("Строки должны быть одинаковой длины")

  distance = 0
  for i in range(len(s)):
    if s[i] != t[i]:
      distance += 1

  return distance

try:
  s = input("Введите первую строку ДНК: ")
  t = input("Введите вторую строку ДНК: ")
  distance = hamming_distance(s, t)
  print(distance)
except ValueError as e:
  print(e)
