


# PyPoll

#incorporated the dependencies
import os
import csv

#files to load and outpur
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

# total vote counter
total_votes = 0

#candidate options and vote counter
candidate_options = []
candidate_votes  = { }

# winning dandidate and winning count tracker
winning_candidate = ""
winning_count = 0

# read the csv and convert into a list
with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
        
        #read the header
        header = next(reader)
      
        for row in reader:
            
                #run the loader animation
              #  print(". ", end="")
                
                #add to total vote count
                total_votes = total_votes + 1
                
                #extract the candidate name from each row
                candidate_name = row[2]
                
                #if the candidate does not match any existing candidate...
                #loop is discovering candidates as it goes
                
                if candidate_name not in candidate_options:
                    #add to the list of candidates in the running
                    candidate_options.append(candidate_name)
                    
                    #begin tracking that candidate voter count at 0
                    candidate_votes[candidate_name] = 0
                    
                candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
           
with open(file_to_output, "w") as txt_file:
                
    #print final vote count
                
    election_results = (
        f"\n\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------\n"
    )
    #print(election_results, end="")
    
    #save final vote count to txt file
    txt_file.write(election_results)

    #determine the winner by looping thru the counts 
    for candidate in candidate_votes:
    
        #retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
    
        #Determine winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        #print each candidate's and percentage to terminal
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    
        print(voter_output, end="")
    
        txt_file.write(voter_output)
    
    #print the winning candidates
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------\n"
    )
    #print(winning_candidate_summary)
    
    #save the winning_candidate name to text file
    txt_file.write(winning_candidate_summary)







