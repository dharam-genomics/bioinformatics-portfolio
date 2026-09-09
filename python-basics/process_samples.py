samples = ["sample1", "sample2", "invalid_sample", "sample3"]
for sample in samples:
    if sample == "invalid_sample":
        continue
    print("Processing:", sample)
