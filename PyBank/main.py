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

  
    for row in csvreader:
        # Calculate the number of months in the CSV
        months += 1
        # Calculate the net profit
        net_profit += int(row[1])
        # Format the net profit
        net_money = "${:,.2f}".format(net_profit)

    # Calculate average
    yraverage = (net_profit/months)
    # Format average
    yravmoney = "${:,.2f}".format(yraverage)

   
# re-populates reader
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    # skips the header row
    csv_header = next (csvreader)
    # finding the max value in column b and grabbing the row data
    yrmax = (max(csvreader, key=lambda _: _[1]))
    # formatting the profit as money
    yrmaxmoney = "${:,.2f}".format(int(yrmax[1]))
    
# re-populates reader
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    # skips the header row
    csv_header = next (csvreader)
    # finding the max value in column b and grabbing the row data
    yrmin= (min(csvreader, key=lambda _: _[1]))
    # formatting the profit as money
    yrminmoney = "${:,.2f}".format(int(yrmin[1]))

# Print the analysis
print(f"""Financial Analysis
        ------------------
        Total Months: {months}
        Total: {net_money}
        Average Change: {yravmoney}
        Greatest Increase in Profits: {(yrmax[0])} ({yrmaxmoney})
        Greatest Decrease in Profits: {(yrmin[0])} ({yrminmoney})""")

# set variable for output file
output_file = os.path.join("Analysis", "result.txt")

#  Open the output file
file = open(output_file, "w")
file.write(f"""Financial Analysis
        ------------------
        Total Months: {months}
        Total: {net_money}
        Average Change: {yravmoney}
        Greatest Increase in Profits: {(yrmax[0])} ({yrmaxmoney})
        Greatest Decrease in Profits: {(yrmin[0])} ({yrminmoney})""")
file.close()

        

