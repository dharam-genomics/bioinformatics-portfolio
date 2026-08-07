genes = {"BRCA1":"chr17", "TP53":"chr17", "CFTR":"chr7"}
print("Printing the original dictionary:")
print(genes)
genes["HBB"] = "chr3"
print("Checking if HBB gene exists in the dictionary:")
print("HBB" in genes)
print("Printing the updated dictionary:")
print(genes)
genes["TP53"] = "chr16"
print("Printing the updated dictionary after updating the value of TP53 gene(using for loop):")
for gene in genes:
    print(gene)
print("Printing the key value pair using .items() function:")
for gene, chromosome in genes.items():
    print(gene, chromosome)
print("Printing only keys using .keys() function:")
for gene in genes.keys():
    print(gene)
print("Printing only the values using the .values() function:")
for gene in genes.values():
    print(gene)
print("Printing the dictionary after deleting the gene TP53 using 'del':")
del genes["TP53"]
print(genes)
genes["TPP1"] ={"ref" : "A", "alt" : "G", "depth" : 56}
print("Added a new key with nasted dictionary, Printing the update dictionary:")
print(genes)
print("Printing the newly added key (which is a dictionary):")
print(genes["TPP1"])
print("Printing the values from the nasted dictionary:")
print(genes["TPP1"]["ref"])
