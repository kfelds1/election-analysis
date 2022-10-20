# The data we need to retrieve


# Direct Method
# Assign a variable for the file to load and the path

#file_to_load = 'Resources/election_results.csv'


# Open the election results and read the file

#with open(file_to_load) as election_data:
   # print(election_data)

# Indirect Method
import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")

with open(file_to_load) as election_data:
    
    # To do: read and analyze the data
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
# Create a filename variable to a direct or indirect path to the file

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file
with open(file_to_save, "w") as election_txt:
    election_txt.write("Counties in the Election\n---------\nArapahoe\nDenver\nJefferson")

election_txt.close

# 1. The total number of votes cast

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on the popular vote

# Close the file

election_data.close()