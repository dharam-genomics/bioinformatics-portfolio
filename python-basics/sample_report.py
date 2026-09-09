samples = ["S1", "S2", "S3", "S4"]
reads = [100, 40, 80, 20]

for sample, read in zip(samples, reads):
    if read >= 80:
        print(sample, read, "PASS")
    else:
        print(sample, read, "FAIL")
