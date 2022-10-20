from Bio import SeqIO
import os

class filteren():
    def __init__(self, tekstbestand,i):
        self.tekstbestand = tekstbestand

        self.__i = i
        self.openen()

        self.lijst_acc = []

    def openen(self):

        fasta_sequences = SeqIO.parse(open(self.tekstbestand), 'fasta')

        for fasta in fasta_sequences:
            acc,naam, sequence = fasta.id,fasta.description, str(fasta.seq)
            #print(acc,naam)
            if ((("Neuraminidase" in naam or "NA" in naam
                  or "neuramindase" in naam or "neuraminidase" in naam
                  or "neuramidinase" in naam or "neuramidase" in naam
                  or "neuroaminidase" in naam ) and "Influenza" in naam)
                    or "hypothetical protein" in naam
                    or "synthetic construct" in naam
                    or "unidentified influenza virus" in naam
                    or "partial" in naam):
                continue
            else:
                with open("seqtest.txt","a") as file:
                    file.write(">")
                    file.write(naam)
                    file.write("\n")
                    file.write(sequence)
                    file.write("\n")

class os_systeem():

    def __init__(self,i):
        self.__i = i
        #self.msa()
        #self.hmm()
        self.__bestandnaam = 'output.fa'
        self.gethmmseq()

    def msa(self):
        if self.__i == 0:
            #os.system(
                #"mafft sequenties.txt > cycle" + str(self.__i + 1) + ".txt")
            print("123")
        else:
            #os.system("mafft cycle" + str(self.__i) + ".fa > cycle" + str(
            #    self.__i + 1) + ".txt")
            print("123")
    def hmm(self):
        os.system(
            "hmmbuild cycle" + str(self.__i + 1) + ".hmm cycle" + str(self.__i + 1) + ".txt")
        os.system("hmmsearch -A cycle" + str(self.__i + 1) + ".sto cycle" + str(
            self.__i + 1) + ".hmm Storage/bin-2/nr_db_ncbi")
        self.__bestandnaam = "cycle" + str(self.__i + 1) + ".fa"

        os.system("esl-reformat fasta cycle" + str(self.__i + 1) + ".sto > "  + self.__bestandnaam)

            #"esl-reformat fasta cycle" + str(self.__i + 1) + ".sto > cycle" + str(
              #  self.__i + 1) + ".fa")
        print("123")
        #self.__bestandnaam = "seqtest2.fa"

    def gethmmseq(self):
        return self.__bestandnaam

def main():

    repeats = 8
    for i in range(repeats):
        os = os_systeem(i)
        bestand = os.gethmmseq()
        filteren(bestand,i)


main()

