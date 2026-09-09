def get_status(sample):
    if sample == "sample1":
        return "PASS"
    elif sample == "sample2":
        return "FAIL"
    else:
        return None

status = get_status("sample3")
if status is None:
    print("Status unavailable")
