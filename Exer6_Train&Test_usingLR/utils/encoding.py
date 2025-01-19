import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def fill_nan_with_mean_or_freq(df, field, method='mean'):
    if method == 'mean':
        df[field] = df[field].fillna(int(round(df[field].mean())))
    elif method == 'freq':
        df[field] = df[field].fillna(df[field].value_counts().index[0])

def standardize_columns(df):
    df['Gender'] = df['Gender'].replace({'Male': 'M', 'Female': 'F'})

def ordinal_encode_level(df):
    valid_levels = ["Junior", "Mid", "Senior", "Lead", "Manager", "Director", "VP"]
    df = df[df['level'].isin(valid_levels)].copy()  # Add .copy() to avoid SettingWithCopyWarning

    ordinal_encoder = OrdinalEncoder(categories=[valid_levels])
    df.loc[:, 'level_encoded'] = ordinal_encoder.fit_transform(df[['level']])
    return df

def one_hot_encode_columns(df):
    df = pd.get_dummies(df, columns=['Gender', 'City', 'Position', 'Main language at work', 'Company type', 'main tech'])
    return df

def fill_missing_values(df, field):
    if df[field].dtype == 'float64' or df[field].dtype == 'int64':
        df[field] = df[field].fillna(int(round(df[field].mean())))
    else:
        df[field] = df[field].fillna(df[field].value_counts().index[0])

def encode_level_column(df):
    ordinal_encoder = OrdinalEncoder()
    df.loc[:, 'level_encoded'] = ordinal_encoder.fit_transform(df[['level']])
    df = df.drop(columns=['level'])  # Drop the original 'level' column
    return df
