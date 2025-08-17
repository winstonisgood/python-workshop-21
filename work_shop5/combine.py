file_name = input("Please enter the file name you want to combine: ")
try:
    f1 = open("./data/" + file_name + "-A.txt","rt")
    f2 = open("./data/" + file_name + "-B.txt","rt")
    filename_out = open(file_name + "-out.txt","at")
except FileNotFoundError:
    print("File not found")
line_num_odd = 1
line_num_even = 1
while True:
    odd_line = f1.readline() 
    if not odd_line:
        break
    if line_num_odd %2 ==1:
        filename_out.write(odd_line)
    line_num_odd += 1
    even_line = f2.readline()
    if not even_line:
        break
    if line_num_even %2 ==0:
        filename_out.write(even_line)
    line_num_even += 1
f1.close()
f2.close()
filename_out.close()


