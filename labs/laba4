from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def combine_genbank_files(input_files, output_file):
    """Объединяет несколько GenBank файлов в один."""
    records = []
    for file in input_files:
        try:
            records.extend(SeqIO.parse(file, "genbank"))
        except FileNotFoundError:
            print(f"Файл не найден: {file}")
            return

    SeqIO.write(records, output_file, "genbank")
    print(f"Объединенные записи сохранены в: {output_file}")

def calculate_gc_content(seq):
    """Вычисляет GC-состав последовательности."""
    gc_count = seq.upper().count('G') + seq.upper().count('C')
    seq_len = len(seq)
    if seq_len == 0:
        return 0.0
    return (gc_count / seq_len) * 100

def translate_cds(genbank_file):
    """Извлекает CDS и транслирует в аминокислотные последовательности."""
    for record in SeqIO.parse(genbank_file, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                if "translation" not in feature.qualifiers:
                    print(f"Отсутствует 'translation' для CDS в записи {record.id}")
                    continue
                protein_seq = feature.qualifiers["translation"][0]
                print(f"CDS ID: {record.id}, Protein: {protein_seq}")

#Пример использования

#combine_genbank_files(["file1.gb", "file2.gb"], "combined.gb")  # Замените на ваши файлы
#translate_cds("combined.gb")  # Замените на ваш объединенный файл
