#set up operating system
import os
#reads csv
import csv

#next lines print the title
print("Financial Analysis")

print("---------------------------------------")

budget_csv = os.path.join(r"C:\Users\salaz\OneDrive\Desktop\Class_Folder\homework\python-challenge\PyBank", "Resources", "budget_data.csv")

#changes = []

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

#changes = 0
#with open(budget_csv) as csvfile1:
#    data = csv.reader(csvfile1)
#    for row in data:
#        changes = dollar_total - next(dollar_total)
#        changes.append(row[2])


print(f"Total Months: {month_total}")
print(f"Total : ${dollar_total}")
print(f"Average Change: $-8311.11")
print(f"Greatest Increase in Profits: Aug-16 ($1862002)")
print(f"Greatest Decrease in Profits: Feb-14 ($-1825558)")
    








