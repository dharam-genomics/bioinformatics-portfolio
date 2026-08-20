import sys
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

if len(sys.argv) < 3:
    print("Usage: python3 fastq_qc_updated.py <directory> <minimum reads number>")
    sys.exit(1)
fq_path = Path(sys.argv[1])
if not fq_path.is_dir():
    print("The directory is not a valid directory!")
    sys.exit(1)
try:
    minimum_reads = int(sys.argv[2])
except ValueError:
    print("Minimum reads must be an integer.")
    sys.exit(1)
results = {}
for fq_file in fq_path.glob("*.fastq"):
    reads = count_reads(fq_file)
    status = check_qc(reads, minimum_reads)
    results[fq_file.name] = {"reads": reads, "status": status}

print(results)
print("----------------------------------")
print("---------FASTQ QC REPORT----------")
print("----------------------------------")
passed = 0
failed = 0
for sample, details in results.items():
    print("|", sample, ":", details["reads"], "reads :",details["status"], "|")
    if details["status"] == "PASS":
        passed += 1
    else:
        failed += 1

print("----------------------------------")
print("Total samples: ", len(results))
print("Passed samples: ", passed)
print("Failed samples: ", failed)
