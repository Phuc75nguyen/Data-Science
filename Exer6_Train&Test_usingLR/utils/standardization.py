import re

def standardize_experience(df):
    for i, val in df['Years of experience'].items():
        try:
            df.at[i, 'Years of experience'] = float(val)
        except:
            if isinstance(val, str):
                if 'less than year' in val:
                    df.at[i, 'Years of experience'] = 0.9
                elif re.search(r'\d+', val):
                    df.at[i, 'Years of experience'] = float(re.search(r'\d+', val).group(0))

def standardize_vacation_days(df):
    for i, val in df['Number of vacation days'].items():
        if val == 'unlimited' or val == 'Unlimited':
            df.at[i, 'Number of vacation days'] = 1000
        elif re.search(r'\d+', str(val)):
            df.at[i, 'Number of vacation days'] = float(re.search(r'\d+', str(val)).group(0))
