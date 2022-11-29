from data import dna_to_rna_dict, rna_to_aa_dict


def convert_dna_to_rna(dna: str) -> str:
    """
    Converts DNA sequence into RNA sequence.
    Simple substitution of DNA bases for RNA bases.
    DOES NOT perform proper transcription, so no base substitution is done
    according to complementarity rules.
    :param dna: string
    :return: string, RNA sequence
    """
    assert isinstance(dna, str), 'Invalid input argument! String is expected.'
    dna = dna.strip().upper()

    rna = ""
    try:
        for base in dna:
            rna += dna_to_rna_dict[base]
    except KeyError:
        raise AssertionError(f"Invalid base encountered in DNA: {base}."
                             f"\nExpected one of 4 bases: 'A', 'G', 'C', 'T'."
                             f"\nConverted RNA sequence is: {rna}")
    return rna


def convert_rna_to_protein(rna: str) -> str:
    """
    Converts RNA sequence (each RNA base triplet) into amino acid sequence
    according to translation rules. Stop codon is represented by a '.'
    but does not result in abortion of the translation,
    it is included in the sequence the same way as one of the amino acids.
    :param rna: RNA sequence
    :return: amino acid sequence
    """
    assert isinstance(rna, str), 'Invalid input argument! String is expected.'
    rna = rna.strip().upper()

    peptide = ""
    try:
        for triplet in range(0, len(rna), 3):
            codon = rna[triplet:triplet+3]
            if len(codon) == 3:
                peptide += rna_to_aa_dict[codon]
    except KeyError:
        raise AssertionError(f"Invalid triplet encountered in RNA: {codon}."
                             f"\nExpected one of 4 bases: 'A', 'G', 'C', 'U'."
                             f"\nConverted amino acid sequence is: {peptide}")
    return peptide
