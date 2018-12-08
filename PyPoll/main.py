import os
import csv

def getPercentage(part, whole):
    return round((part/whole * 100), 3)


# Define the path: ./Resources/election_data.csv
data_path = os.path.join(".", "Resources", "election_data.csv")

# Open the file
with open(data_path, newline='') as data_file:

    # Read the data
    election_data = csv.reader(data_file, delimiter = ",")

    # Skip the first row in the data.
    election_header = next(election_data) 
    print(f"election_header = {election_header}")

    # Initialize data
    num_votes = 0
    candidates = {}
    winner_value = 0

    for row in election_data:

        # Count the number of votes
        num_votes += 1

        # Check if the candidate exists in the dictionary
        if candidates.get(row[2], 0) == 0:
            # Candidate does not exist

            # Enter the candidate in the dictionary, and give them their first vote
            candidates[row[2]] = 1
        else:
            # Candidate exists
           
            # Add a vote for the candidate
            candidates[row[2]] += 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(num_votes))
print("-------------------------")

for key in candidates:

    # Print the election results:
    # Format:
    # Candidate: VotePercentage% (numberOfVotes)
    print(key + ": " + str(getPercentage(int(candidates[key]), num_votes)) + "% (" + str(candidates[key]) + ")")

    # Find winner:
    if candidates[key] > winner_value: 
        winner_value = candidates[key]
        winner = key

print("------------------------")
print("Winner: " + winner)
print("-------------------------")




