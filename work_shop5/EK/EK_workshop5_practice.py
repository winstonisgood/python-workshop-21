import os
from itertools import zip_longest

file_name = input("Enter filename (exclude -A.txt/-B.txt): ").strip()
#Let people enter the filename in the data folder.

current_dir = os.path.dirname(__file__) 
folder = os.path.join(current_dir, "..", "data")  
folder_path = os.path.abspath(folder)  #Get the absolute path of the data folder.
#Get the current working directory and join it with 'data' to create the folder path.
file_path_A = os.path.join(folder_path, f"{file_name}-A.txt")
file_path_B = os.path.join(folder_path, f"{file_name}-B.txt")
#Create the full file paths for both A and B files.
file_path_output = os.path.join(folder_path, f"{file_name}-out.txt")
#Create the output file path.

if not os.path.exists(file_path_A):
    print(f"File {file_path_A} does not exist.")
    exit()
if not os.path.exists(file_path_B):
    print(f"File {file_path_B} does not exist.")
    exit()
    #Check if both files exist, if not, print an error message and exit the program.

with open(file_path_A, "r", encoding="utf-8") as fa:
    lines_A = fa.readlines()
    #Open file A and read all lines into a list.

with open(file_path_B, "r", encoding="utf-8") as fb:
    lines_B = fb.readlines()
    #Open file B and read all lines into a list.

combined_lines = []
for a, b in zip_longest(lines_A, lines_B, fillvalue=""):
    if a:  # If A has content, add it as odd line
        combined_lines.append(a.rstrip("\n"))
    if b:  # If B has content, add it as even line
        combined_lines.append(b.rstrip("\n"))
#Combine the lines from both files
#Use zip_longest to handle files of different lengths, filling missing lines with an empty string.

with open(file_path_output, "w", encoding="utf-8") as fo:
    fo.write("\n".join(combined_lines))
#Open the output file and write the combined lines

print(f"Combined file created at: {file_path_output}")
#Print the path of the created output file.
for line in combined_lines:
    print(line)
#Print each line of the combined output to the console.