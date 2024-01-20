import os
import csv

# Function to perform financial analysis
def financial_analysis(csv_file):
    # Initialize lists to store data
    months = []
    amounts = []

    # Read CSV file and extract data
    with open(csv_file, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip header row

        for row in csvreader:
            months.append(row[0])
            amounts.append(int(row[1]))

    # Calculate financial metrics
    total_months = len(months)
    total_amount = sum(amounts)
    average_change = round(total_amount / total_months, 2)

    max_increase = max(amounts)
    max_decrease = min(amounts)

    max_inc_month = months[amounts.index(max_increase)]
    max_dec_month = months[amounts.index(max_decrease)]

    # Display the report
    print("Financial Analysis")
    print("---------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_amount}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_inc_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_dec_month} (${max_decrease})")

    # Save the report to file
    with open('FinancialAnalysis.txt', 'w') as result_file:
        result_file.write("Financial Analysis\n")
        result_file.write("---------------------------------------------------\n")
        result_file.write(f"Total Months: {total_months}\n")
        result_file.write(f"Total: ${total_amount}\n")
        result_file.write(f"Average Change: ${average_change}\n")
        result_file.write(f"Greatest Increase in Profits: {max_inc_month} (${max_increase})\n")
        result_file.write(f"Greatest Decrease in Profits: {max_dec_month} (${max_decrease})")

# Define the path to the CSV file
csv_path = os.path.join('Resources','budget_data.csv')

# Perform financial analysis
financial_analysis(csv_path)


