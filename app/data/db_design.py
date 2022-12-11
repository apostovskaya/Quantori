from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class DNA(Base):
    """The table of DNA bases (one-to-one relationship to the tables
    with corresponding RNA bases and RNA complementary bases)"""
    __tablename__ = 'dna_table'
    # to update existing objects
    __tablearg__ = {"extend_existing": True}

    dna_base_id = Column(Integer, primary_key=True)
    rna_base_id = Column(Integer, ForeignKey("rna_table.rna_base_id"))
    rna_complement_base_id = \
        Column(Integer,
               ForeignKey("rna_complement_table.rna_complement_base_id"))
    dna_base = Column(String(1))
    rna_base = relationship("RNA", back_populates="dna_base", uselist=False)
    rna_complement_base = relationship("RNAcomplement",
                                       back_populates="dna_base",
                                       uselist=False)

    def __str__(self) -> str:
        return f"{self.dna_base} {self.rna_base} {self.rna_complement_base}"


class RNA(Base):
    """The table of RNA bases corresponding to DNA bases
    (one-to-one relationship to DNA table)"""
    __tablename__ = 'rna_table'
    __tablearg__ = {"extend_existing": True}

    rna_base_id = Column(Integer, primary_key=True)
    rna_base = Column(String(1))
    dna_base = relationship("DNA", back_populates="rna_base", uselist=False)

    def __str__(self) -> str:
        return f"{self.rna_base}"


# I didn't manage to figure out the correct way to build one RNA-database, so
# making two separate ones
class RNAcomplement(Base):
    """The table of RNA bases complementary to DNA bases
    (one-to-one relationship to DNA table)"""
    __tablename__ = 'rna_complement_table'
    __tablearg__ = {"extend_existing": True}

    rna_complement_base_id = Column(Integer, primary_key=True)
    rna_complement_base = Column(String(1))
    dna_base = relationship("DNA", back_populates="rna_complement_base",
                            uselist=False)

    def __str__(self) -> str:
        return f"{self.rna_complement_base}"


class Codon(Base):
    """The table of codons (triplets) corresponding to amino acids in
    amino_acid_table (many-to-one relationship to amino_acids table)"""
    __tablename__ = 'codon_table'
    __tablearg__ = {"extend_existing": True}

    codon_id = Column(Integer, primary_key=True)
    codon = Column(String(3))
    amino_acid = relationship("AminoAcid", back_populates="codon")
    amino_acid_id = Column(Integer,
                           ForeignKey("amino_acid_table.amino_acid_id"))

    def __str__(self) -> str:
        return f"{self.codon} {self.amino_acid}"


class AminoAcid(Base):
    """The table of Amino acids (one-to-many relationship to codon_table)"""
    __tablename__ = 'amino_acid_table'
    __tablearg__ = {"extend_existing": True}

    amino_acid_id = Column(Integer, primary_key=True)
    amino_acid = Column(String(1))
    codon = relationship("Codon", back_populates="amino_acid")

    def __str__(self) -> str:
        return f"{self.amino_acid}"
