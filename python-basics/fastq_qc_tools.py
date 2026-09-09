from pathlib import Path
class FastqValidationError(Exception):
    pass


def validate_record(sequence, quality):
    if len(sequence) != len(quality):
        raise FastqValidationError(
            "Sequence and quality lengths do not match"
        )

def count_reads(filename):
    sample = Path(filename)
    sequence = ''
    quality = ''
    reads = 0
    with sample.open("r") as file:
        while True:
            record = [file.readline() for _ in range(4)]
            if record[0] == "":
                break 
            sequence = record[1]
            quality = record[3]
            validate_record(sequence, quality)
            reads += 1

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
        try:
            reads = count_reads(file)
            status = check_qc(reads, minimum_reads)
            results[file.name] = {
            "reads": reads,
            "status": status
        }
        except FastqValidationError as e:
            results[file.name] = {"reads": None, "status": "INVALID", "error": str(e)}
            continue


    return results
