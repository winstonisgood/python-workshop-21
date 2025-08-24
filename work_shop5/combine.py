file_name = input("Please enter the file name you want to combine: ")
try:
    fA = open("./data/" + file_name + "-A.txt","rt")
    fB = open("./data/" + file_name + "-B.txt","rt")
    filename_out = open(file_name + "-out.txt","at")
except FileNotFoundError:
    print("File not found")
while True:
    odd_line = fA.readline()     
    even_line = fB.readline()
    if not odd_line and not even_line:
        break
    filename_out.write(odd_line)
    filename_out.write(even_line)   
fA.close()
fB.close()
filename_out.close()


