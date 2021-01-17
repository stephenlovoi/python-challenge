import os
import csv

#budget data

budget_csv = os.path.join("Resources", "budget_data.csv")

total_months = []
total_profit = []
profit_change = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csvheader = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        profit = total_profit.append(int(row[1]))

    for i in range(len(total_profit) - 1):
        profit_change.append(total_profit[i + 1] - total_profit[i])

    average_profit = round(sum(profit_change) / len(total_months))
    total_profit_change = sum(total_profit)

    max_increase = max(profit_change)
    max_decrease = min(profit_change)


#election data

election_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

with open(election_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
            total_votes +=1

            if row[2] == "Khan":
                khan += 1
            elif row[2] == "Correy":
                correy += 1
            elif row[2] == "Li":
                li += 1
            elif row[2] == "O'Tooley":
                otooley += 1


    khan_percentage = khan / total_votes * 100
    correy_percentage = correy / total_votes * 100
    li_percentage = li / total_votes * 100
    otooley_percentage = otooley / total_votes * 100

    winner = 0

    if khan_percentage > correy_percentage > li_percentage > otooley_percentage:
        winner = "Khan"
    elif correy_percentage > khan_percentage > li_percentage > otooley_percentage:
        winner = "Correy"
    elif li_percentage > khan_percentage > correy_percentage > otooley_percentage:
        winner = "Li"
    elif otooley_percentage > khan_percentage > correy_percentage > li_percentage:
        winner = "O'Tooley"


#print statements

print(" ")
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${total_profit_change}")
print(f"Average Change: ${average_profit}")
print(f"Greatest Increase in Profits: ${max_increase}")
print(f"Greatest Decrease in Profits: ${max_decrease}")

print(" ")
print(" ")

print("Election Results")
print("----------------------")
print(f"Total Votes: {(total_votes)}")
print("----------------------")
print(f"Khan: {round(khan_percentage, 2)}%")
print(f"Correy: {round(correy_percentage, 2)}%")
print(f"Li: {round(li_percentage, 2)}%")
print(f"O'Tooley: {round(otooley_percentage, 2)}%")
print("----------------------")
print(f"Winner: {winner}")
print(" ")


#output files

output_file_budget = os.path.join("Analysis", "budget_data.txt")

with open(output_file_budget, "w", newline="") as datafile:
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("----------------------")
    datafile.write("\n")
    datafile.write(f"Total Months: {len(total_months)}")
    datafile.write("\n")
    datafile.write(f"Total: ${total_profit_change}")
    datafile.write("\n")
    datafile.write(f"Average Change: ${average_profit}")
    datafile.write("\n")
    datafile.write(f"Greatest Increase in Profits: ${max_increase}")
    datafile.write("\n")
    datafile.write(f"Greatest Decrease in Profits: ${max_decrease}")


output_file_election = os.path.join("Analysis", "election_results.txt")

with open(output_file_election, "w", newline="") as datafile:
    datafile.write("Election Results")
    datafile.write("\n")
    datafile.write("----------------------")
    datafile.write("\n")
    datafile.write(f"Total Votes: {(total_votes)}")
    datafile.write("\n")
    datafile.write("----------------------")
    datafile.write("\n")
    datafile.write(f"Khan: {round(khan_percentage, 2)}%")
    datafile.write("\n")
    datafile.write(f"Correy: {round(correy_percentage, 2)}%")
    datafile.write("\n")
    datafile.write(f"Li: {round(li_percentage, 2)}%")
    datafile.write("\n")
    datafile.write(f"O'Tooley: {round(otooley_percentage, 2)}%")
    datafile.write("\n")
    datafile.write("----------------------")
    datafile.write("\n")
    datafile.write(f"Winner: {winner}")