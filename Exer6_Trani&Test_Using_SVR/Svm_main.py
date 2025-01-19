import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df_2020 = pd.read_csv('D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Exer6_Trani&Test_Using_SVM/data/IT_Salary_Survey_EU_2018.csv')
df_2019 = pd.read_csv('D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Exer6_Trani&Test_Using_SVM/data/IT_Salary_Survey_EU_2019.csv')
df_2018 = pd.read_csv('D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Exer6_Trani&Test_Using_SVM/data/IT_Salary_Survey_EU_2020.csv')

new_df_2018 = df_2018.rename(columns={'Your level':'level', \
                                      'Current Salary':'salary'}, inplace=False)

# delete column 'Salary two years ago', 'Are you getting any Stock Options?' because only available in 2018
# delete column 'Timestamp' for not having correlation to salary
new_df_2018 = new_df_2018.drop(['Salary two years ago', \
                                'Timestamp', \
                                'Are you getting any Stock Options?'], axis=1,errors='ignore')
# insert missing column
new_df_2018['main tech'] = np.nan
new_df_2018['Number of vacation days'] = np.nan

new_df_2019 = df_2019.rename(columns={'Zeitstempel':'Timestamp', \
                                      'Position (without seniority)':'Position', \
                                      'Seniority level':'level', \
                                      'Yearly brutto salary (without bonus and stocks)':'salary', \
                                      'Yearly brutto salary (without bonus and stocks) one year ago. Only answer if staying in same country':'Salary one year ago',\
                                      'Your main technology / programming language':'main tech'}, inplace=False)

# delete these column because of lacking in other file or having so many null row
new_df_2019 = new_df_2019.drop(['Company name ', \
                                'Timestamp', \
                                'Yearly bonus', \
                                'Yearly stocks', \
                                'Yearly bonus one year ago. Only answer if staying in same country', \
                                'Yearly stocks one year ago. Only answer if staying in same country', \
                                'Number of home office days per month', \
                                'Сontract duration', \
                                '0', \
                                'Company business sector'], axis=1, inplace=False)

new_df_2020 = df_2020.rename(columns={'Total years of experience':'Years of experience', \
                                      'Seniority level':'level', \
                                      'Yearly brutto salary (without bonus and stocks) in EUR':'salary', \
                                      'Annual brutto salary (without bonus and stocks) one year ago. Only answer if staying in the same country':'Salary one year ago',\
                                      'Your main technology / programming language':'main tech'}, inplace=False)
# delete these column because of lacking in other file or having so many null row
new_df_2020 = new_df_2020.drop(['Yearly bonus + stocks in EUR', \
                                'Timestamp', \
                                'Annual bonus+stocks one year ago. Only answer if staying in same country', \
                                'Have you lost your job due to the coronavirus outbreak?', \
                                'Have you been forced to have a shorter working week (Kurzarbeit)? If yes, how many hours per week', \
                                'Have you received additional monetary support from your employer due to Work From Home? If yes, how much in 2020 in EUR',\
                                'Employment status', \
                                'Сontract duration', \
                                'Years of experience in Germany',\
                                'Other technologies/programming languages you use often'], axis=1, errors="ignore")

# align the column to 2018
new_df_2019 = new_df_2019.reindex(columns=new_df_2018.columns)
new_df_2020 = new_df_2020.reindex(columns=new_df_2018.columns)

# concat df of 3 year
df_3year = pd.concat([new_df_2018, new_df_2019, new_df_2020])

def fill_nan_with_mean_or_freq(field, value='mean'):
  val = None
  if value == 'mean':
    val = int(round(df_3year.loc[:, field].mean()))
  elif value == 'freq':
    val = df_3year[field].value_counts().index[0]
  df_3year[field] = df_3year[field].fillna(val)

# fill na value of Age with mean
fill_nan_with_mean_or_freq('Age')

# standardize value in gender column
for i, value in df_3year['Gender'].items():
  if value == 'Male':
    df_3year.at[i, 'Gender'] = 'M'
  elif value == 'Female':
    df_3year.at[i, 'Gender'] = 'F'
# fill na value of Gender with most frequence value
fill_nan_with_mean_or_freq('Gender', 'freq')

# fill na value of City with most frequence value
fill_nan_with_mean_or_freq('City', 'freq')

# fill na value of Position with most frequence value
fill_nan_with_mean_or_freq('Position', 'freq')

# standardize
for i, val in df_3year['Years of experience'].items():
  try:
    df_3year.at[i, 'Years of experience'] = float(val)
  except:
    match val:
      case '1,5':
        df_3year.at[i, 'Years of experience'] = 1.5
      case '2,5':
        df_3year.at[i, 'Years of experience'] = 2.5
      case '15, thereof 8 as CTO':
        df_3year.at[i, 'Years of experience'] = 15
      case '6 (not as a data scientist, but as a lab scientist)':
        df_3year.at[i, 'Years of experience'] = 6
      case 'less than year':
        df_3year.at[i, 'Years of experience'] = 0.9
      case '1 (as QA Engineer) / 11 in total':
        df_3year.at[i, 'Years of experience'] = 11
# fill na value of experience with mean
fill_nan_with_mean_or_freq('Years of experience')

# fill na value of level with most frequence value
fill_nan_with_mean_or_freq('level', 'freq')

# fill na value of salary with mean
fill_nan_with_mean_or_freq('salary')

# fill na value of salary with mean
fill_nan_with_mean_or_freq('Salary one year ago')

# fill na value of salary 1 year ago with most frequence value
fill_nan_with_mean_or_freq('Main language at work', 'freq')

#standadize
for i, val in df_3year['Company size'].items():
  if val is np.nan: continue
  value = None
  match val:
    case '1000+':
      value = 1000
    case '100-1000':
      value = 1100 // 2
    case '101-1000':
      value = 1101 // 2
    case '50-100':
      value = 150 // 2
    case '10-50':
      value = 60 // 2
    case '11-50':
      value = 61 // 2
    case '51-100':
      value = 151 // 2
    case 'up to 10':
      value = 10
  df_3year.at[i, 'Company size'] = value
# fill na value of company size with mean
fill_nan_with_mean_or_freq('Company size')

# fill na value of Company type with most frequence value
fill_nan_with_mean_or_freq('Company type', 'freq')

# fill na value of main tech with most frequence value
fill_nan_with_mean_or_freq('main tech', 'freq')

# fill na value of Number of vacation days with most frequence value
fill_nan_with_mean_or_freq('Number of vacation days', 'freq')

# standardize
column = 'Number of vacation days'
for i, val in df_3year[column].items():
  try:
    df_3year.at[i, column] = float(val)
  except:
    match val:
      case 'unlimited '| 'Unlimited':
        df_3year.at[i, column] = 1000
      case '(no idea)':
        df_3year.at[i, column] = -1
      case '~25' | '23+' | '24 labour days' | '30 in contract (but theoretically unlimited)':
        import re
        df_3year.at[i, column] = re.compile(r'\d\d').search(val).group(0)


# sorting level column from worst to best
from sklearn.preprocessing import OrdinalEncoder
job_positions = [
    "no idea, there are no ranges in the firm ",
    "No idea",
    "No level ",
    "No level",
    "student",
    "Student",
    "Entry level",
    "intern",
    "Intern",
    "Working Student",
    "Entry Level",
    "Junior",
    "Middle",
    "Senior",
    "Lead",
    "Manager",
    "Work Center Manager",
    "Key",
    "Principal",
    "Head",
    "Director",
    "VP",
    "CTO",
    "C-Level",
    "C-Level executive manager",
    "C-level executive manager",
    "CEO",
    "President",
    "Self employed"
]
# encode lever column with ordinal encoding scheme
ordinal_encoder = OrdinalEncoder(categories=[job_positions])
df_3year['level_encoded'] = ordinal_encoder.fit_transform(df_3year[['level']])
df_3year = df_3year.drop(['level'], axis=1, inplace=False)

# encode these column with one hot encoding scheme
one_hot_encode_df = pd.get_dummies(df_3year, columns=['Gender', \
                                                      'City',\
                                                      'Position', \
                                                      'Main language at work', \
                                                      'Company type', \
                                                      'main tech'\
                                                      ])

# split train, test set
from sklearn.model_selection import train_test_split

X = one_hot_encode_df[[i for i in one_hot_encode_df.columns if i != 'salary']]
y = one_hot_encode_df['salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

'''
SVMs are sensitive to the scales of the input features.
Features with larger magnitudes can dominate the calculation of the distance between data points,
which affects the performance and the decision boundary of the model.
Scaling ensures that all features contribute equally to the model.
'''
# scale features
scaler = StandardScaler()
'''
If use fit_transform on both training and test data, the test data would influence the scaling parameters.
This leads to data leakage, where information from the test set contaminates the training process,
resulting in overly optimistic performance estimates.
'''
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# train
svm_ = SVR(kernel='poly', degree=3)
svm_.fit(X_train_scaled, y_train)

from sklearn.metrics import mean_squared_error, r2_score

# make predict
y_pred_test = svm_.predict(X_test_scaled)

test_mse = mean_squared_error(y_test, y_pred_test)
test_r2 = r2_score(y_test, y_pred_test)

# evaluation
print(f'test_mse {test_mse}')
print(f'test_r2 {test_r2}')

# Plotting
from matplotlib import pyplot as plt

x_age = X_test['Years of experience'].tolist()

plt.scatter(x_age, [round(i) for i in y_test.tolist()] , color='red', label='Truth salary')
plt.plot(x_age, [round(i) for i in y_pred_test.tolist()], color='blue', label='Predict salary')

plt.xlabel('sample index (Year of experience)')
plt.ylabel('salary')
plt.title('It Salary prediction')
plt.autoscale(axis='y')

plt.legend()
plt.show()
