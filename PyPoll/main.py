#Task: Modernize voting counting

#Script needs to calculate: 
# 1) total number of votes cast, 
# 2)complete list of candidates who received votes, 
# 3)percentage of votes each candidate won, 
# 4)total number of votes each candidate won 
# 5)winner of the election based on popular vote

import os
import csv
import pandas as pd


poll_path = os.path.join('PyPoll','Resources','election_data.csv')

poll_df = pd.read_csv(poll_path)

def summary_data():
   heading1 = "Election Results"
   heading2 = "--------------------------------"

   total_votes = len(poll_df)  #calculates total votes by counting the length of the data frame 
   
   
   votes = poll_df['Candidate'].value_counts()

   perc_votes = ((poll_df['Candidate'].value_counts())/total_votes)*100
   
   
   

   #grouped_poll_df = pd.DataFrame(counts_df.groupby(["Candidate"]).sum())
   
   #grouped_poll_df.rename(columns={'Candidate': "Candidate", "Votes":"Votes"})
   #sorted_df = grouped_poll_df.sort_values("Candidate", ascending=False)

   
   print(heading1)
   print(heading2)
   print(f'Total Votes: {total_votes}')
   print(heading2)
   
   print(perc_votes
   

summary_data()