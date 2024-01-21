import os
import csv


# Specify the path to the CSV file
election_csv = os.path.join("Resources", "election_data.csv")

# Checking the 'analysis' folder 
election_folder = os.path.join("analysis")

# Opne the CSVfile
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Declare variables to store values
    total_votes = 0
    candidates = {}
    winner = {"name": "", "votes": 0}

    # Go through each row in the file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Retrieve the name of the candidate
        candidate_name = row[2]

        # Update candidate votes count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

    # Determine the winner
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes} votes)")

        # Update the winner list
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes

    # Display the election results.
    print("Election Result")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes} votes)")
    print("--------------------------------")
    print(f"Winner: {winner['name']}")
    
    print("--------------------------------")

     # Save the outcome to a text file within the 'analysis' folder
    output_path = os.path.join(election_folder, "election_analysis.txt")
    output_path = os.path.join("analysis", "election_analysis.txt")
    with open(output_path, "w") as output_file:
      output_file.write("Election Result\n")
      output_file.write("--------------------------------\n")
      output_file.write(f"Total Votes: {total_votes}\n")
      output_file.write("--------------------------------\n")
      for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes} votes)\n")
      output_file.write("--------------------------------\n")
      output_file.write(f"Winner: {winner['name']}\n")
      output_file.write("--------------------------------\n")
