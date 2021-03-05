from itertools import zip_longest
from textwrap import wrap


def count_bases(seq):
    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")

    nucleotide_sum = A + C + G + T
    return nucleotide_sum, A, C, G, T


def translate_to_prot(seq):
    rna_seq = seq.replace("T", "U")
    data = wrap(rna_seq, 3)

    INPUT = ["GCU", "GCC", "GCA", "GCG", "UGU", "UGC", "GAU",
             "GAC", "GAA", "GAG", "UUU", "UUC", "GGG", "GGC",
             "GGA", "GGU", "CAU", "CAC", "AUU", "AUC", "AUA",
             "AAA", "AAG", "UUA", "UUG", "CUA", "CUU", "CUC",
             "CUG", "AUG", "AAU", "AAC", "CCU", "CCC", "CCA",
             "CCG", "CAA", "CAG", "CGU", "CGC", "CGA", "CGG",
             "AGA", "AGG", "UCA", "UCC", "UCG", "UCU", "AGU",
             "AGC", "ACU", "ACA", "ACC", "ACG", "GUU", "GUG",
             "GUA", "GUC", "UGG", "UAU", "UAC"]

    OUTPUT = ["A", "A", "A", "A", "C", "C", "D", "D", "E", "E",
              "F", "F", "G", "G", "G", "G", "H", "H", "I", "I",
              "I", "K", "K", "L", "L", "L", "L", "L", "L", "M",
              "N", "N", "P", "P", "P", "P", "Q", "Q", "R", "R",
              "R", "R", "R", "R", "S", "S", "S", "S", "S", "S",
              "T", "T", "T", "T", "V", "V", "V", "V", "W", "Y",
              "Y"]

    prot_seq = ""

    for bases in data:
        for i, o in zip_longest(INPUT, OUTPUT):
            if i == bases:
                prot_seq += o

    return prot_seq


def find_mutations(origin_seq, mut_seq):
    num_of_mut = 0
    for i in range(0, len(origin_seq)):
        if origin_seq[i] == mut_seq[i]:
            continue
        else:
            num_of_mut += 1
    return num_of_mut
