#import dependencies
import csv


#initialize variables
total_vote = 0
candidate_list = []
vote_counts = {}
winner = ""


#open and read csv
with open('PyPoll/Resources/election_data.csv', 'r') as poll_file:
    reader = csv.reader(poll_file)

    # Skip the header row
    next(reader)

    for row in reader:
#get total votes    
        # increment vote count
        total_vote = total_vote + 1
        
# get list of candidates
        # get candidate names
        candidate_name = row[2]

        # establish candidates in dictionary and begin counting their votes
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name) 
            vote_counts[candidate_name] = 1

# total votes won per candidate
        # add vote to existing candidate
        else:
            vote_counts[candidate_name] += 1

#establish percentage of votes per candidate
    # new dictionary for vote percent
    vote_percent = {}

    # loop through dictionary to find votes per candidate        
    for candidate in vote_counts:

        # calculate percentage of votes per candidate
        percentage = vote_counts[candidate] / total_vote *100

        # store value in new dictionary
        vote_percent[candidate] = round(percentage, 3)

# declare winner
    #establish new variable for winners votes
    winner_votes = 0

    #loop through dictionary to find max votes + candidate
    for candidate in vote_counts:
        if vote_counts[candidate] > winner_votes:
            winner = candidate
            winner_votes = vote_counts[candidate]






#print results

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_vote))
print("-------------------------")
for candidate in candidate_list:
    print(candidate + " " + str(vote_percent[candidate]) + "% (" + str(vote_counts[candidate]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#export results
output_path =  ('PyPoll/Analysis/Election_Analysis.txt')
with open(output_path, 'w') as outfile:
    outfile.write("Election Results \n")
    outfile.write("-------------------------\n")
    outfile.write("Total Votes: " + str(total_vote) + "\n")
    outfile.write("-------------------------\n")
    for candidate in candidate_list:
        outfile.write(candidate + " " + str(vote_percent[candidate]) + "% (" + str(vote_counts[candidate]) + ")\n")
    outfile.write("-------------------------\n")
    outfile.write("Winner: " + winner + "\n")
    outfile.write("-------------------------\n")


