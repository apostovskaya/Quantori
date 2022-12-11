import sys
sys.path.extend(
    ['/Users/apost/Documents/CloudMail/PhD_2020/Self-education'
     '/Quantori_Py/Quantori', '/Users/apost/Documents/CloudMail/PhD_2020'
                              '/Self-education/Quantori_Py/Quantori/src',
     '/Users/apost/Documents/CloudMail/PhD_2020/Self-education/'
     'Quantori_Py/Quantori/data'])

import random
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
    if not isinstance(dna, str):
        raise TypeError("Invalid DNA input argument! String is expected.")

    dna = dna.strip().upper()

    # handle invalid method argument
    try:
        method = method.strip().lower()
    except TypeError:
        print(f"Unsupported method is provided: {method}. "
              f"Standard 'transformation' will be performed.")
        method = "transformation"

    # find which method to use for conversion
    if method == "transformation":
        refer_dict = dna_to_rna_dict
    elif method == "transcription":
        refer_dict = dna_to_rna_complement_dict
    else:
        print(f"Unsupported method is provided: {method}. "
              f"Standard 'transformation' will be performed.")
        refer_dict = dna_to_rna_dict

    rna = ""

    # convert each base according to the appropriate conversion method
    try:
        for base in dna:
            rna += refer_dict[base]
    except KeyError:
        raise KeyError(f"Invalid base encountered in DNA: {base}."
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
    if not isinstance(rna, str):
        raise TypeError("Invalid RNA input argument! String is expected.")

    rna = rna.strip().upper()
    protein = ""

    # translate each triplet into amino acid
    try:
        # triplets always have 3 nucleotides, that's biology
        for triplet in range(0, len(rna), 3):
            codon = rna[triplet:triplet + 3]
            if len(codon) == 3:
                protein += rna_to_aa_dict[codon]
    except KeyError:
        raise KeyError(f"Invalid triplet encountered in RNA: {codon}."
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
    if not isinstance(genomic_data, str):
        raise TypeError("Invalid input argument: "
                        "DNA sequence! String is expected.")

    if not isinstance(file_format, str):
        raise TypeError("Invalid input argument: file format! "
                        "String is expected.")

    if not isinstance(bin_size, int):
        raise TypeError("Invalid input argument: subsequence size! "
                        "String is expected.")

    genomic_data = genomic_data.strip("(){}<>[]. ").upper()
    file_format = file_format.strip("(){}<>[]. ").lower()

    # this list will store tuples of values:
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
    plt.xticks(location[::2], rotation=45)
    plt.xlabel("genome position of the last nucleotide of the subsequence")
    plt.ylabel("GC-content in the window, %")
    plt.title(f"GC-content for subsequences of length {bin_size}")
    plt.tight_layout()
    plt.savefig(f"./data/output/gc_content_bins_size{bin_size}.{file_format}")
    plt.close()


if __name__ == "__main__":

    if len(sys.argv) < 1:
        raise Exception("Missing compulsory arguments. "
                        "Expected: script_name DNA_seq [optional: method]")

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

    # mock-up run of GC-content plotting for short sequences
    genome = dna_in
    if len(genome) < 200:
        genome_size = 10**5
        genome *= genome_size
        genome = ''.join(random.sample(genome, len(genome)))

    try:
        len_subsequence = int(sys.argv[3])
        if len(sys.argv) > 4:
            plot_format = sys.argv[4]
            plot_gc_content(genome, len_subsequence, plot_format)
        else:
            plot_format = "png"
            plot_gc_content(genome, len_subsequence)
        print(f"gc_content_bins_size{len_subsequence}.{plot_format} plot "
              f"of GC-content for every subsequence of size {len_subsequence} "
              f"is generated and saved in the ./data/output directory.")
    except IndexError:
        smaller_genome = genome[:5000]
        plot_gc_content(smaller_genome)
        print("The plot of GC-content is generated with the default "
              "parameters: .png format,"
              "GC-content for every subsequence of length 100 bases.")
        print(f"gc_content_bins_size100.png plot is saved "
              f"in the ./data/output directory.")
