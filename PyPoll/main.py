# Call OS and CSV modules
import os 
import csv

# Set filepath for CSV
election_csv = os.path.join("Resources", "election_data.csv")

# Reading the CSV
with open(election_csv, newline='') as csvfile:
    #csvreader = csvfile.readlines()
    csvreader = csv.reader(csvfile, delimiter =',')
    # Skip header row
    csv_header = next (csvreader)
    # Set initial value for total votes variable
    total_votes = 0
    # Set candidate list variable
    candidate = []
    # loop through sheet to get total votes and build candidate list
    for row in csvreader:
        total_votes = total_votes+1
        candidate.append(row[2]) 
    # set candidate votes dictionary           
    candidate_votes = {}
    # Read through the CSV and build the total votes for each candidate in the dictionary
    for i in candidate:
            # Create the keys for each unique name
            if not candidate_votes.__contains__(i): candidate_votes[i] = 1 
            # Create the values per key
            else: candidate_votes[i] +=1
    # Do the math and format the percentages for each candidate's net votes against the total
    khan = "{:.0%}".format(int(candidate_votes['Khan'])/int(total_votes))
    correy = "{:.0%}".format(int(candidate_votes['Correy'])/int(total_votes))
    li = "{:.0%}".format(int(candidate_votes['Li'])/int(total_votes))
    otooley = "{:.0%}".format(int(candidate_votes["O'Tooley"])/int(total_votes))
    # Split the dictionary into two lists to find the max vote count and corresponding candidate
    all_val = candidate_votes.values()
    max_vote = max(all_val)
    key_list = list(candidate_votes.keys())
    val_list = list(candidate_votes.values())
    position = val_list.index(max_vote)
    winner = key_list[position]
    # Print the results to screen
    print (f"""
        --------------------------
        Total Votes: {total_votes}
        --------------------------
        Khan: {khan} ({candidate_votes['Khan']})
        Correy: {correy} ({candidate_votes['Correy']})
        Li: {li} ({candidate_votes['Li']})
        O'Tooley: {otooley} ({candidate_votes["O'Tooley"]})
        --------------------------
        Winner: {winner}
        --------------------------""")    
    
    # set variable for output file
output_file = os.path.join("Analysis", "result.txt")

#  Open the output file
file = open(output_file, "w")
file.write(f"""
        --------------------------
        Total Votes: {total_votes}
        --------------------------
        Khan: {khan} ({candidate_votes['Khan']})
        Correy: {correy} ({candidate_votes['Correy']})
        Li: {li} ({candidate_votes['Li']})
        O'Tooley: {otooley} ({candidate_votes["O'Tooley"]})
        --------------------------
        Winner: {winner}
        --------------------------""")
file.close()