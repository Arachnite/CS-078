
# Brandon Jun // COMSC 078 // Trees & Dictionaries

AMINO_ACIDS = {
    'TTT': 'Phe', 'TCT': 'Ser', 'TGT': 'Cys', 'TAT': 'Tyr',
    'TTC': 'Phe', 'TCC': 'Ser', 'TGC': 'Cys', 'TAC': 'Tyr',
    'TTG': 'Leu', 'TCG': 'Ser', 'TGG': 'Trp', 'TAG': '***',
    'TTA': 'Leu', 'TCA': 'Ser', 'TGA': '***', 'TAA': '***',

    'CTT': 'Leu', 'CCT': 'Pro', 'CGT': 'Arg', 'CAT': 'His',
    'CTC': 'Leu', 'CCC': 'Pro', 'CGC': 'Arg', 'CAC': 'His',
    'CTG': 'Leu', 'CCG': 'Pro', 'CGG': 'Arg', 'CAG': 'Gln',
    'CTA': 'Leu', 'CCA': 'Pro', 'CGA': 'Arg', 'CAA': 'Gln',

    'GTT': 'Val', 'GCT': 'Ala', 'GGT': 'Gly', 'GAT': 'Asp',
    'GTC': 'Val', 'GCC': 'Ala', 'GGC': 'Gly', 'GAC': 'Asp',
    'GTG': 'Val', 'GCG': 'Ala', 'GGG': 'Gly', 'GAG': 'Glu',
    'GTA': 'Val', 'GCA': 'Ala', 'GGA': 'Gly', 'GAA': 'Glu',

    'ATT': 'Ile', 'ACT': 'Thr', 'AGT': 'Ser', 'AAT': 'Asn',
    'ATC': 'Ile', 'ACC': 'Thr', 'AGC': 'Ser', 'AAC': 'Asn',
    'ATG': 'Met', 'ACG': 'Thr', 'AGG': 'Arg', 'AAG': 'Lys',
    'ATA': 'Ile', 'ACA': 'Thr', 'AGA': 'Arg', 'AAA': 'Lys',
}


def clean_sequence(text):

    result = ''
    for ch in text:
        if ch.isalpha():
            result = result + ch.upper()
    return result


def translate(sequence):

    i = 0
    while i < len(sequence):
        triple = sequence[i:i + 3]
        if triple in AMINO_ACIDS:
            print(triple, AMINO_ACIDS[triple])
        else:
            print(triple, 'invalid sequence')
        i = i + 3


def main():

    prompt = "Enter a nucleotide sequence, or just press ENTER to quit: "

    while True:

        text = input(prompt)
        sequence = clean_sequence(text)
        if len(sequence) == 0:
            break
        elif len(sequence) % 3 != 0:
            print("Error: You must give complete triples.")
        else:
            translate(sequence)
        print()


main()