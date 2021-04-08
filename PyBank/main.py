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
    month_start = 0
    total_change = 0
    month_result = []
    date_result = []
    for row in csvreader:
        # Calculate the number of months in the CSV
        months += 1
        # Calculate the net profit
        net_profit += int(row[1])
        # Format the net profit
        net_money = "${:,.2f}".format(net_profit)
        # set variable for month end being the current row in the iteration
        month_end = int(row[1])
        # Subtract the current row value from the previous stored value
        monthly_profit_change = month_end - month_start
        # add monthly profit change to month result list
        month_result.append(monthly_profit_change)
        date_result.append(row[0])
        # reset month start for next iteration 
        month_start = month_end
    # Remove first result becuase there was no prior month value to calculate a change
    month_result.pop(0)
    date_result.pop(0)
    # find the total sum of the changes
    total_change = sum(month_result)
    # Calculate average of changes and format to currency
    yravmoney = "${:,.2f}".format((int(total_change))/(months-1))
    # find max and min changes
    yearx = max(month_result)
    yearn = min(month_result)
    # determine index of max and min changes
    yearxd = month_result.index(yearx)
    yearnd = month_result.index(yearn)
    # use max and min change indexes to determine corresponmding months
    maxdate = date_result[yearxd]
    mindate = date_result[yearnd]
  
# Print the analysis
print(f"""Financial Analysis
        ------------------
        Total Months: {months}
        Total: {net_money}
        Average Change: {yravmoney}
        Greatest Increase in Profits: {maxdate} ({"${:,.2f}".format(int(yearx))})
        Greatest Decrease in Profits: {mindate} ({"${:,.2f}".format(int(yearn))})""")

# set variable for output file
output_file = os.path.join("Analysis", "result.txt")

#  Open the output file
file = open(output_file, "w")
file.write(f"""Financial Analysis
        ------------------
        Total Months: {months}
        Total: {net_money}
        Average Change: {yravmoney}
        Greatest Increase in Profits: {maxdate} ({"${:,.2f}".format(int(yearx))})
        Greatest Decrease in Profits: {mindate} ({"${:,.2f}".format(int(yearn))})""")
file.close()

        

