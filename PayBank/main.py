import os
import csv


# Provide the file path for the CSV
budget_csv = os.path.join("Resources", "budget_data.csv")

# Checking the 'analysis' folder if it doesn't exist
analysis_folder = os.path.join("analysis")

# Open CSVfile
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader)

    # Declare variables to store values
    total_month = 0
    total_amount = 0
    last_PnL = 0
    changes = []
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}

    for row in csvreader:
            
        # Find out the total number of months and the overall profit or loss
        date = row[0]
        profit_loss = int(row[1])

        # Finad out the total number of months and the overall  profit or loss
        total_month += 1
        total_amount += profit_loss

        # Determine all of changes
        change = profit_loss - last_PnL

        # find out change in profit,loss and store
        if total_month > 1:
            changes.append(change)

        # Update greatest increase and decrease
        if change > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change

        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change

        # Update last profit and loss
        last_PnL = profit_loss

        # Calculate average
    average_change = sum(changes) / len(changes)

    # Print result to terminal
    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Net Total: ${total_amount}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

    # Export result to a text file in the 'analysis' folder
    output_path = os.path.join("analysis_folder", "financial_analysis.txt")
    with open(output_path, "w") as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("--------------------------------\n")
        output_file.write(f"Total Months: {total_month}\n")
        output_file.write(f"Net Total: ${total_amount}\n")
        output_file.write(f"Average Change: ${average_change:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")


