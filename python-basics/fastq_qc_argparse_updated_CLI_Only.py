import sys
from pathlib import Path
import argparse
from fastq_qc_tools import run_qc

def format_report(results):
    report = ""   
    report += "----------------------------------\n"
    report += "---------FASTQ QC REPORT----------\n"
    report += "----------------------------------\n"
    passed = 0
    failed = 0
    for sample, details in results.items():
        report += f"| {sample} : {details['reads']} reads : {details['status']} |\n"
        if details["status"] == "PASS":
            passed += 1
        else:
            failed += 1
    
    report += "----------------------------------\n"
    report += f"Total samples: {len(results)}\n"
    report += f"Passed samples: {passed}\n"
    report += f"Failed samples: {failed}\n"
    
    return report

def print_report(report):
    print(report)

def save_report(report, output_file):
    with open(output_file, "w") as file:
            file.write(report)

def main():
    parser = argparse.ArgumentParser(description="Perform basic Fastq read-count QC")
    parser.add_argument("--input", required=True, help="Input directory containing the FASTQ files")
    parser.add_argument("--min-reads", type=int, required=True, help="Minimum number of reads required for PASS")
    parser.add_argument("--output", required=True, help="Output file to write the FASTQ QC report")
    args = parser.parse_args()

    fq_path = Path(args.input)
    if not fq_path.is_dir():
        print("Please enter a valid directory.")
        sys.exit(1)
    
    results = run_qc(fq_path, args.min_reads)
    report = format_report(results)
    print_report(report)
    save_report(report, args.output)
    

if __name__ == "__main__":
    main()
