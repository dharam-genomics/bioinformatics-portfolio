def check_qc(filename):
    passed = []
    failed = []
    invalid = []

    with open(filename, "r") as file:
        for line in file:
            try:
                value = line.strip()
                qc = int(value)
                if qc >= 30:
                    passed.append(qc)
                elif qc < 30:
                    failed.append(qc)
            except ValueError:
                invalid.append(value)
                print("Printing invalid values: ", value)
    return passed, failed, invalid
pass_qc, fail_qc, invalid_qc = check_qc("coverage_mixed.txt")
print("Passed: ", pass_qc)
print("Failed: ", fail_qc)
print("Invalid: ", invalid_qc)
print("Number Passed: ", len(pass_qc))
print("Number failed: ", len(fail_qc))
print("Number Invalid: ", len(invalid_qc))
