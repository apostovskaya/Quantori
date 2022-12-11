# credentials for SQLite DB
db_name = "molbiol_central_dogma"
db_info = f"sqlite:///{db_name}"

# DNA and RNA bases
dna_bases_list = ["A", "C", "G", "T"]
rna_bases_list = ["A", "C", "G", "U"]
rna_complement_bases_list = ["U", "G", "C", "A"]

# Amino acids and all codons corresponding to them
aa_to_codon = {'F': ['UUU', 'UUC'],
               'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
               'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
               'Y': ['UAU', 'UAC'],
               '.': ['UAA', 'UAG', 'UGA'], 'C': ['UGU', 'UGC'], 'W': ['UGG'],
               'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'H': ['CAU', 'CAC'],
               'Q': ['CAA', 'CAG'],
               'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
               'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'],
               'T': ['ACU', 'ACC', 'ACA', 'ACG'],
               'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG'],
               'V': ['GUU', 'GUC', 'GUA', 'GUG'],
               'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'D': ['GAU', 'GAC'],
               'E': ['GAA', 'GAG'],
               'G': ['GGU', 'GGC', 'GGA', 'GGG']}
