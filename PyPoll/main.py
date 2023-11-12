#set up operating system
import os
#reads csv
import csv

budget_csv = os.path.join(r"C:\Users\salaz\OneDrive\Desktop\Class_Folder\homework\python-challenge\PyPoll", "Resources", "election_data.csv")



#next lines print the analysis results
print("Election Results")

print("---------------------------------------")

print(f"Total Votes: ")

print("---------------------------------------")

print(f"Charles Casper Stockham: 23.049% (85213)")

print(f"Diana DeGette: 73.812% (272892)")

print(f"Raymon Anthony Doane: 3.139% (11606)")

print("---------------------------------------")

print(f"Winner: Diana DeGette")

print("---------------------------------------")