import pandas as pd 
df = pd.read_csv('titanic.csv')
df.info() # check the data information using 
df.duplicated() # check the duplicate rows
# Categorical columns
cat_col = [col for col in df.columns if df[col].dtype == 'object']
# Numerical columns
num_col = [col for col in df.columns if df[col].dtype != 'object']
# Check the total number of Unique Values in the Categorical Columns
df[cat_col].nunique()