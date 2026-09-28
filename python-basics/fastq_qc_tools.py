import logging
from pathlib import Path

from dataclasses import dataclass


@dataclass
class QCResult:
    reads: int | None
    status: str
    error: str | None = None


result = QCResult(
    reads=8,
    status="PASS"
)

print(result)
print(result.reads)
print(result.status)
print(result.error)

@dataclass
class QCConfig:
    input_dir: Path
    minimum_reads: int
    output_file: Path

config = QCConfig(
    input_dir=Path("data"),
    minimum_reads=4,
    output_file=Path("fastq_qc_report.txt")
)

print(config)
print(config.input_dir)
print(config.minimum_reads)
print(config.output_file)


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


#def run_qc(fastq_dir, minimum_reads):
def run_qc(config):
    results = {}

    #for file in fastq_dir.glob("*.fastq"):
    for file in config.input_dir.glob("*.fastq"):
        logging.info("Processing sample: %s", file.name)
        try:
            reads = count_reads(file)
            logging.info("Reads found: %s", reads)
            status = check_qc(reads, config.minimum_reads)
            if status == "FAIL":
                #logging.warning("%s failed QC: low read count (%s reads, minimum %s)", file.name, reads, minimum_reads)
                logging.warning("%s failed QC: low read count (%s reads, minimum %s)", file.name, reads, config.minimum_reads)
            else:
                logging.info("%s passed QC", file.name)
            #results[file.name] = {"reads": reads, "status": status }
            results[file.name] = QCResult(reads = reads, status = status)
        except FastqValidationError as e:
            logging.error("%s is invalid: %s", file.name, str(e))
            #results[file.name] = {"reads": None, "status": "INVALID", "error": str(e)}
            results[file.name] = QCResult(reads = None, status = "INVALID", error = str(e))
            continue


    return results
