#Task: Analyze financial records

#Script needs to calculate: 1) total number of months in dataset, 
# 2)net total amt of profit/losses over entire period, 
# 3)changes in "Profit/Losses" over entire period, then find the average of those changes, 
# 4)greatest increase in profits (date and amount) over entire period, 
# 5)greatest decrease in losses (date and amount) over entire period

import os
import csv
from statistics import mean



budget_csv = os.path.join('Resources','budget_data.csv')

#define function for the calcs
def totals(budget_data):
   
    heading1 = "Financial Analysis \n"                 #header info
    heading2 = "------------------------------ \n"     #divider
    total_months = len(months)                      #eq for total months
    total_profloss = sum(profloss)                  #eq for sum of all prof/loss
    avg_change = mean(change_profloss)              #eq for average change
    change_dictval = change_dict.values()           #getting jus values for the dictionary
                                                    #containing months and change in profit pairs
    great_inc = max(change_dictval)                 #calculate greatest increase by finding max value in dict
    max_key = max(change_dict, key=change_dict.get) #finding the key pair for max value in dict
    great_dec = min(change_dictval)                 #calculate greatest decrease by finding min value in dict
    min_key = min(change_dict, key=change_dict.get) #finding the key pair for min value in dict
   

    #Print all the info
    print(heading1)
    print(heading2)
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profloss}")
    print(f"Average change: ${avg_change:.2f}")
    print(f"Greatest increase in profits: {max_key} (${great_inc})")
    print(f"Greatest decrease in profits: {min_key} (${great_dec})")
    
    #create text file; create strings for all print lines.
    str_total_months = (f"Total Months: {total_months} \n")
    str_total_profloss = (f"Total: ${total_profloss} \n")
    str_avg_change = (f"Average change: ${avg_change:.2f} \n")
    str_great_inc = (f"Greatest increase in profits: {max_key} (${great_inc}) \n")
    str_great_inc = (f"Greatest decrease in profits: {min_key} (${great_dec}) \n")
    #create file with append mode and add each string line then close file
    analysis_file = open(r'/Users/rosaicelaroman/Desktop/Data_BootCamp/LearnPython/python-challenge/PyBank/Analysis/pyBank.txt', "a+")
    analysis_file.writelines(heading1)
    analysis_file.writelines(heading2)
    analysis_file.writelines(str_total_months)
    analysis_file.writelines(str_total_profloss)
    analysis_file.writelines(str_avg_change)
    analysis_file.writelines(str_great_inc)
    analysis_file.writelines(str_great_inc)

    analysis_file.close()

#open the csv file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips header
    header = next(csvreader)
   #initialize all necessary lists and dictionaries
    months =[]
    profloss = []
    change_profloss = []
    month_change_profloss = []
    change_dict = {}

    # Loop through the data
    for row in csvreader:
        #loops through data and extracts months and appends to months list
        months.append(row[0])
        #changes the data in prof/loss column to integer
        row[1] = int(row[1])
        #loops through data and extracts prof/loss and appends to prof/loss list
        profloss.append(row[1])

    for i in range(1, len(profloss)):
        #loops through prof/loss list, calculates the change and appends to change prof/loss list
        change_profloss.append(profloss[i]-profloss[i-1])
    for i in range(1, len(months)):
        #loops through months list, calculates appends to months corresponding to change prof/loss list
        month_change_profloss.append(months[i])
    #creates a dictionary for month and change prof/loss pairs
    change_dict = {month_change_profloss[i]: change_profloss[i] for i in range(len(month_change_profloss))}
    #calls function to do all calculations and 
    
    totals(row)

