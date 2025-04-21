def read_fasta(filename):
  """
  Читает последовательности ДНК из FASTA файла.

  Args:
    filename: Имя файла FASTA.

  Returns:
    Словарь, где ключи - идентификаторы последовательностей,
    а значения - последовательности ДНК.
  """
  sequences = {}
  with open(filename, 'r') as f:
    identifier = None
    sequence = ""
    for line in f:
      line = line.strip()
      if line.startswith(">"):
        if identifier:
          sequences[identifier] = sequence
        identifier = line[1:]
        sequence = ""
      else:
        sequence += line
    if identifier: # Add last sequence
        sequences[identifier] = sequence

  return sequences


def gc_content(sequence):
  """
  Вычисляет GC-состав последовательности ДНК в процентах.

  Args:
    sequence: Последовательность ДНК.

  Returns:
    GC-состав в процентах.
  """
  gc_count = sequence.count('G') + sequence.count('C')
  return (gc_count / len(sequence)) * 100


# Основная часть программы
filename = "rosalind_gc.txt"  # Замените на имя вашего файла
sequences = read_fasta(filename)

max_gc = -1
max_id = None

for identifier, sequence in sequences.items():
  gc = gc_content(sequence)
  if gc > max_gc:
    max_gc = gc
    max_id = identifier

print(max_id)
print(f"{max_gc:.5f}")
