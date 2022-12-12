## Quantori Python School Final Project

### Summary
The app provides the following functionality:
* DNA to RNA transformation or transcription;
* RNA to peptide translation;
* Calculating and plotting GC-content in a DNA sub-sequence of a given length.

The project was built incrementally using *Python*, *SQLAlchemy*, *Matplotlib*, *PostgreSQL*, *Docker*, *Unittest*.

The project consisted of 5 sub-goals.

### Part 1: Functions
A script *script.py* with two functions inside: convert_dna_to_rna and convert_rna_to_protein that model these two processes. 
These functions have a string sequence as input and output.
The data describing how DNA<->RNA and RNA<->amino_acid conversion is performed are in the /data/data.py.

1. ```convert_dna_to_rna```

Converts DNA sequence into RNA sequence.
In the default 'transform' mode, simple substitution of DNA bases for
RNA bases is performed. NO proper transcription occurs,
so no base substitution is done according to complementarity rules.
In 'transcription' mode, proper transcription with base substitution
according to complementarity rules is performed.
- :param method: string, specifies the type of conversion (options are:
transformation, transcription)
- :param dna: string, DNA sequence
- :return: string, RNA sequence

**DNA -> RNA input and output examples**
- ATTTGGCTACTAACAATCTA -> AUUUGGCUACUAACAAUCUA
- GTTGTAATGGCCTACATTA -> GUUGUAAUGGCCUACAUUA
- CAGGTGGTGTTGTTCAGTT -> CAGGUGGUGUUGUUCAGUU
- GCTAACTAAC -> GCUAACUAAC
- GCTAACTAACATCTTTGGCACTGTT -> GCUAACUAACAUCUUUGGCACUGUU
- TATGAAAAACTCAAA -> UAUGAAAAACUCAAA
- CCCGTCCTTGATTGGCTTGAAGAGAAGTTT -> CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU

2. ```convert_rna_to_protein```

Converts RNA sequence (each RNA base triplet) into amino acid sequence
according to translation rules. Stop codon is represented by a '.'
but does not result in abortion of the translation,
it is included in the sequence the same way as one of the amino acids.
- :param rna: string, RNA sequence
- :return: string, amino acid sequence

**RNA -> protein input and output examples**

- AUUUGGCUACUAACAAUCUA -> IWLLTI
- GUUGUAAUGGCCUACAUUA -> VVMAYI
- CAGGUGGUGUUGUUCAGUU -> QVVLFS
- GCUAACUAAC -> AN.
- GCUAACUAACAUCUUUGGCACUGUU -> AN.HLWHC
- UAUGAAAAACUCAAA -> YEKLK
- CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU -> PVLDWLEEKF

### Part 2: Database
The data describing how DNA<->RNA and RNA<->amino_acid conversion is performed is now put in a database with 4 tables:
- dna_table (contains 4 bases that form a DNA sequence: A, C, G, and T)
- rna_table (and rna_complement_table).
The table rna_table contains 4 bases that form an RNA sequence and is connected to the first table with one-to-one relation
(simple substitution of DNA bases for RNA bases).
Similarly for rna_complement_table but in this case, DNA bases are connected to complementary RNA bases (transcription rules).
- codon_table
- amino_acids_table: is linked to codon_table according to the rules of translation. 

All the code that manages the database is in the /data directory. 

### Part 3: Plots
Sometimes in bioinformatics GC-content metric is of interest: https://en.wikipedia.org/wiki/GC-content

The bond that forms between G and C bases is particularly strong. In regions of the molecule, that are rich in G and C bases, 
two DNA strands hold together better, which influences the melting temperature that needs to be selected for PCR.

A function that plots G-C ratio in a DNA molecule and saves the resulting plot to a .png or .jpeg file is created in script.py.

The horizontal axis of the graph represents the genome position. The vertical axis shows the G-C ratio in the window. The default size of a window is 100 bases.

```plot_gc_content```

Plots G-C ratio (GC-content in %) of every subsequence of the requested size in a DNA molecule 
and saves the plot in a file (.png  by default). The function doesn't check
the correctness of nucleotides, any letter will be accepted.
```
- :param file_format: str, desired file format of the produced plot (.png  by default)
- :param genomic_data: string, a nucleotide sequence (genomic data)
- :param bin_size: int, denotes a width of a bin (default is 100 characters)
- :return: saves plot in the current directory
```

### Part 4: Docker
- The app is packed into a Docker container.
- The previously created database is migrated to Postgres. This database is created in the second container.
Pending:
Add a command-line arguments to your Python app, so that all the functions you wrote in Part 1 and Part 3 could be run from the command line.
Add all the commands that run Docker and the app to the Readme

### Part 5: Tests
Write unit tests for functions from parts 1 & 3.

## How to run
### -without Docker:
1. in *db_config.py*, comment credentials for Postgres DB and release credentials for SQLite DB
2. from Qunatori directory as working directory, run

```python3 ./app/script.py [required: param1] [optional: param2] [optional: param3] [optional: param4]```

- param1 = DNA sequence (string)
- param2 = mode: transformation or transcription of DNA to RNA (string)
- param3 = length of subsequence for GC-content calculations (int)
- param4 = format in which to save GC-content plot (string, Ex: "jpeg"")

**Example:**

```python3 ./app/script.py "ATTTGGCTACTAACAATCTA" "transcription" 5```