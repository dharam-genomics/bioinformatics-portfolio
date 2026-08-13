import os
fastqlist = []
dirname = input("Please enter the input folder name: ")
if os.path.exists(dirname):
    if os.path.isdir(dirname):
        filelist = os.listdir(dirname)
        for filename in filelist:
            if filename.endswith(".fastq"):
                name = os.path.join(dirname, filename)
                fastqlist.append(name)
    else:
        print("The input folder name", dirname, "is not a directory")
else:
    print("The entered directory path", dirname, "does not exists")
print("FASTQ files found: ")
for fqfiles in fastqlist:
    print(fqfiles)

print("Total FASTQ files: ", len(fastqlist))
print("Checking FASTQ files: ")
for fastqs in fastqlist:
    if os.path.isfile(fastqs):
        print(fastqs, "-> Exists")
    else:
        print(fastqs, "-> Does not Exists")
