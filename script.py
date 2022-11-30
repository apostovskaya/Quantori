import sys
from data.data import \
    dna_to_rna_dict, \
    dna_to_rna_complement_dict, \
    rna_to_aa_dict


def convert_dna_to_rna(dna: str, method='transformation') -> str:
    """
    Converts DNA sequence into RNA sequence.
    In the default 'transform' mode, simple substitution of DNA bases for
    RNA bases is performed. NO proper transcription occurs,
    so no base substitution is done according to complementarity rules.
    In 'transcription' mode, proper transcription with base substitution
    according to complementarity rules is performed.
    :param method: string, specifies the type of conversion (options are:
    transformation, transcription)
    :param dna: string, DNA sequence
    :return: string, RNA sequence
    """
    assert isinstance(dna, str), 'Invalid input argument: DNA sequence! ' \
                                 'String is expected.'
    dna = dna.strip().upper()
    assert isinstance(method, str), 'Invalid input argument: ' \
                                    'conversion method!' \
                                    ' String is expected.'
    method = method.strip().lower()

    rna = ""

    try:
        for base in dna:
            if method == "transformation":
                rna += dna_to_rna_dict[base]
            elif method == "transcription":
                rna += dna_to_rna_complement_dict[base]
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
    :param rna: string, RNA sequence
    :return: string, amino acid sequence
    """
    assert isinstance(rna, str), 'Invalid input argument! String is expected.'
    rna = rna.strip().upper()

    protein = ""
    try:
        for triplet in range(0, len(rna), 3):
            codon = rna[triplet:triplet + 3]
            if len(codon) == 3:
                protein += rna_to_aa_dict[codon]
    except KeyError:
        raise AssertionError(f"Invalid triplet encountered in RNA: {codon}."
                             f"\nExpected one of 4 bases: 'A', 'G', 'C', 'U'."
                             f"\nConverted amino acid sequence is: {protein}")
    return protein


if __name__ == '__main__':
    # expected: script_name DNA_seq [optional: method]
    assert len(sys.argv) >= 1

    dna_in = sys.argv[1]

    # transform or transcribe DNA to RNA
    try:
        convert_method = sys.argv[2]
        rna_out = convert_dna_to_rna(dna_in, convert_method)
        print(f"Conversion of DNA to RNA: {convert_method}: {rna_out}")
    except IndexError:
        rna_out = convert_dna_to_rna(dna_in)
        print(f"Conversion of DNA to RNA: transformation: {rna_out}")

    # translate RNA to protein
    protein_out = convert_rna_to_protein(rna_out)
    print(f"Translation of RNA to protein: {protein_out}")
