import os
import csv

#set variables
monthcount = 0
totalprofit = 0
prev_net = 0
average_change = 0
max_increase = 0
max_decrease = 0

#create list of monthly changes & month names
monthly_changes = []
month_names = []

#set path
budgetdata_csv = os.path.join("..", "Resources", "budget_data.csv")

#open csv file
with open(budgetdata_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#omit header
    csv_header = next(csv_reader)

#find first month manually 
    firstrow = next(csv_reader)
    monthcount += 1
    totalprofit += int(firstrow[1])
    prev_net = int(firstrow[1])

#loop through all rows  
    for row in csv_reader:

#add 1 to monthcount for each row
        monthcount += 1
        month_names.append(row[0])

#add value of each to profit        
        totalprofit += int(row[1])

#find net change
        netchange = int(row[1]) - prev_net
        prev_net = int(row[1])
        monthly_changes.append(netchange)
        average_change = round(sum(monthly_changes) / len(monthly_changes), 2)

#find max & min net changes
        max_increase = max(monthly_changes)
        max_decrease = min(monthly_changes)

    for month in monthly_changes:
        if month == max_increase:
            bestmonth = monthly_changes.index(max_increase)
        elif month == max_decrease:
            worstmonth = monthly_changes.index(max_decrease)
            
#print values
    print("Financial Analysis")
    print('-'*25)
    print(f'Total months: {monthcount}')
    print(f'Total: ${totalprofit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {month_names[bestmonth]} (${max_increase})')
    print(f'Greatest Decrease in Profits: {month_names[worstmonth]} (${max_decrease})')

output_file = os.path.join("..", "analysis", "analysis.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write('-'*25)
    file.write("\n")
    file.write(f'Total months: {monthcount}')
    file.write("\n")
    file.write(f'Total: ${totalprofit}')
    file.write("\n")
    file.write(f'Average Change: ${average_change}')
    file.write("\n")
    file.write(f'Greatest Increase in Profits: {month_names[bestmonth]} (${max_increase})')
    file.write("\n")
    file.write(f'Greatest Decrease in Profits: {month_names[worstmonth]} (${max_decrease})')