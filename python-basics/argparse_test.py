import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--min-reads", type=int, required=True)
args = parser.parse_args()
print("Input:", args.input)
print("Minimum Reads:", args.min_reads)
