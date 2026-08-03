sequence = "ATGCGTGC"
count = 0
for base in sequence:
    print(sequence, count, base)
    count+=1
for i in range(4):
    print("range(4)", i)
for i in range(2, 9):
    print("range(2,9)", i)
for i in range(2,9,3):
    print("range(2,9,3)", i)
for i in range(10,0,-2):
    print("range(10,0,-2)", i)
