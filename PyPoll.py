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

# Dictionary for counting candidate votes
candidate_votes = {}

# variables for determining the winner
winner = ""
winning_count = 0
winning_percentage = 0


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

            # add candidates to the list of candidates as they appear
            candidates.append(candidate_name)

            # Begin tracking votes for the candidate
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Calculate percentage of total votes for each candidate by iterating through the candidate list
for candidate_name in candidate_votes:
    
    # get the total vote count
    votes = candidate_votes[candidate_name]

    # Determine the percentage of votes
    vote_percentage = float(votes)/float(total_votes)*100
    # vote_percentage = "{:.1f}".format(float(votes)/float(total_votes)*100)

    # Print the candidate name and their percentage of the votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine the winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # Set a new winner
        winner = candidate_name
        # set a new winning count
        winning_count = votes
        # set a new winning percentage
        winning_percentage = vote_percentage

# Display total votes
# print(total_votes)
# print(candidate_votes)
# print(f"{winner} won the election with {winning_count:,} votes making up {winning_percentage:.1f}% of the vote.")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

election_data.close()
