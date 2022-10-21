
# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Counting total votes, resetting to 0 every time we open the file
total_votes = 0

#Initialize a list that will hold candidate name
candidate_options = []

# Declare an empty dictionary to hold candidate name and number of votes they received
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read the field
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        
            # Add name to list
            candidate_options.append(candidate_name)

            # begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # save the results to our text file
with open(file_to_save, "w") as election_analysis:

        # print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end = "")

    # save the final vote count to the text file
    election_analysis.write(election_results)

    # iterate through the candidate list
    for candidate_name in candidate_votes:

        #retrieve the vote counte of a candidate
        votes = candidate_votes[candidate_name]

        # calculate the percentage of cotes
        vote_percentage = float(votes)/float(total_votes)*100

        # print the candidate's name, vote count, percentage of votes 
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print each candidate's voter count and percentage to the terminal
        print(candidate_results)

        # save the candidate results to our text file
        election_analysis.write(candidate_results)


        # Determine if the votes are greater than the winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):

            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        
    winning_candidate_summary = (
        f"-------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------\n")

        # print each candidate, their voter count, and percentage to the terminal
    print(winning_candidate_summary)

        # save the candidate results to our text file
    election_analysis.write(winning_candidate_summary)
    


election_data.close()