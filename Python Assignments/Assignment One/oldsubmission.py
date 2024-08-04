# used stack overflow, Geeks for Geeks, and other similar sites for help with the code in linux.
# Used chatgpt for steps on solving as well as pushing me in the right direction
import os
import argparse
import stat 
import time
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

  #path is just a array of our files 
  return path



# Step 3:	Get File Attributes: Retrieve file size, modification date, and name for each file.  
def getFileAttributes(directory, path):
  #we don't do anything directory
  name = []
  modDate = []
  size = []
  for files in path: #or files in directory?
    name.append(os.path.basename(files)) # name of file
    modDate.append(os.path.getmtime(files)) # modification date
    size.append(stat.st_size / (1024 * 1024)) #stats was used before instead of stat
  
  #can use a for loop for printing as well, this might make more sense opposed to writing down name 
  print("Name is ",name)
  print("Modification date is ", modDate)
  print("Size is ",size)
  #print all file attributes, return type is ???
  
  
  

# Step 4:	Write to CSV: Use the csv module to write the file attributes to a CSV file.

def writeCSV():
  #use the 'w' for mode to write in a new csv file using the with open method
   with open('file_attributes.csv', 'w', newline='') as csvfile: #assuming file_attributes.csv is a empty csv somewhere in syedAssignmentONe.py directory
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Permissions", "Size (MB)", "Modification Date", "File Name"])
        csv_writer.writerows(getFileAttributes)


  
# For testing purposes, write a main function

#main function
if __name__ == "__main__":
  # let's test out by passing in a directory
  directory = args.directory
  path = read_files(directory) #name of all the files
  fileAttributes = getFileAttributes(directory, path)


