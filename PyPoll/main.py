import os
import pandas as pd

# Read in a .csv file 
csv_path = os.path.join("..","PyPoll", "election_data.csv") 

# Load data into data frame
poll_data = pd.read_csv(csv_path)

# Extract poll totals
poll_totals = poll_data['Candidate'].value_counts()

# Total Votes Cast
total_votes = poll_totals.sum()

# Print results to terminal
print("Election Result")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for index_val, series_val in poll_totals.iteritems():
    print(index_val + ": " + "{:,.3f}".format(100*series_val/total_votes) + "% (" + str(series_val) + ")")
print("-------------------------")
print("Winner: " + poll_totals.index[0])

# Prepare file output
output_file = open("election_output.txt","w")

# Write results to file
output_file.write("Election Result\n")
output_file.write("-------------------------\n")
output_file.write("Total Votes: " + str(total_votes) +"\n")
output_file.write("-------------------------\n")
for index_val, series_val in poll_totals.iteritems():
    output_file.write(index_val + ": " + "{:,.3f}".format(100*series_val/total_votes) + "% (" + str(series_val) + ")\n")
output_file.write("-------------------------\n")
output_file.write("Winner: " + poll_totals.index[0] + "\n")

# Close file
output_file.close()