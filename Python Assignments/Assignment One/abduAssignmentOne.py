import os
import argparse

# Step 1: Parse Command line arguments (there are 3 of them)
parser = argparse.ArgumentParser(description='takes in file and outputs date of file, file size in MB, and name of file')
parser.add_argument(sizeFile)
parser.add_argument(dateFile)
parser.add_argument(nameFile)

args = parser.parse_args()

# Step 2: Read Files from Directory: Use the os module to list files in a given directory.


# Step 3:	Get File Attributes: Retrieve file permissions, size, modification date, and name for each file.

# Step 4:	Convert File Size: Convert the file size to megabytes (MB).

# Step 5:		Write to CSV: Use the csv module to write the file attributes to a CSV file.

# Step 6:	Error Checking and Help Display: The argparse module automatically provides error checking and help display.
