import sys
from pathlib import Path
import argparse
parser = argparse.ArgumentParser(description="Perform basic Fastq read-count QC")
parser.add_argument("--input", required=True, help="Input directory containing the FASTQ files")
parser.add_argument("--min-reads", type=int, required=True, help="Minimum number of reads required for PASS")
args = parser.parse_args()

fq_path = Path(args.input)
if not fq_path.is_dir():
    print("Please enter a valid directory.")
    sys.exit(1)


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

def run_qc(fastq_dir, minimum_reads):
    results = {}
    for file in fastq_dir.glob("*.fastq"):
         reads = count_reads(file)
         status = check_qc(reads, minimum_reads)
         results[file.name] = {"reads" : reads, "status" : status}
         

    return results

result = run_qc(fq_path, args.min_reads)

print(result)
print("----------------------------------")
print("---------FASTQ QC REPORT----------")
print("----------------------------------")
passed = 0
failed = 0
for sample, details in result.items():
    print("|", sample, ":", details["reads"], "reads :",details["status"], "|")
    if details["status"] == "PASS":
        passed += 1
    else:
        failed += 1

print("----------------------------------")
print("Total samples: ", len(result))
print("Passed samples: ", passed)
print("Failed samples: ", failed)
