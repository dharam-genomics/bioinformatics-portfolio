from sequence_tools import sequence_length
sequence = input("Enter the sequence to check lenght: ")
length, g_count, gc_content = sequence_length(sequence)
print("The sequence length is :", length)
print("The G count is :", g_count)
print("The GC content is :", gc_content)
