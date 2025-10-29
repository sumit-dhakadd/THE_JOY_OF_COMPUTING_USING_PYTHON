import string

dict = {}
data = ""

# Create output file
file = open("op_file.txt", "w")

# Create substitution dictionary (maps each ASCII letter to another)
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i - 1]

print(dict)

# Read input file and perform substitution
with open("ip_file.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        file.write(data)
        print(data)

file.close()