selected_genes = []
with open("genes.txt", "r") as file:
    for line in file:
        gene = line.strip()
        if gene == "BRCA1" or gene == "TP53":
            selected_genes.append(gene)
print(selected_genes)
with open("selected_genes.txt", "w") as file:
    for line in selected_genes:
        file.write(line + "\n")
