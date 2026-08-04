seq = "ATCCATGTGATGATCCCCCGGGGGGTTTTAT"
count = 0
count_A = 0
count_T = 0
count_G = 0
count_C = 0
for base in seq:
    count += 1
    if base == "A":
        count_A += 1
    elif base == "T":
        count_T += 1
    elif base == "G":
        count_G += 1
    elif base == "C":
        count_C += 1

print("Count of total bases is", count)
print("Count of A is", count_A)
print("Count of T is", count_T)
print("Count of G is", count_G)
print("Count of C is", count_C)
