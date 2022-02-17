# we need to retrieve
# 1. the total number of votes cast
# 2. A complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# file_path = "Resources\election_results.csv"

# election_data = open(file_path,"r")



# election_data.close()

# with open(file_path) as election_data:
    
#     print(election_data)

import csv
import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# outfile.write("Hello World!")

# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # # Write some data to the file.
    # txt_file.write("Hello World")

    # Write three counties to the file.
    # txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Arapahoe\nDenver\nJefferson")