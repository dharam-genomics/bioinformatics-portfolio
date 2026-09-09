results = {
    "sample1.fastq": {"reads": 100, "status": "PASS"},
    "sample2.fastq": {"reads": 40, "status": "FAIL"},
    "sample3.fastq": {"reads": 80, "status": "PASS"},
    "sample4.fastq": {"reads": 20, "status": "FAIL"},
    "sample5.fastq": {"reads": 0, "status": "INVALID"}
}
passed = 0
failed = 0
invalid = 0
for sample, details in results.items():
    if details["status"] == "PASS":
        passed += 1
    elif details["status"] == "FAIL":
        failed += 1
    else:
        invalid += 1

print("Passed samples:", passed)
print("Failed samples:", failed)
print("Invalid samples:", invalid)
