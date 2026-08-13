import os
file_list = os.listdir()
count = 0
print("Fastq Files: ")
for file in file_list:
    if file.endswith(".fastq"):
        print(file)
        count += 1

print("The total FASTQ files: ", count)

