#import dependencies
import csv


#initialize variables
total_months = 0
total_loss = 0
previous_month = 0
profit_loss_list = []
max_increase = 0
max_increase_month = ''
max_decrease = 0
max_decrease_month = ''
profit_loss_change = 0

#open and read csv
with open('Pybank/Resources/budget_data.csv', 'r') as bd_file:
    reader = csv.reader(bd_file)

    # Skip the header row
    next(reader)

    for row in reader:
        # Count the total number of months
        total_months = total_months + 1

        # Calculate the net total amount of profit/losses over the entire period
        total_loss = total_loss + int(row[1])

        # Calculate the change in profit/loss from the previous month (skip first month as there is no real change)
        if previous_month != 0:
            profit_loss_change = int(row[1]) - previous_month

        # Add the profit/loss change to a list (for calculating the average)
        profit_loss_list.append(profit_loss_change)

        # Check for the greatest increase in profits
        if profit_loss_change > max_increase:
            max_increase = profit_loss_change
            max_increase_month = row[0]

        # Check for the greatest decrease in profits
        if profit_loss_change < max_decrease:
            max_decrease = profit_loss_change
            max_decrease_month = row[0]

        # Set the previous month's profit/loss to the current row's value 
        previous_month = int(row[1])
        
#calculate average change over period

average_change = (sum(profit_loss_list) / total_months)

#print results

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_loss))
print("Average Change $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + str(max_increase_month) + " $" + str(max_increase)) 
print("Greatest Decrease in Profits: " + str(max_decrease_month) + " $" + str(max_decrease))

#export results
output_path =  ('PyBank/Analysis/Financial_Analysis.txt')
with open(output_path, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-------------------------\n")
    outfile.write("Total Months: " + str(total_months) + "\n")
    outfile.write("Total: $" + str(total_loss)  + "\n")
    outfile.write("Average Change $" + str(round(average_change, 2)) + "\n")
    outfile.write("Greatest Increase in Profits: " + str(max_increase_month) + " $" + str(max_increase) + "\n") 
    outfile.write("Greatest Decrease in Profits: " + str(max_decrease_month) + " $" + str(max_decrease) + "\n")


