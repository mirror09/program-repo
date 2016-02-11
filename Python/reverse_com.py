# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    rev=Pattern[::-1]
    revComp=complement(rev)
    return revComp


# Copy your reverse function from the previous step here.


# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    for i in range(0, len(Nucleotide)):
            if Nucleotide[i] == "T":
                comp += "A"

            if Nucleotide[i] == "A":
                comp += "T"

            if Nucleotide[i] == "G":
                comp += "C"

            if Nucleotide[i] == "C":
                comp += "G"
    return comp

Text="CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
print(ReverseComplement(Text))
