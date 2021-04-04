# Calling modules
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

# Reading the CSV
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    
    # skips the header row
    csv_header = next (csvreader)
    # Calculate the number of months in the CSV
    months = len(list(csvreader))
    print(months)
    net_profit = sum(float(row[1]) for row in csvreader)
    # net_profit = 0

    # for row in csvreader:
        # net_profit += int(row[1])
    print(net_profit)
    # Calculate the net profit
    # for row in csv.reader(csvfile):
       
        

