import os
import pandas as pd

# Read in a .csv file 
csv_path = os.path.join("..","PyBoss", "employee_data.csv")

# Create State dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Import data in pandas dataframe
employee = pd.read_csv(csv_path)

# Initialize employee_clean
employee_clean = pd.DataFrame()

# Transfer employee ids to employee clean
employee_clean['Emp ID'] = employee['Emp ID']

# Split name into first and last names
name_split = employee['Name'].str.split(" ")

# Add first and last names to employee_clean
employee_clean['First Name'] = name_split.str.get(0)
employee_clean['Last Name'] = name_split.str.get(1)

# Format DOB column then add to employee_clean 
employee_clean['DOB'] = pd.to_datetime(employee['DOB']).dt.strftime('%m/%d/%Y')

# Format SSN column
employee_clean['SSN'] = employee['SSN'].str.slice_replace(stop=6,repl='***-**')

# Replace state with abbreviation
employee_clean['State'] = employee['State'].map(us_state_abbrev)

# Export employee_clean to csv
employee_clean.to_csv("employee_data_clean.csv",sep=',')
