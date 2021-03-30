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

df = pd.read_csv(poll_path)
print(df)