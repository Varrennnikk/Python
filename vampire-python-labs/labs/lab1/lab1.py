def hamming_distance(s, t):
    """Вычисляет расстояние Хэмминга между двумя строками."""
    if len(s) != len(t):
        raise ValueError("Длины строк должны совпадать.")

    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1

    return distance

# Пример использования
dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT"

try:
    distance = hamming_distance(dna1, dna2)
    print(f"Расстояние Хэмминга: {distance}")
except ValueError as e:
    print(f"Ошибка: {e}")
