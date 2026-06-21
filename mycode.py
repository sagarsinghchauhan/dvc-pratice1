import pandas as pd
import os 

# create a sample dataframe with column names 
data = {'Name':['alice','bob','charlie',],
        'Age':[25,30,35],
        'City':['New york','Los angeles','chaicago']
        }

df = pd.DataFrame(data)

# Adding new row to df for v2
new_row_loc = {'Name':'gf1','Age':20,'City':'city1'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for v3
# new_row_loc2 = {'Name':'gf1','Age':30,'City':'city1'}
# df.loc[len(df.index)] = new_row_loc2

#ensure the 'data' directory exits at the root level 
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

#define the file_path 
file_path = os.path.join(data_dir,'sample_data.csv')

# save the dataframe to a csvfile , including column names 
df.to_csv(file_path, index= True)

print(f"CSV file saved to {file_path}")
