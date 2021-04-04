import os
import csv


poll_csv = os.path.join('Resources','election_data.csv')

#define function for final summary table and export to txt
def summary_table():
    #create file with append mode and add each string line then close file
    
    analysis_file = open(os.path.join('Analysis','pyPoll_2.txt'), "a+")
    
    winner = max(cand_dict, key=cand_dict.get)

    heading1 = "Election Results \n----------------------------\n"
    print(heading1)
    analysis_file.writelines(heading1)

    print(f'Total Votes: {total_votes}')
    print(f'---------------------------- \n')
    analysis_file.writelines(f'Total Votes: {total_votes}\n')
    analysis_file.writelines(f'---------------------------- \n')

    for key, [value1, value2] in combined_dict.items():
        print(f'{key}: {value1:.3%} ({value2})')
        analysis_file.writelines(f'{key}: {value1:.3%} ({value2})\n')
    
    print(f'---------------------------- \n')
    analysis_file.writelines(f'---------------------------- \n')
    print(f'Winner: {winner}')
    analysis_file.writelines(f'Winner: {winner}\n')
    print(f'---------------------------- \n')
    analysis_file.writelines(f'---------------------------- \n')

#open the csv file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips header
    header = next(csvreader)
    #initialize all necessary lists and dictionaries
    candidates = []
    unique_candidates = []
    votes_per_candidate = []
    perc_votes_candidates = []

    #loop to append to a list with all instances a name of a candidate appears in csv
    for row in csvreader:
        candidates.append(row[2])
    #calculate number of total votes in election by counting all elements in list populated above
    total_votes = len(candidates)
    #loop for populating list with unique candidate names
    for x in candidates:
        if x not in unique_candidates:
           unique_candidates.append(x) 
    #counting number of unique names in list populated above
    num_candidates = len(unique_candidates)
    #looping through list of candidates and comparing it to the position i in list of unique candidates to count the
    #instances the candidate name repeats, storing it as a variable that gets added to list of votes per candidates
    #once it finished counting all instances unique_candidate in position i appears in list. Once it is done sets the
    #unique candidate list position i to 1 more than previous instance.
    i = 0
    while i < num_candidates:
        votes = candidates.count(unique_candidates[i])
        votes_per_candidate.append(votes)
        i = i+1
    #loop for calculating percent of votes per candidate by going through votes per candidate list and dividing the 
    #items for the total of votes
    for j in votes_per_candidate:
        perc_votes = (j/total_votes)
        perc_votes_candidates.append(perc_votes)

    #create dictionary for candidates and percent votes, candidates and votes per candidate then combine them by key
    cand_dict = dict(zip(unique_candidates, perc_votes_candidates))
    cand_dict2 = dict(zip(unique_candidates, votes_per_candidate))
    combined_dict = {key:[cand_dict[key], cand_dict2[key]] for key in cand_dict}

#call function
summary_table()