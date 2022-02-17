# we need to retrieve
# 1. the total number of votes cast
# 2. A complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# counter for total votes
total_votes = 0

# Identify the candidates
candidates = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    # print(headers)

    for row in file_reader:
        # Sum total votes
        total_votes += 1
        candidate_name = row[2]

        # add candidate name to candidates list
        if candidate_name not in candidates:
            candidates.append(candidate_name)

# Display total votes
# print(total_votes)
print (candidates)

election_data.close()
