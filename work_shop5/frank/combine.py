def line_write_file(lines:list, line_len:int, line_num:int, written_file):
    if line_num < line_len:
        written_file.write(f"{line_num:}{lines[line_num]}")
        
file_name_prefex = input("Enter the prefix for the file names: ")
file_a= f"../data/{file_name_prefex}-A.txt"
file_b= f"../data/{file_name_prefex}-B.txt"

try:        
    with open(file_a, "r") as f_a, open(file_b, "r") as f_b:
        lines_a = f_a.readlines()#read into a list
        lines_b = f_b.readlines()
        
        lines_a_len = len(lines_a)#how many lines
        lines_b_len = len(lines_b)
        max_lines = max(lines_a_len, lines_b_len)#for the loop times

        fw = open(f"{file_name_prefex}-out.txt", "a")#append mode
        for i in range(max_lines):
            line_write_file(lines_a, lines_a_len, i, fw)#1 line from A into output
            line_write_file(lines_b, lines_b_len, i, fw)#1 line from B into output
            
        f_a.close()
        f_b.close()
        fw.close()
except FileNotFoundError:
    print("File does not exist!")

        
