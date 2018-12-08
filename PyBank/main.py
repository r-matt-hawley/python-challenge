import os
import csv 

# Define the path: ./budget_data.csv
data_path = os.path.join(".", "Resources", "budget_data.csv")

# Open the file
with open(data_path, newline='') as data_file:

        budget_data = csv.reader(data_file, delimiter = ",")

        # Skip the first row in the data.
        budget_header = next(budget_data) 

        # Initialize data
        num_months = 0
        net_revenue = 0
        sum_change = 0

        for row in budget_data:

            # Count each month.
            num_months += 1

            # Get this month's name and revenue.
            month_name = row[0]
            month_revenue = int(row[1])

            # Add the current month's revenue to the total revenue
            net_revenue += month_revenue

            # If this is the first month, initiate the superlative data
            if num_months == 1:
                last_month_profit = month_revenue
                greatest_increase = {
                    "month": month_name,
                    "profit": month_revenue
                }
                greatest_decrease = {
                    "month": month_name,
                    "profit": month_revenue
                }
            else:

                # Calculate the difference in profit from last month
                month_change = month_revenue - last_month_profit

                # Add difference to the total amount of change
                sum_change += month_change

                # This month's profit becomes last month's profit
                last_month_profit = month_revenue

                # Check for Greatest Increase
                # Note: If 2 months tie for greatest increase
                # only the first month will be recorded.
                if month_change > greatest_increase["profit"]:
                    greatest_increase["month"] = month_name
                    greatest_increase["profit"] = month_change
                
                # Check for Greatest Decrease
                # Note: If 2 months tie for greatest decrease
                # only the first month will be recorded.
                if month_change < greatest_decrease["profit"]:
                    greatest_decrease["month"] = month_name
                    greatest_decrease["profit"] = month_change

# Print analysis.
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(num_months))
print("Total: $" + str(net_revenue))
print("Average Change: $" + str(round(sum_change/(num_months-1), 2))) 
print("Greatest Increase in Profits: " + greatest_increase["month"] +"($" + str(greatest_increase["profit"]) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease["month"] +"($" + str(greatest_decrease["profit"]) + ")")

    