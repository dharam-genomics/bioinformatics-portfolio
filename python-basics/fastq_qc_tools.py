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


def run_qc(fastq_dir, minimum_reads):
    results = {}

    for file in fastq_dir.glob("*.fastq"):
        reads = count_reads(file)
        status = check_qc(reads, minimum_reads)

        results[file.name] = {
            "reads": reads,
            "status": status
        }

    return results
