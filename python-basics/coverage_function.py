passed = []
def check_qc(coverage_file):
    with open(coverage_file, "r") as file:
        for line in file:
            coverage = int(line.strip())
            if coverage >= 30:
                passed.append(coverage)
    return(passed)
sample = check_qc("coverage.txt")
print("The list: ", sample)
print("The number of passing value: ", len(sample))
