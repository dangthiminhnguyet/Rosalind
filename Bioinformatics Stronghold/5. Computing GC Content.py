from Bio import SeqIO
def count1(dna):
     i = 0
     i2 = 0
     for c in dna:
         if c == 'G' or c == 'C': i2 += 1
         i += 1
     return round((float(i2)/float(i)*100),6)
fasta_sequences = SeqIO.parse(open('C:/Users/MinhNguyet/Downloads/rosalind_gc.txt'),'fasta')
kk=0
meoz=0
for seq_record in fasta_sequences:
     kk=count1(seq_record.seq)
     if kk>=meoz:
          meoz=kk
          l=seq_record.id
print l
print meoz
