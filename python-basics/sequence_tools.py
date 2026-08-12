def sequence_length(value):
    count_g = 0
    count_c = 0
    length = len(value)
    for base in value:
        if base == "G":
            count_g += 1
        elif base == "C":
            count_c += 1
    total_gc = count_g + count_c
    gc_content = (total_gc / length) * 100
    return length, count_g, gc_content
