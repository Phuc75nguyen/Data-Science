import pandas as pd
import numpy as np

def load_data(file_paths):
    data_frames = [pd.read_csv(path) for path in file_paths]
    return data_frames

def preprocess_2018(df):
    df = df.rename(columns={'Your level': 'level', 'Current Salary': 'salary'}, inplace=False)
    df = df.drop(['Salary two years ago', 'Timestamp', 'Are you getting any Stock Options?'], axis=1, inplace=False)
    df['main tech'] = np.nan
    df['Number of vacation days'] = np.nan
    return df

def preprocess_2019(df):
    df = df.rename(columns={
        'Zeitstempel': 'Timestamp',
        'Position (without seniority)': 'Position',
        'Seniority level': 'level',
        'Yearly brutto salary (without bonus and stocks)': 'salary',
        'Your main technology / programming language': 'main tech'
    }, inplace=False)
    df = df.drop(['Company name ', 'Timestamp', 'Yearly bonus', 'Yearly stocks', 
                  'Number of home office days per month', 'Сontract duration', '0', 'Company business sector'], axis=1, inplace=False)
    return df

def preprocess_2020(df):
    df = df.rename(columns={
        'Total years of experience': 'Years of experience',
        'Seniority level': 'level',
        'Yearly brutto salary (without bonus and stocks) in EUR': 'salary',
        'Your main technology / programming language': 'main tech'
    }, inplace=False)
    df = df.drop(['Yearly bonus + stocks in EUR', 'Timestamp', 'Employment status', 
                  'Сontract duration', 'Years of experience in Germany'], axis=1, inplace=False)
    return df

def merge_data(dfs):
    dfs[1] = dfs[1].reindex(columns=dfs[0].columns)
    dfs[2] = dfs[2].reindex(columns=dfs[0].columns)
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df
