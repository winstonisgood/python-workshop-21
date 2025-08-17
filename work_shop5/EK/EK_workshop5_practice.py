import os
from itertools import zip_longest

#Let people enter the filename in the data folder.
file_name = input("Enter filename (exclude -A.txt/-B.txt): ").strip()

#Get the absolute path of the data folder.
#Get the current working directory and join it with 'data' to create the folder path.
current_dir = os.path.dirname(__file__) 
folder = os.path.join(current_dir, "..", "data")  
folder_path = os.path.abspath(folder)  

#Create the full file paths for both A and B files.
file_path_A = os.path.join(folder_path, f"{file_name}-A.txt")
file_path_B = os.path.join(folder_path, f"{file_name}-B.txt")

#Create the output file path by appending '-out.txt' to the file name.
file_path_output = os.path.join(current_dir, f"{file_name}-out.txt")

#Check if both files exist, if not, print an error message and exit the program.
if not os.path.exists(file_path_A):
    print(f"File {file_path_A} does not exist.")
    exit()
if not os.path.exists(file_path_B):
    print(f"File {file_path_B} does not exist.")
    exit()

#Open file A and read all lines into a list.
with open(file_path_A, "r", encoding="utf-8") as fa:
    lines_A = fa.readlines()

#Open file A and read all lines into a list.
with open(file_path_B, "r", encoding="utf-8") as fb:
    lines_B = fb.readlines()

#Combine the lines from both files
combined_lines = []
#Use zip_longest to handle files of different lengths, filling missing lines with an empty string.
for a, b in zip_longest(lines_A, lines_B, fillvalue=""):
# If A has content, add it as odd line
    if a: 
        combined_lines.append(a.rstrip("\n"))
# If B has content, add it as even line
    if b:  
        combined_lines.append(b.rstrip("\n"))

#Open the output file and write the combined lines
with open(file_path_output, "w", encoding="utf-8") as fo:
    fo.write("\n".join(combined_lines))

#Print the path of the created output file.
print(f"Combined file created at: {file_path_output}")

#Print each line of the combined output to the console.
for line in combined_lines:
    print(line)