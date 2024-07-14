import os
import argparse
import csv

# Step 1: Parse Command line arguments (there are 3 of them)
parser = argparse.ArgumentParser(description='takes in file and outputs date of file, file size in MB, and name of file')

#Input is the directory of the file
parser.add_argument("directory", help = "The directory in which you want info regarding files") 

args = parser.parse_args()

# Step 2: Read Files from Directory: Use the os module to list files in a given directory.
#input is directory
def read_files(directory):
  path = os.listdir(directory) #use listdir method which appends the files in a directory to a list variable "path"
  print("Files and directories in path", directory, ":")
  print(path)
  return path

# Step 3:	Get File Attributes: Retrieve file size, modification date, and name for each file.  
def getFileAttributes(directory, path):
  name = []
  #for files in path:
    name.append(files)


  return 
  
  
  
# Step 4:	Convert File Size: Convert the file size to megabytes (MB).
  

# Step 5:	Write to CSV: Use the csv module to write the file attributes to a CSV file.

# Step 6:	Error Checking and Help Display: The argparse module automatically provides error checking and help display.
