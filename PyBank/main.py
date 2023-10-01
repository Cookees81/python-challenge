#set up operating system
import os
#reads csv
import csv

#next lines print the title
print("Financial Analysis")

print("---------------------------------------")

budget_csv = os.path.join(r"C:\Users\salaz\OneDrive\Desktop\Class_Folder\homework\python-challenge\PyBank", "Resources", "budget_data.csv")

changes = []

with open(budget_csv, "r") as f:
    readfile = csv.reader(f)
    # skip header
    header = next(readfile)

month_total = (len(budget_csv)-17)

dollar_total = 0
with open(budget_csv) as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        dollar_total = dollar_total + int(row['Profit/Losses'])

    for row in data:
        changes.append(row[2])

top = 0
with open(budget_csv) as csvfile1:
    data = csv.DictReader(csvfile1)
    for row in data:
        top = int(row['Profit/Losses'])

bottom = 0
with open(budget_csv) as csvfile2:
    data = csv.DictReader(csvfile2)
    for row in data:
        top = next(csvfile2)        
        bottom = int(row["Profit/Losses"])


changes = []
with open(budget_csv) as csvfile1:
    data = csv.DictReader(csvfile1)
    for row in data:
        changes = int(top) - int(bottom)


print(f"Total Months: {month_total}")
print(f"Total : ${dollar_total}")
print(f"Average Change: {changes}")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")
    








