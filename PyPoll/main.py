import os
import csv

#set variables & lists
number_votes = 0
candidates = {}
vote_percentage = 0

#set path
electiondata_csv = os.path.join("..", "Resources", "election_data.csv")

#open csv file
with open(electiondata_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#omit header
    csv_header = next(csv_reader)

#count rows
    for row in csv_reader:
        number_votes += 1

#create list of candidates & add up their values 
# Tutorials: Could I make str(row[2]) a variable? How?  
        if str(row[2]) not in candidates:
            candidates.update({str(row[2]):1})
        else: 
            candidates[str(row[2])] += 1

#print values so far
    print("Election Results")
    print('-'*25)
    print(f"Total Votes: {number_votes}")
    print('-'*25)

#print name, percentage, and votes in a loop
    for name in candidates:
        votes = candidates.get(name)
        vote_percentage = round(float(votes) / float(number_votes) * 100, 3)
        print(f'{name}: {vote_percentage}% ({votes})')
    print('-'*25)

#find & print winner
winner = max(zip(candidates.values(), candidates.keys()))[1]
print(f'Winner: {winner}')
print('-'*25)

output_file = os.path.join("..", "analysis", "analysis.txt")
with open(output_file, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write('-'*25)
    file.write("\n")
    file.write(f"Total Votes: {number_votes}")
    file.write("\n")
    file.write('-'*25)
    file.write("\n")

    for name in candidates:
        votes = candidates.get(name)
        vote_percentage = round(float(votes) / float(number_votes) * 100, 3)
        file.write(f'{name}: {vote_percentage}% ({votes})')
        file.write("\n")
    file.write('-'*25)
    file.write("\n")

    winner = max(zip(candidates.values(), candidates.keys()))[1]
    file.write(f'Winner: {winner}')
    file.write("\n")
    file.write('-'*25)




