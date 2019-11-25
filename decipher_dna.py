from body_characteristics import body_characteristics
from suspects import suspects

#read the dna sequence
with open("dna.txt") as input_file:
    dna_sequence = input_file.read()

#check, whether a certain sequence, determining a feature appears in the dna sequence
perpetrator = {}
for i in body_characteristics:
    for j in body_characteristics[i]:
        if dna_sequence.find(body_characteristics[i][j]) != -1:
            perpetrator.update({i: j})  # constructing features of the perpetrator

#check, whether the perpetrator is among the suspects
for i in suspects:
    if suspects[i] == perpetrator:
        print("The perpetrator is: "+i)
