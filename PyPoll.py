# Data we need to retrieve:
# 1. Total number of votes
# 2. Complete list of candidates
# 3. Percentage of voter per candidate
# 4. Total votes for each candidate.
# 5. Winner of the election
# 
# Add our dependencies
import csv
import os
file_to_load = os.path.join('Resources','election_results.csv')
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#create the Counter of Total Votes
total_votes = 0
#Create the candidate list
candidate_list = []
#Create the candidates-votes dictionary
candidate_votes = {}
#Create a winning candidate and winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file with the reader function. 
    file_reader = csv.reader(election_data)
    # Read the header row
    headers=next(file_reader)
    #Print each  Row in the CSV file
    for row in file_reader:
       #Add a vote per ballot
       total_votes += 1
       #Read the candidate name per ballot
       candidate_name = row[2]
       if candidate_name not in candidate_list:
        #Add the candidate name to our candidate list
        candidate_list.append(candidate_name)
        #Begin tracking candidates votes
        candidate_votes[candidate_name]=0
        #Add a vote to candidate's count
       candidate_votes[candidate_name]+=1
    #Save results to txt file
    with open(file_to_save) as txt_file:
        election_results = (
        f'\nElections Results\n'
        f'-------------------\n'
        f'Total Votes = {total_votes:,}\n'
        f'-------------------\n'
    )
        print(election_results,end="")
        #Save final vote count to the text file.
        txt_file.write(election_results)
        #Determine percentage of votes
        for candidate in candidate_votes:
            #Retrieve votes per candidates
            votes = candidate_votes[candidate]
            #Calculate percentage of votes
            vote_percentage = int(votes)/int(total_votes) * 100
            #print candidate name and percentage of votes
            #print(f"{candidate}: received {vote_percentage:.2f}% of the vote")
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if true, set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #set the winning candidates name equal to candidate's name
                winning_candidate = candidate
            #print(f"{candidate}: has {vote_percentage:.2f}% of the votes ({votes:,} votes)\n")
        winning_candidate_summary = (
            f"-----------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count:,} out of {total_votes:,} votes\n"
            f"Winning percentage: {winning_percentage:.2f}%\n"
            f"-----------------\n"
        )
        #print(winning_candidate_summary)
    #print number of total votes
    #print(total_votes) 
    #print the candidate list
    #print(candidate_list)
    #print the candidate vote dictionary
    #print(candidate_votes)