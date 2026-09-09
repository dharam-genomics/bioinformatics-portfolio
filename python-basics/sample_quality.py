def check_quality(reads):
    if reads >= 100:
        return "EXCELLENT"
    elif reads >= 50:
        return "PASS"
    else:
        return "FAIL"

status = check_quality(75)
print("Sample status:", status)

