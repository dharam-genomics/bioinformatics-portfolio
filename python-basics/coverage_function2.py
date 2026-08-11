def check_qc(filename):
    passed = []
    failed = []
    with open(filename, "r") as file:
        for line in file:
            qc = int(line.strip())
            if qc >= 30:
                passed.append(qc)
            if qc < 30:
                failed.append(qc)


    return passed, failed
passed, failed = check_qc("coverage.txt")
print("The QC passed values are: ", passed)
print("The QC failed values are: ", failed)
print("Number of QC passed: ", len(passed))
print("Number of QC failed: ", len(failed))
