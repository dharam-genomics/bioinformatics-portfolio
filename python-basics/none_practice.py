def check_sample(sample):
    if sample == "sample1":
        return "PASS"
    return None

sample_check = check_sample("sample1")
if sample_check is None:
    print("Sample not found")
else:
    print("Sample:", sample_check)
