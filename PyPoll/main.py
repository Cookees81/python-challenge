#set up operating system
import os
#reads csv
import csv

election_data = os.path.join(r"C:\Users\salaz\OneDrive\Desktop\Class_Folder\homework\python-challenge\PyPoll", "Resources", "election_data.csv")

#setting buckets for counts
vote_total = 0

stockham_votes = 0

degette_votes = 0

doane_votes = 0

stockham = []

degette = []

doane = []

stvotes = []

dgvotes = []

dovotes = []

#reading
with open(election_data, "r") as f:
    readfile = csv.reader(f)
    # skip header
    header = next(readfile)

    for row in readfile:
        vote_total = vote_total + 1

        if (row[2]) == 'Charles Casper Stockham':
            stockham_votes = stockham_votes + 1
        elif (row[2]) == 'Diana DeGette':
            degette_votes = degette_votes + 1
        elif (row[2]) == 'Raymon Anthony Doane':
            doane_votes = doane_votes + 1

#calculate percentages and convert to str
stockham_pct = round(int(stockham_votes)/int(vote_total) * 100, 3)
stockham.append(str(stockham_pct) + "%")

degette_pct = round(int(degette_votes)/int(vote_total) *100, 3)
degette.append(str(degette_pct) + "%")

doane_pct = round(int(doane_votes)/int(vote_total) * 100, 3)
doane.append(str(doane_pct) + "%")

#convert lists to str
stvotes.append(str(stockham_votes))
dgvotes.append(str(degette_votes))
dovotes.append(str(doane_votes)) 

#next lines print the analysis results
print("Election Results")

print("---------------------------------------")

print(f"Total Votes: " + str(vote_total))

print("---------------------------------------")
# 23.049% (85213)
print(f"Charles Casper Stockham: " + str(stockham) + "(" + str(stvotes) + ")")
# 73.812% (272892)
print(f"Diana DeGette: " + str(degette) + "(" + str(dgvotes) + ")")
# 3.139% (11606)
print(f"Raymon Anthony Doane: " + str(doane) + "(" + str(dovotes) + ")")

print("---------------------------------------")

print(f"Winner: Diana DeGette")

print("---------------------------------------")