f = open('example.txt', 'r')
line = "start"
while line != "":
    line = f.readline()
    print(line)