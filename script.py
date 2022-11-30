import sys
import matplotlib.pyplot as plt
from data.data import \
    dna_to_rna_dict, \
    dna_to_rna_complement_dict, \
    rna_to_aa_dict


def convert_dna_to_rna(dna: str, method="transformation") -> str:
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
    assert isinstance(dna, str), "Invalid input argument: DNA sequence! " \
                                 "String is expected."
    dna = dna.strip().upper()
    assert isinstance(method, str), "Invalid input argument: " \
                                    "conversion method!" \
                                    " String is expected."
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
    assert isinstance(rna, str), "Invalid input argument! String is expected."
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


def plot_gc_content(genomic_data: str, bin_size: int = 100,
                    file_format: str = "png"):
    """
    Plots G-C ratio (GC-content in %) of every subsequence
    of the requested size in a DNA molecule
    and saves the plot in a file (.png  by default). The function doesn't check
    the correctness of nucleotides, any letter will be accepted.
    :param file_format: str, desired file format of the produced plot
    (.png  by default)
    :param genomic_data: string, a nucleotide sequence (genomic data)
    :param bin_size: int, denotes a width of a bin (default is 100 characters)
    :return: saves plot in the current directory
    """
    assert isinstance(genomic_data, str), "Invalid input argument: " \
                                          "DNA sequence! String is expected."
    genomic_data = genomic_data.strip().upper()

    assert isinstance(file_format, str), "Invalid input argument: " \
                                         "file format! String is expected."
    file_format = file_format.strip().lower()

    assert isinstance(bin_size, int), "Invalid input argument: " \
                                      "subsequence size! Integer is expected."

    # will store tuples of values:
    # position of the last nucleotide of the subsequence in the full sequence,
    # GC-content in %
    gc_all_bins = []

    for bin_start in range(0, len(genomic_data), bin_size):
        bin_end = bin_start + bin_size
        one_bin = genomic_data[bin_start:bin_end]
        # calculate gc-content for every bin of requested size only
        if len(one_bin) == bin_size:
            one_gc = 100 * (one_bin.count("C") + one_bin.count("G")) \
                     / len(one_bin)
            gc_all_bins.append((bin_end, int(one_gc)))

    # plotting
    location, content = zip(*gc_all_bins)
    plt.plot(location, content, linestyle="--", marker=".", color="tab:blue")
    plt.xticks(location[::2])
    plt.xlabel("genome position of the last nucleotide of the subsequence")
    plt.ylabel("GC-content in the window, %")
    plt.title(f"GC-content for subsequences of length {bin_size}")
    plt.tight_layout()
    plt.savefig(f"./gc_content_bins_size{bin_size}.{file_format}")
    plt.close()


if __name__ == "__main__":
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
