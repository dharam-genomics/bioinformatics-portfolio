from pathlib import Path
def count_reads(filename):
    file = Path(filename)
    with file.open("r") as f:
        lines = len(f.readlines())
        reads = lines / 4
    return reads

files = Path("data/sample1.fastq")
total_reads = count_reads(files)
print("The Number of Reads: ", int(total_reads))
