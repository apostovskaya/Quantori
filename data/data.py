from src.db_design import DNA, Codon
from src.db_build import Session

# DNA bases and corresponding RNA bases
dna_to_rna_dict = {}
# translation of DNA bases into RNA bases according to complementarity
dna_to_rna_complement_dict = {}
# RNA base triplets and corresponding amino acids or stop codon (".")
rna_to_aa_dict = {}

with Session() as run_session:
    # extract DNA-RNA and DNA-RNA_complement dictionaries from the DB
    dna_table = run_session.query(DNA).all()
    for row in dna_table:
        dna, rna, rna_complement = str(row).split()
        dna_to_rna_dict[dna] = rna
        dna_to_rna_complement_dict[dna] = rna_complement

    # extract codon (triplet) to amino acid dictionary from the DB
    codon_table = run_session.query(Codon).all()
    for row in codon_table:
        codon, aa = str(row).split()
        rna_to_aa_dict[codon] = aa

# PREVIOUS WAY with manual construction of the dictionaries, without DB
# DNA bases and corresponding RNA bases
# dna_to_rna_dict = {"A": "A", "C": "C", "G": "G", "T": "U"}

# translation of DNA bases into RNA bases according to complementarity
# dna_to_rna_complement_dict = {"A": "U", "C": "G", "G": "C", "T": "A"}

# RNA base triplets and corresponding amino acids or stop codon (".")
# rna_to_aa_dict = {'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
#                   'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
#                   'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
#                   'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
#                   'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
#                   'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
#                   'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
#                   'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
#                   'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
#                   'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
#                   'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
#                   'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
#                   'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
#                   'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
#                   'UAC': 'Y', 'UAU': 'Y', 'UAA': '.', 'UAG': '.',
#                   'UGC': 'C', 'UGU': 'C', 'UGA': '.', 'UGG': 'W',
#                   }
