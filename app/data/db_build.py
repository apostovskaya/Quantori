from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_design import AminoAcid, Codon, DNA, RNA, RNAcomplement, Base
from db_config import aa_to_codon, db_info, dna_bases_list, rna_bases_list, \
    rna_complement_bases_list

engine = create_engine(db_info)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

aminoacids_list = list(aa_to_codon.keys())

with Session() as build_session:
    # fill in the DNA and RNA tables with the respective bases
    for rna_base, dna_base, rna_complement_base in \
            zip(rna_bases_list, dna_bases_list, rna_complement_bases_list):
        rna_base_entry = RNA(rna_base=rna_base)
        build_session.add(rna_base_entry)
        rna_complement_base_entry = RNAcomplement(
            rna_complement_base=rna_complement_base)
        build_session.add(rna_complement_base_entry)
        dna_base_entry = DNA(dna_base=dna_base, rna_base=rna_base_entry,
                             rna_complement_base=rna_complement_base_entry)
        build_session.add(dna_base_entry)

    # fill in the Codon and AminoAcid tables
    for aa, codons in aa_to_codon.items():
        aa_entry = AminoAcid(amino_acid=aa)
        build_session.add(aa_entry)
        for codon in codons:
            codon_entry = Codon(codon=codon, amino_acid=aa_entry)
            build_session.add(codon_entry)

        build_session.commit()
