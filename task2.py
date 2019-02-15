import os
import re
# the following code is for getting GET, POST, PUT and DELETE requests in different files
line_regex = re.compile(r"GET")
line_regex1 = re.compile(r"POST")
line_regex2 = re.compile(r"PUT")
line_regex2 = re.compile(r"DELETE")

output_filename1 = os.path.normpath("output/GET.log")
with open(output_filename1, "w") as out_file:
    out_file.write("")

output_filename2 = os.path.normpath("output/POST.log")
with open(output_filename2, "w") as out_file:
    out_file.write("")

output_filename3 = os.path.normpath("output/POST.log")
with open(output_filename3, "w") as out_file:
    out_file.write("")

output_filename4 = os.path.normpath("output/DELETE.log")
with open(output_filename4, "w") as out_file:
    out_file.write("")

with open(output_filename1, "a") as out_file:
    with open("access.log", "r") as in_file:
        
        for line in in_file:
            
            if (line_regex.search(line)):
                print(line)
                out_file.write(line)

with open(output_filename2, "a") as out_file:
    with open("access.log", "r") as in_file:
          
        for line in in_file:
              
            if (line_regex.search(line)):
                print(line)
                out_file.write(line)

with open(output_filename3, "a") as out_file:
    with open("access.log", "r") as in_file:
          
        for line in in_file:
              
            if (line_regex.search(line)):
                print(line)
                out_file.write(line)

with open(output_filename4, "a") as out_file:
    with open("access.log", "r") as in_file:
          
        for line in in_file:
              
            if (line_regex.search(line)):
                print(line)
                out_file.write(line)

