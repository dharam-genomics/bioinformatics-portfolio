from pathlib import Path
def count_reads(filename):
    file = Path(filename)
    with file.open("r") as f:
        lines = len(f.readlines())
        reads = lines // 4
    return reads

fq_path = Path("data")
results = {}
for file in fq_path.glob("*.fastq"):
    total_reads = count_reads(file)
    results[file.name] = total_reads
print(results)
for item in results:
    print(item, results[item])
