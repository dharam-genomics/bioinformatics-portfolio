class FastqValidationError(Exception):
    pass

def validate_record(sequence, quality):
    if len(sequence) == len(quality):
        print("Valid Fastq record")
    else:
        raise FastqValidationError("Sequence and the quality length do not match")

try:
    validate_record("ATGCATGC", "IIIIIIII")
except FastqValidationError as e:
    print("ERROR:", e)  

try:
    validate_record("ATGCATGC", "IIII")
except FastqValidationError as e:
    print("ERROR:", e)
