vaf =0.80
coverage = 90
depth = 100
readlength = 50
gene = "BRCA1"
sampletype = "blood"
if(vaf <= .50):
    print("Hetrozygous")
else:
    print("Homozygous")
if(coverage >= 90):
    if(gene == "BRCA1"):
        print("gene is", gene)
    else:
        print("gene is not listed")
    print("Very good coverage")
elif(coverage >= 80):
    print("Coverage passed")
else:
    print("coverage failed")
if(depth >= 80):
    if(sampletype == "blood"):
        print("sample type is", sampletype)
    else:
        print("Unknown sample type")
    print("Depth is excellent!")
elif(depth >= 30):
    print("Depath is good")
else:
    print("Depth failed")

