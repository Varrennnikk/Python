def calculate_gc_content(sequence):
    """Вычисляет GC-состав последовательности ДНК."""
    gc_count = sequence.count('G') + sequence.count('C')
    total_length = len(sequence)
    if total_length == 0:
        return 0.0  # Предотвращаем деление на ноль
    gc_content = (gc_count / total_length) * 100
    return gc_content


def read_fasta(filepath):
    """Читает FASTA файл и возвращает словарь с идентификаторами и последовательностями."""
    sequences = {}
    with open(filepath, 'r') as file:
        identifier = None
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if identifier:  # Сохраняем предыдущую последовательность, если она есть
                    sequences[identifier] = sequence
                identifier = line[1:]  # Удаляем ">"
                sequence = ""
            else:
                sequence += line
        if identifier:  # Сохраняем последнюю последовательность
            sequences[identifier] = sequence
    return sequences


# Пример использования
fasta_file = "example.fasta"  # Замените на свой FASTA файл
dna_sequences = read_fasta(fasta_file)

gc_contents = {}
for identifier, sequence in dna_sequences.items():
    gc_content = calculate_gc_content(sequence)
    gc_contents[identifier] = gc_content

# Находим последовательность с максимальным GC-составом
best_identifier = max(gc_contents, key=gc_contents.get)
best_gc_content = gc_contents[best_identifier]

print(f"Последовательность с максимальным GC-составом: {best_identifier}")
print(f"GC-состав: {best_gc_content:.5f}%")
