genes = []
with open("genes.txt", "r") as file:
    for line in file:
        gene = line.strip()
        genes.append(gene)

    print("The complete list is:", genes, "\n And the length of genes list is:", len(genes))


