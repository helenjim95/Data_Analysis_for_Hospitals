import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)
general = pd.read_csv("general.csv")
prenatal = pd.read_csv("prenatal.csv")
sports = pd.read_csv("sports.csv")

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

df = pd.concat([general, prenatal, sports], ignore_index=True)
df.drop(columns=["Unnamed: 0"], inplace=True)

# # 6. Delete all the empty rows
df.dropna(axis=0, how='all', inplace=True)

# Correct all the gender column values to f and m respectively
df.loc[df.gender == 'male', 'gender'] = 'm'
df.loc[df.gender == 'man', 'gender'] = 'm'
df.loc[df.gender == 'female', 'gender'] = 'f'
df.loc[df.gender == 'woman', 'gender'] = 'f'
# print(df.describe(include='all'))

# Replace the NaN values in the gender column of the prenatal hospital with f
df.loc[df.hospital == 'prenatal', 'gender'] = 'f'

# Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound,
# mri, xray, children, months columns with zeros
df.fillna(0, inplace=True)

# print(df.shape)
# print(df.sample(n=20, random_state=30))

# 1. Which hospital has the highest number of patients?
# print(f'The answer to the 1st question is {df["hospital"].value_counts().idxmax()}')
# # 2. share of the patients in the general hospital suffers from stomach-related issues
# general_diagnosis_sum = df[df.hospital == "general"].diagnosis.value_counts().sum()
# general_diagnosis_stomach = df[df.hospital == "general"].diagnosis.value_counts().loc['stomach']
# share_stomach = (general_diagnosis_stomach / general_diagnosis_sum).round(3)
# print(f"The answer to the 2nd question is {share_stomach}")

# 3. share of the patients in the sports hospital suffers from dislocation-related issues
# sports_diagnosis_sum = df[df.hospital == "sports"].diagnosis.value_counts().sum()
# sports_diagnosis_dislocation = df[df.hospital == "sports"].diagnosis.value_counts().loc['dislocation']
# share_dislocation = (sports_diagnosis_dislocation / sports_diagnosis_sum).round(3)
# print(f"The answer to the 2nd question is {share_dislocation}")

# 4. difference in the median ages of the patients in the general and sports hospitals
# median_age = df.pivot_table(index="hospital", values="age", aggfunc="median")
# median_age_general = median_age.loc['general']
# median_age_sports = median_age.loc["sports"]
# median_age_difference = (median_age_general - median_age_sports)[0]
# print(f"The answer to the 4th question is {median_age_difference}")

# 5. In which hospital the blood test was taken the most often?
# How many blood tests were taken?
# max_blood_test_hospital = df.loc[df.blood_test == "t", 'hospital'].value_counts().idxmax()
# max_blood_test = df.loc[df.blood_test == "t", 'hospital'].value_counts().max()
# print(f"The answer to the 5th question is {max_blood_test_hospital}, {max_blood_test} blood tests")

# Stage 5/5: Visualize it
# 1. The most common age of a patient among all hospitals?
#   Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80
bin = [0, 15, 35, 55, 70, 80]
df["age"].value_counts().plot(kind='hist', bins=bin)
plt.show()
range_ = "15-35"
# 2. The most common diagnosis among patients in all hospitals. Create a pie chart
df["diagnosis"].value_counts().plot(kind='pie')
plt.show()
common_diagnosis = "pregnancy"

# 3. Build a violin plot of height distribution by hospitals:
#   Main reason for the gap in values
#   Why there are two peaks, which correspond to the relatively small and big values?
df.loc[(df["hospital"] == "sports"), 'height'] = df['height'] * 2.54 / 10
# sns.violinplot(x=df['hospital'], y=df['height'])
fig, ax = plt.subplots()
ax.violinplot(df.height)
plt.show()

reason = "it's because the large values"
print(f"The answer to the 1st question: {range_}")
print(f"The answer to the 2nd question: {common_diagnosis}")
print(f"The answer to the 3rd question: {reason}")
