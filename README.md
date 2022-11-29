# Quantori

## Part 1: Functions
Write a script script.py with two functions inside: convert_dna_to_rna and convert_rna_to_protein that model these two processes. These functions must have a string sequence as input and output.
For these functions to work, you'll probably need data describing how DNA and RNA bases correspond, and same for RNA <-> protein conversion. Put these files in the /data directory in the project root.
### Examples
1. DNA -> RNA input and output examples:

ATTTGGCTACTAACAATCTA -> AUUUGGCUACUAACAAUCUA

GTTGTAATGGCCTACATTA -> GUUGUAAUGGCCUACAUUA

CAGGTGGTGTTGTTCAGTT -> CAGGUGGUGUUGUUCAGUU

GCTAACTAAC -> GCUAACUAAC

GCTAACTAACATCTTTGGCACTGTT -> GCUAACUAACAUCUUUGGCACUGUU

TATGAAAAACTCAAA -> UAUGAAAAACUCAAA

CCCGTCCTTGATTGGCTTGAAGAGAAGTTT -> CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU

2. RNA -> protein input and output examples:

AUUUGGCUACUAACAAUCUA -> IWLLTI

GUUGUAAUGGCCUACAUUA -> VVMAYI

CAGGUGGUGUUGUUCAGUU -> QVVLFS

GCUAACUAAC -> AN.

GCUAACUAACAUCUUUGGCACUGUU -> AN.HLWHC

UAUGAAAAACUCAAA -> YEKLK

CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU -> PVLDWLEEKF



## Part 2: Database
For the functions that we requested in the first part, you surely needed some data describing how DNA and RNA bases correspond,
and same for RNA <-> protein conversion.
We asked you to put these files in the /data directory in the project root.

Now we want you to create a database with three tables that will store this data: 

dna_bases 
rna_bases 
amino_acids 
Table dna_bases should contain four bases that form a DNA sequence: A, C, G, and T. Table rna_bases should contain bases that form an RNA sequence and should be connected to the first table with one-to-one relation. Link the amino_acids table to rna_bases in a similar fashion. 

Use this database in your code instead of the files you've used before.

Put all the code that manages the database (create/access/change/...) into a separate file (or files) in the /data directory. 

## Part 3: Plots
Sometimes in bioinformatics we are interested in the GC-content metric:

https://en.wikipedia.org/wiki/GC-content

The bond that forms between G and C bases is particularly strong. In regions of the molecule, that are rich in G and C bases, two DNA strands hold together better, which influences the melting temperature that we have to select for PCR.

Let's analyse GC-content ratio in our project! GC-content is calculated as

where
G is the number of G-bases in the selected region (it may be the whole molecule or it's part)
C is the number of C-bases
and so on.

Write a function that plots G-C ratio in a DNA molecule has and saves the resulting graph to a .png or .jpeg file.

The horizontal axis of this graph should be the genome position. The vertical axis should be the G-C ratio in the window. Let the default size of a window be 100 bases.

The function must take parameters:
string: genomic data as a string,
step: int parameter, denoting a width of a bin with a default value of 100 characters.

## Part 4: Docker
it's the most challenging one

Pack your app into a Docker container
Create a Postgres database in the second container (Roman shared an example how to do it above in the chat)
Migrate the previously created SQLAchemy database to Postgres
Add a command-line arguments to your Python app, so that all the functions you wrote in Part 1 and Part 3 could be run from the command line (you can find an example here)
Add all the commands that run Docker and the app to the Readme

## Part 5: Tests
