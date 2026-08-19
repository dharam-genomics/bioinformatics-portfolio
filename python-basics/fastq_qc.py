from pathlib import Path
def count_reads(filename):
    sample = Path(filename)
    with sample.open("r") as file:
        lines = len(file.readlines())
        reads = lines // 4

    return reads
def check_qc(reads, minimum_reads):
    if reads >= minimum_reads:
        status = "PASS"
    else:
        status = "FAIL"

    return status

fq_path = Path("data")
results = {}
minimum_reads = 4
for fq_file in fq_path.glob("*.fastq"):
    reads = count_reads(fq_file)
    status = check_qc(reads, minimum_reads)
    results[fq_file.name] = {"reads": reads, "status": status}

print(results)
print("----------------------------------")
print("---------FASTQ QC REPORT----------")
print("----------------------------------")
for sample, details in results.items():
    print("|", sample, ":", details["reads"], "reads :",details["status"], "|")

print("----------------------------------")

