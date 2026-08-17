import os
import sys
def find_fastq(directory):
    fastqlist = []
    filelist = os.listdir(directory)
    for filename in filelist:
        if filename.endswith(".fastq"):
            name = os.path.join(directory, filename)
            fastqlist.append(name)
    return fastqlist

if len(sys.argv) < 2:
    print("Please enter the directory name.")
    sys.exit(1)
else:
    dirname = sys.argv[1]
    if os.path.isdir(dirname):
        fqlist = find_fastq(dirname)
    else:
        print("The entered name", dirname, "is not a directory!")
        sys.exit(1)
print("The FASTQ files found: ")
for files in fqlist:
    print(files)

print("Total FASTQ files: ", len(fqlist))
