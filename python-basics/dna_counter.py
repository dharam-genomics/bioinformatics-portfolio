seq = input("Please enter the DNA sequence: ")
count = 0
countA = 0
countT = 0
countG = 0
countC = 0
for base in seq:
    count += 1
    if base == "A":
        countA += 1
    elif base == "T":
        countT += 1
    elif base == "G":
        countG += 1
    elif base == "C":
        countC += 1
print("Count of A is: ", countA)
print("Count of T is: ", countT)
print("Count of G is: ", countG)
print("Count of C is: ", countC)
print("Count of Total Bases is: ", count)
