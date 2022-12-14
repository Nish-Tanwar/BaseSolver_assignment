from Bio.Seq import Seq, MutableSeq
from Bio import SeqIO
#parsed the file in the form of list
r = list(SeqIO.parse("C:/Users/LENOVO/Downloads/MonkeyPox.fn.txt", "fasta"))
#selected second sequence of the multifasta file
s = r[1].seq
print(s)
#reversed complement the original extracted sequence
rc = s.reverse_complement()
print(rc)
#Inserted a mutation on first position in the original extracted sequence
mutable_seq = s.tomutable()
mutable_seq.insert(0, 'A')
print(mutable_seq)
#r.append(mutable_seq)
seqs = []
i = []
for record in SeqIO.parse("C:/Users/LENOVO/Downloads/MonkeyPox.fn.txt","fasta"):
        seqs.append(str(record.seq))
        i.append(record.id)

seqs.append(mutable_seq)
i.append("New Seq")
SeqIO.write(seqs,"C:/Users/LENOVO/Downloads/abc.fn.txt","fasta")
#bed file generation
with open("C:/Users/LENOVO/Downloads/regions.bed","w") as bed:
        for record in parse("C:/Users/LENOVO/Downloads/MonkeyPox.fn.txt", "fasta"):
                print(record.id, len(record.seq), sep="\t", file=bed)