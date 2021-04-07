# Call OS and CSV modules
import os 
import csv

# Set filepath for CSV
election_csv = os.path.join("Resources", "election_data.csv")

# Reading the CSV
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    total_votes = len(csvreader[2])
    print (total_votes)