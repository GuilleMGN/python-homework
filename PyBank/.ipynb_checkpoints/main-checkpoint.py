# Import Path class from the pathlib library and csv
from pathlib import Path
import csv

# Specify input Path
csvpath = Path("budget_data.csv")

# Initialize all variables
records = []
changes = []
total_months = 0
total = 0
change = 0
previous = 0
average_change = 0
greatest_increase_profits = 0
greatest_increase_date = None
increase_amount = 0
greatest_decrease_profits = 0
greatest_decrease_date = None
decrease_amount = 0

# Open csv file as an object
with open(csvpath, "r") as csvfile:
#     Seperator set to ","
    csvreader = csv.reader(csvfile, delimiter=",")
#     Skip header
    csv_header = next(csvreader)
        
#     Read each row after the header
    for row in csvreader:
        total_months = total_months + 1
        date = row[0]
        profit_losses = int(row[1])
        total = total + profit_losses
        change = profit_losses - previous
        changes.append(change)
        previous = profit_losses
#         Check greatest increase/decrease
        if profit_losses > greatest_increase_profits:
            greatest_increase_profits = profit_losses
            greatest_increase_date = date
            increase_amount = change
        elif profit_losses < greatest_decrease_profits:
            greatest_decrease_profits = profit_losses
            greatest_decrease_date = date
            decrease_amount = change
        
#     Function to calculate average
    def Average(list):
        return sum(list) / len(list) 
    average_change = round(Average(changes), 2)

# Display Financial Analysis in terminal
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${decrease_amount})")
print("")

# Set the path for the output.txt
output_path = Path("output.txt")

# Open the output path as a file
with open(output_path, "w") as file:
#     Write Financial Analysis info to .txt file
    file.write(f"Financial Analysis \n")
    file.write(f"---------------------------- \n")
    file.write(f"Total Months: {total_months} \n")
    file.write(f"Total: ${total} \n")
    file.write(f"Average Change: ${average_change} \n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${increase_amount}) \n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${decrease_amount}) \n")
