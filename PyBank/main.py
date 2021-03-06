# Import the necessary dependencies for os.path.join() import os import csv 
import os
import csv

# Initialize variable
month_count = 0
net_profit = 0
last_month_total = 0
monthly_change = []
months = []
 
# Read in a .csv file 
csv_path = os.path.join("..","PyBank", "budget_data.csv") 

with open(csv_path, newline='') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # This skips the header row of the CSV file.
    next(csv_reader,None)
    
    # Read each row of data after the header
    for row in csv_reader:

        # Count the number of months in the dataset
        month_count += 1

        # Net profit
        net_profit += int(row[1])

        # Build list of monthly changes
        monthly_change.append(int(row[1]) - last_month_total)

        # Build list of months
        months.append(row[0])

        # Update last month total
        last_month_total = int(row[1])

    # Remove the first entry of monthly change and months
    monthly_change.pop(0)
    months.pop(0)

    # Avergage change 
    avg_change = sum(item for item in monthly_change)/len(monthly_change)

    # Max change/month
    max_change = max(monthly_change) 
    max_month = months[monthly_change.index(max_change)]

    # Min change/month
    min_change = min(monthly_change)
    min_month = months[monthly_change.index(min_change)]

    # Prepare file output
    output_file = open("financial_analysis.txt","w")

    # Output to files
    output_file.write("Financial Analysis\n")
    output_file.write("------------------------------\n")
    output_file.write("Total Months: " + str(month_count) + "\n")
    output_file.write("Net Profit: " + "${:,.2f}".format(net_profit) + "\n")
    output_file.write("Average change: " + "${:,.2f}".format(avg_change) + "\n")
    output_file.write("Greatest Increase in Profits: " + max_month + " " + "${:,.2f}".format(max_change) + "\n")
    output_file.write("Greatest Decrease in Profits: " + min_month + " " + "${:,.2f}".format(min_change) + "\n")

    # Close file
    output_file.close()

    # Output to terminal
    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(month_count))
    print("Net Profit: " + "${:,.2f}".format(net_profit))
    print("Average change: " + "${:,.2f}".format(avg_change))
    print("Greatest Increase in Profits: " + max_month + " " + "${:,.2f}".format(max_change))
    print("Greatest Decrease in Profits: " + min_month + " " + "${:,.2f}".format(min_change))
