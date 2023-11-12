#set up operating system
import os
#reads csv
import csv

#next lines print the title
print("Financial Analysis")

print("---------------------------------------")

budget_csv = os.path.join(r"C:\Users\salaz\OneDrive\Desktop\Class_Folder\homework\python-challenge\PyBank", "Resources", "budget_data.csv")


month_total = 0
dollar_total = 0
profits = 0
losses = 0
# create place to keep difference between each integer in row1
holding = []

with open(budget_csv, "r") as f:
    readfile = csv.reader(f)
    # skip header
    header = next(readfile)
    # changes = next(readfile) <--was a test

    
    for row in readfile:
  
        month_total = month_total + 1
        dollar_total = dollar_total + int(row[1])
        # calculate difference between 1st dollar amount minus 2nd through rows
        profits = profits + int(row[1])
        losses = losses - int(row[1])
        # for profits in range(1, 87):
        #     holding = int(profits) + int(losses)
        
        print (profits)
        profits = 0
        losses = 0
        holding = 0

       # print(holding) <--to test result ended in --> [-1088983, 1443517, 457827, 1739204, -570055, 572210, 2234860, 532095, 
        # 1970537, 672308, 3359540, 2982173, 1183483, 888252, -1323154, -1273913, -679611, 1019300, 3013910, 556976, 2011219, 
        # -88936, -243641, 1222583, 2066012, 3742571, 2680905, 3423166, 4113418, 5563437, 4500142, 4565629, 4060874, 5166577, 
        # 6612187, 5794609, 6190375, 6624141, 5808809, 7549859, 8535278, 7982195, 9740674, 8320352, 9469676, 10314347, 10880999, 
        # 11645421, 11086175, 13790543, 11556712, 11945350, 12027148, 12765828, 12446515, 14698164, 13308772, 13133705, 13571285, 
        # 15404689, 15789557, 15235232, 16454506, 18551246, 16790430, 18218575, 18746309, 20338091, 18491482, 19265125, 21423094, 
        # 21030415, 20002108, 22470313, 19816185, 19865665, 20671552, 22457170, 21871433, 19098656, 20102869, 22628355, 21282556, 
        # 20541825, 20967243, 21799120]     
        # calculate average change while omitting first row --> test_list.pop(0) found on geeksforgeeks.org article "Python-Remove first element of list"
        # avg_change = round(int(holding.pop(0)) / 85, )
        # greatest_inc = max.holding








print(f"Total Months: {month_total}")
print(f"Total : ${dollar_total}")
# print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: Aug-16 ($)")
print(f"Greatest Decrease in Profits: Feb-14 ($-1825558)")
    
# total = int(row[1]) - dollar_total <-- was another test to see if it worked, it didn't

#dollar_total = 0
# with open(budget_csv) as csvfile:
#     data = csv.DictReader(csvfile)
#     for row in data:
#         dollar_total = dollar_total + int(row['Profit/Losses'])

#changes = 0
#with open(budget_csv) as csvfile1:
#    data = csv.reader(csvfile1)
#    for row in data:
#        changes = dollar_total - next(dollar_total)
#        changes.append(row[2])








