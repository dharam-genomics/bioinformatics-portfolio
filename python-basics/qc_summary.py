results = {
    "sample1.fastq": {"reads": 50, "status": "PASS"},
    "sample2.fastq": {"reads": 20, "status": "FAIL"},
    "sample3.fastq": {"reads": 80, "status": "PASS"},
    "sample4.fastq": {"reads": 10, "status": "FAIL"}
}

passed = 0
failed = 0
for sample, details in results.items():
    if details["status"] == "PASS":
        #print(sample, details["reads"])
        passed += 1
    else:
        failed += 1

print("Passed samples:", passed)
print("Failed samples:", failed)
