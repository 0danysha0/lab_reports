# install EMBOSS for searching orf's
# install biopython
# in bash
getorf -sequence 10000.fasta -outseq orf_cov.fasta  #10000.fasta it's longest contig in first homework file, it's for example
#ok, now i have file with orf's which include amino acid sequences
#in python inside bash
from Bio import SeqIO

def find_coding_sequences(orf_file):
    coding_sequences = []

    for record in SeqIO.parse(orf_file, "fasta"):
        protein_sequence = str(record.seq)
      
        if protein_sequence.startswith("M") and len(protein_sequence) >= 33:  #it's not good, but it's only cretereas which was in my head
            coding_sequences.append(protein_sequence)

    return coding_sequences

protein_file = "orf_cov.fasta"  
coding_sequences = find_coding_sequences(orf_file)

for i, seq in enumerate(coding_sequences):
    print(f"Coding Sequence {i + 1}: {seq}")
  #in bash i created txt file which consist coding sequences with given criteria
