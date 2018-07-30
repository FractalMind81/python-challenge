import os
import pandas as pd

# Read in a .csv file 
csv_path = os.path.join("..","PyPoll", "election_data.csv") 

# Load data into data frame
poll_data = pd.read_csv(csv_path)

# Extract poll totals
poll_totals = poll_data.groupby('Candidate')['Voter ID'].agg(['count']).sort_values(by='count',ascending=False).reset_index()

# Total Votes Cast
total_votes = poll_totals['count'].sum()

# Print results to terminal
print("Election Result")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for index, row in poll_totals.iterrows():
    print(row['Candidate'] + ": " + "{:,.3f}".format(100*row['count']/total_votes) + "% (" + str(row['count']) + ")")
print("-------------------------")
print("Winner: " + poll_totals.loc[0,'Candidate'])

# Prepare file output
output_file = open("election_output.txt","w")

# Write results to file
output_file.write("Election Result\n")
output_file.write("-------------------------\n")
output_file.write("Total Votes: " + str(total_votes) +"\n")
output_file.write("-------------------------\n")
for index, row in poll_totals.iterrows():
    output_file.write(row['Candidate'] + ": " + "{:,.3f}".format(100*row['count']/total_votes) + "% (" + str(row['count']) + ")\n")
output_file.write("-------------------------\n")
output_file.write("Winner: " + poll_totals.loc[0,'Candidate'] + "\n")

# Close file
output_file.close()