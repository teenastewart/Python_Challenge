# Calling modules
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")


# Reading the CSV
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    
    # skips the header row
    csv_header = next (csvreader)
    months = 0
    net_profit = 0
    yrmax = 0
    yrmin = 0
    for row in csvreader:
    # Calculate the number of months in the CSV
        months += 1
        net_profit += int(row[1])
        net_money = "${:,.2f}".format(net_profit)
        if int(row[1]) > yrmax:
            yrmax = int(row[1])
        elif int(row[1]) < yrmin:
            yrmin = int(row[1])    

    yraverage = (net_profit/months)
    yravmoney = "${:,.2f}".format(yraverage)

    # Calculate the net profit
    #net_profit = sum(int(row[1]) for row in csvreader)
    print(f"Total Months: {months}")
    print(f"Total: {net_money}")
    print(f"Average Change: {yravmoney}")
    print(f"Greatest Increase in Profits: {yrmax}")
    print(f"Greatest Decrease in Profits: {yrmin}")
    # net_profit = 0
    # for row in csvreader:
        #print(row)
        # net_profit += int(row[1])
    
    
    # for row in csv.reader(csvfile):
       
        

