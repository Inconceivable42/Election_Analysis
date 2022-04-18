# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join(os.path.dirname(__file__),"Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join(os.path.dirname(__file__),"Analysis", "election_analysis.txt")

# Create accumulator variable set to 0
total_votes = 0

# Create new list of candidates
candidate_options = []

# Create vote dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:


    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]
        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) 
           
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print what directions said to print
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)


# 3. Print the total votes.
#print(total_votes)

# print the candidate list.
#print(candidate_options)

# Print the candidate vote dictionary.
#print(candidate_votes)

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Caluculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes)*100


                #print (f"{candidate_name} received {vote_percentage:.1f}% of the vote.")
                # To do: print out each candidate's name, vote count, and % of votes to the terminal.
                #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% {votes:,}\n\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results) 
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate
    # Detrmine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percent=vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate' name.
            winning_candidate = candidate_name

    # To do: print out the winning candidate, vote count and % to terminal.
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner:  {winning_candidate}\n"
        f"Winning Vote Count:  {winning_count:,}\n"
        f"Winning Percentage:  {winning_percentage:.1f}%\n"
        f"-----------------------------\n")

    #print(winning_candidate_summary)
    # Save the wining candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

