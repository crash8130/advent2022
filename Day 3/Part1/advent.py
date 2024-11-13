import pathlib  
work_dir = pathlib.Path.cwd()
path =  'puzzle.txt'
f = open(path, 'r')

sum = 0
for i in f:
    both_compartments = i.strip()
    len_of_compartments = len(both_compartments)
    first_compartment = both_compartments[:int(len_of_compartments/2)]
    second_compartment = both_compartments[int(len(both_compartments)/2):]
    shared = set(first_compartment).intersection(set(second_compartment))
    letter = list(shared)[0]
    if ord(letter) > 95:
        sum += ord(letter)-96
    else:
        sum += ord(letter)-38 



# print(ord('a')-96)
# print(ord('A')-38)
print(sum)