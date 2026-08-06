coverage = [34, 38, 40, 50, 10, 78, 89, 90, 20, 99]
total = 0
qc_passed = 0
qc_failed = 0
highest = coverage[0]
lowest = coverage[0]
print("Coverage values:")
for item in coverage:
    total += 1
    print(item)
    if item > highest:
        highest = item
    if item < lowest:
        lowest = item
print("Total samples: ", total)
print("Total samples using len():", len(coverage))
print("Sample Passing QC (>=30):") 
for item in coverage:
    if item >= 30:
        qc_passed += 1
        print(item)
print("Number of sample passing QC:", qc_passed)
print("Samples failing QC (<30):")
for item in coverage:
    if item < 30:
        print(item)
        qc_failed +=1
print("Number of samples failing QC:", qc_failed)
print("Highest Coverage:", highest)
print("Lowest Coverage:", lowest)
