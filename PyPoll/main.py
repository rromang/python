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

#set path for csv file
poll_path = os.path.join('PyPoll','Resources','election_data.csv')
#read csv file and create dataframe
poll_df = pd.read_csv(poll_path)

#define function that will contain all the necessary calculations and print statements
def summary_data():
   #set variable for headings
   heading1 = "Election Results"
   heading2 = "--------------------------------"   
   #calculates total votes by counting the length of the data frame
   total_votes = len(poll_df)                       
   #create dataframe series for names of the candidates by selecting all unique names
   names = pd.Series(poll_df['Candidate'].unique(), name="Name")
   #create dataframe series for the names and votes per candidates by using value counts per candidate in original dataframe and assigning it a new column name
   votes = pd.Series(poll_df['Candidate'].value_counts(),name="Votes")
   #create dataframe series for the names and percent votes per candidates by using value counts per candidate, dividing it by total votes and assigning it a new column name
   perc_votes = pd.Series(((poll_df['Candidate'].value_counts())/total_votes),name="Percent of Votes")
   #establish names as the new index column in percent votes dataframe series
   perc_votes.index = names
   #create new dataframe from the percent votes series
   new_poll_df = pd.DataFrame(perc_votes)
   #create new combined dataframe by joining the percent votes dataframe with the names as index and the votes series
   all_poll_df = new_poll_df.join(votes)
   #find the highest percentage of votes
   winner_votes = all_poll_df["Percent of Votes"].max()
   #loop through the dataframe to find the highest percentage value and return its index for the winner
   for index in all_poll_df.index:
      if all_poll_df.loc[index, "Percent of Votes"] == winner_votes:
         winner = index
   
   #print headings and total votes
   print(heading1)
   print(heading2)
   print(f'Total Votes: {total_votes}')
   print(heading2)
   #loop through combined data frame and print f-string formatted indexes and values
   for index in all_poll_df.index:
      print(f'{index}: {all_poll_df.loc[index,"Percent of Votes"]:.2%} ({all_poll_df.loc[index,"Votes"]})')
   #print the winner
   print(heading2)
   print(f'Winner: {winner}')
   print(heading2)

   #writes the data in a text file
   analysis_file = open(r'/Users/rosaicelaroman/Desktop/Data_BootCamp/LearnPython/python-challenge/PyPoll/Analysis/pyPoll.txt', "a+")
   analysis_file.writelines(heading1 + "\n")
   analysis_file.writelines(heading2 + "\n")
   analysis_file.writelines(f'Total Votes: {total_votes}\n')
   analysis_file.writelines(heading2 + '\n')
   for index in all_poll_df.index:
      analysis_file.writelines(f'{index}: {all_poll_df.loc[index,"Percent of Votes"]:.2%} ({all_poll_df.loc[index,"Votes"]})\n')
   analysis_file.writelines(heading2 + "\n")
   analysis_file.writelines(f'Winner: {winner}\n')
   analysis_file.writelines(heading2 + "\n")
 
   #call function
summary_data()