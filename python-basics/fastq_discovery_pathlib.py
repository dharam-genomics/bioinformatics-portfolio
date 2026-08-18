import sys
from pathlib import Path
def find_fastq(directory):
    fastqlist = []
    data = Path(directory)
    for file in data.iterdir():
        if file.suffix == ".fastq":
            fastqlist.append(file)
    return fastqlist

if len(sys.argv) < 2:
    print("Enter a directory name!!!")
    sys.exit(1)
dir_name = Path(sys.argv[1])

if not dir_name.is_dir():
    print("Please enter a valid directory name!!!")
    sys.exit(1)
fqlist = find_fastq(dir_name)
print("The FASTQ list is: ")
for item in fqlist:
    print(item)
print("The Total FASTQ count:", len(fqlist))
