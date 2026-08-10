passed = []
failed = []
passed_qc = 0
with open("coverage.txt", "r") as coverage:
    for value in coverage:
        qc = int(value.strip())
        if qc >= 30:
            passed.append(qc)
            passed_qc += 1
        else:
            failed.append(qc)
print("All passing values are: ")
with open("passed_coverage.txt", "w") as coverage:
    for pass_qc in passed:
        coverage.write(str(pass_qc) + "\n")
        print(pass_qc)
print("Number of samples passing QC:", passed_qc)
print("The other way to get count is: ", len(passed))
print("All failed QC values are: ")
with open("failed_coverage.txt", "w") as failed_coverage:
    for fail in failed:
        failed_coverage.write(str(fail) + "\n")
        print(fail)
print("Number of samples QC failed: ", len(failed))
