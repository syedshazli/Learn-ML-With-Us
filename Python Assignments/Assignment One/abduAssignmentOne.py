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
  return path



# Step 3:	Get File Attributes: Retrieve file size, modification date, and name for each file.  
def getFileAttributes(directory, path):
  name = []
  modDate = []
  for files in path: #or files in directory?
    name.append(os.path.basename(path)) # name of file
    modDate.append(os.path.getmtime(path)) # modification date
    size_in_mb = stats.st_size / (1024 * 1024)
  
  #print all file attributes
  
  
  

# Step 4:	Write to CSV: Use the csv module to write the file attributes to a CSV file.

def writeCSV():
  #use the 'w' for mode to write in a new csv file using the with open method
   with open('file_attributes.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Permissions", "Size (MB)", "Modification Date", "File Name"])
        csv_writer.writerows(file_attributes)

  
# For testing purposes

#main function
if __name__ == "__main__":
  # let's test out by passing in a directory
