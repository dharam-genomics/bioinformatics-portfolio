import sys
from pathlib import Path
import argparse
from fastq_qc_tools import run_qc

def print_report(results):
    print(results)
    print("----------------------------------")
    print("---------FASTQ QC REPORT----------")
    print("----------------------------------")

    passed = 0
    failed = 0

    for sample, details in results.items():
        print(
            "|", sample, ":",
            details["reads"], "reads :",
            details["status"], "|"
        )

        if details["status"] == "PASS":
            passed += 1
        else:
            failed += 1

    print("----------------------------------")
    print("Total samples: ", len(results))
    print("Passed samples: ", passed)
    print("Failed samples: ", failed)

def main():
    parser = argparse.ArgumentParser(description="Perform basic Fastq read-count QC")
    parser.add_argument("--input", required=True, help="Input directory containing the FASTQ files")
    parser.add_argument("--min-reads", type=int, required=True, help="Minimum number of reads required for PASS")
    args = parser.parse_args()

    fq_path = Path(args.input)
    if not fq_path.is_dir():
        print("Please enter a valid directory.")
        sys.exit(1)
    
    result = run_qc(fq_path, args.min_reads)
    print_report(result)
    

if __name__ == "__main__":
    main()
