with open('tmv.gene', "r+") as f:
    clean_gene = f.readlines()[0]

    print clean_gene.upper()


