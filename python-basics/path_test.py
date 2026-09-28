from pathlib import Path

data_dir = Path("data")

fastq_files = data_dir.glob("*.fastq")

for file in fastq_files:
    print(file)
#data_dir = Path("data/sample1.fastq")
#print(data_dir)
#print(data_dir.exists())
#print(data_dir.is_dir())
#print(data_dir.is_file())
#print(data_dir.name)
#print(data_dir.suffix)
#path = Path("sample.fastq")
#
#print(path)
#print(path.exists())
#print(path.name)
#print(path.suffix)
