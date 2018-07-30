# Import the necessary dependencies for os.path.join() import os import csv 
import os
import csv
import functools

# Initialize variable
month_count = 0
net_profit = 0
monthly_change = []
last_month_total = 0
 
# Read in a .csv file 
csv_path = os.path.join("..","PyBank", "budget_data.csv") 

with open(csv_path, newline='') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Check if the csv file has a header row
    sniffer = csv.Sniffer()
    contains_hdr = sniffer.has_header(csv_file.read(128))

    # This skips the header row of the CSV file.
    if contains_hdr == True:
        next(csv_reader,None)

    # Read each row of data after the header
    for row in csv_reader:

        # Count the number of months in the dataset
        month_count += 1

        # Net profit
        net_profit += int(row[1])

        # Build list of monthly changes
        monthly_change.append(int(row[1]) - last_month_total)

        # Update last month's total
        last_month_total = int(row[1])

    # Remove the first entry of monthly change
    monthly_change.pop(0)
    
    # Avergage change 
    avg_change = functools.reduce(lambda x,y : x+y,monthly_change)/(month_count-1)

    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(month_count))
    print("Net Profit: " + str(net_profit))
    print("Average change: " + str(avg_change))
