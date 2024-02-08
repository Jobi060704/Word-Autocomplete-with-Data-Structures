import random

# get parameters
data_size = int(input("Input data size: "))
out_data_name = "data" + str(data_size) + ".txt"
out_in_name   = "test" + str(data_size) + ".in"

empty_exp_name = "test" + str(data_size) + ".exp"

with open('sampleData200k.txt', 'r') as data_file: lines = data_file.readlines()
# create out data and in file
out_data_file = open(out_data_name,'w')
out_in_file = open(out_in_name,'w')

empty_exp_file = open(empty_exp_name,'w')

# add lines to out data file if unique and until its size is not equal to data_size
added_lines = []
while len(added_lines) != data_size:
    rand_line = lines[random.randint(0,len(lines)-1)]
    if rand_line not in added_lines:
        added_lines.append(rand_line)
        out_data_file.write(rand_line)

print(f"Created a datafile named {out_data_name} with size of {len(added_lines)}")


# ADD

a1 = added_lines[random.randint(0,data_size/2)].partition(" ")[0]
a2 = added_lines[random.randint(data_size/2 + 1,data_size)].partition(" ")[0]

out_in_file.write( "A comby 345\n") # not exist
out_in_file.write(f"A {a1} 10\n") # exists
out_in_file.write(f"A {a2} 1000\n") # exists
out_in_file.write( "A superpositioning 55555\n") # not exist

# DELETE

d1 = added_lines[random.randint(0,data_size/2)].partition(" ")[0]
d2 = added_lines[random.randint(data_size/2 + 1,data_size)].partition(" ")[0]

out_in_file.write( "D aiai\n") # not exist
out_in_file.write(f"D {d1}\n") # exists
out_in_file.write(f"D {d2}\n") # exists
out_in_file.write( "D hydroxylaminez\n") # not exist

# SEARCH

s1 = added_lines[random.randint(0,data_size/2)].partition(" ")[0]
s2 = added_lines[random.randint(data_size/2 + 1,data_size)].partition(" ")[0]

out_in_file.write( "S azaza\n") # not exist
out_in_file.write(f"S {s1}\n") # exists
out_in_file.write(f"S {s2}\n") # exists
out_in_file.write( "S semiochemics\n") # not exist

# AUTOCOMPLETE

ac1 = ""
ac2 = ""

while len(ac1) < 5:
    ac1 = added_lines[random.randint(0,data_size/2 - 1)]
    ac1 = ac1.partition(" ")[0]

while len(ac2) < 8:
    ac2 = added_lines[random.randint(data_size/2 + 1,data_size - 1)]
    ac2 = ac2.partition(" ")[0]

ac1 = ac1[:-3]
ac2 = ac2[:-3]

out_in_file.write( "AC sups\n") # not exist
out_in_file.write(f"AC {ac1}\n") # exists
out_in_file.write(f"AC {ac2}\n") # exists
out_in_file.write( "AC whistleblows\n") # not exist

print(f"Created an instruction file named {out_in_name}\n")