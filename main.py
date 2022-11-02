import os
import csv


#store the data in csv 
budgetcsvpath = os.path.join('resources/budget_data.csv')


with open(budgetcsvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    # Read the header row 
    csv_header = next(csvreader)
   #save the csv as a list in order to bring it into memory- thus allowing the len() function to count how many rows there are
     
    csv_list=list(csvreader)
    total_monies=[]
    for col in csv_list:
        total_monies.append(col[1])

#list comprehension to convert strings to int
total_monies=[int(x) for x in total_monies]
#total money
sum_total_monies= sum(total_monies)

print(sum_total_monies)


#total of months
length= len(csv_list) 
print(length)

#avg change in value 
changes=[]
for i in range(1,len(total_monies)):
    changes=total_monies[i]-total_monies[i-1]
    print(changes)

avg=changes/85
print(avg)

avg_monies= sum(total_monies)/86
print(avg_monies)

print(f" Financial Analysis"
" ----------------------------"
" Total Months: {length} Total: {total_monies} Average Change: {avg}Greatest Increase in Profits: Aug-16 ($1862002)"
" Greatest Decrease in Profits: Feb-14 ($-1825558)")