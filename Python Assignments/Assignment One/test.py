import os
import argparse
import stat
import time
import csv

# Step 1 Parse command line arguements(just the filename)
parser = argparse.ArgumentParser(description='takes in file and outputds date of file, file size in MB, and name of file')
parser.add_argument("--directory", type=str, help = "The directory in which you want info regarding files")
args = parser.parse_args()
#you can write python3 test.py /path/to/directory
print("Argument passed was: ",args)

#Step 2: Read files from Directory. use the ::OS module to list files in current directory
directory = args.directory
print("Directory is: ",directory)
path = os.listdir(directory)
print("these are the files in the path:", path)

# Step 3: Get file attributes: Retrieve file size, create date, and name for each file
name = []
createDate = []
size = []
for files in path:
    name.append(os.path.basename(files)) #name of file
    createDate.append(time.ctime(os.path.getmtime(files)))
    size.append(os.path.getsize(files)/ (1024*1024))

print("Name is", name)
print("\n modification date is",createDate)
print("\n size in MB is", size)
data = [name,createDate,size]
with open('file_attributes.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Name", "Modification Date", "Size (MB)"])
    csv_writer.writerows(zip(*data))
