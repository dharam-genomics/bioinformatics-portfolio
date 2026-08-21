import sys
import argparse
parser = argparse.ArgumentParser(description="Perform basic Fastq read-count QC")
parser.add_argument("--input", required=True, help="Input directory containing the FASTQ files")
parser.add_argument("--min-reads", type=int, required=True, help="Minimum number of reads required for PASS")
args = parser.parse_args()

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

fq_path = Path(args.input)
if not fq_path.is_dir():
    print("Please enter a valid directory.")
    sys.exit(1)
results = {}
for fq_file in fq_path.glob("*.fastq"):
    reads = count_reads(fq_file)
    status = check_qc(reads, args.min_reads)
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
