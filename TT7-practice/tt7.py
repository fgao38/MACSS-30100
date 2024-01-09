import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

morg = pd.read_csv("morg_d07_strings.csv", index_col="h_id")

# TASKS 2-6

#2 
age = morg["age"]
age

#3
h_id = morg.loc["1_2_2"]
h_id

#4 
h_id_4 = morg.iloc[:4]
h_id_4

#5

dic = {}
for i in morg.columns:
    if any(morg[i].isna()):
        dic[i] = 0.0
dic

#6

morg.fillna(value = dic, inplace=True)
morg

#7

categ = ["gender", "race", "ethnicity", "employment_status"]

for i in categ:
    if i in morg.columns:
        morg[i] = morg[i].astype("category")

# For each of the tasks, print the value requested in the task.

## YOUR CODE HERE ##


### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

## YOUR CODE HERE ##

# Example use of cut()
boundaries = range(16, 89, 8)
morg.loc[:, "age_bin"] = pd.cut(morg.loc[:, "age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

### Task 8

boundaries = range(0, 99, 10)
morg.loc[:, "hwpw_bin"] = pd.cut(morg.loc[:, "hours_worked_per_week"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

print(morg)
print(morg.dtypes)



### Tasks 9-13

#9

filter_morg = (morg["hours_worked_per_week"] >= 35)
ft = morg[filter_morg]
ft

#10

not_working_filter = (morg["employment_status"] == "Working")
not_working = morg[not_working_filter]
not_working_filter

#11

filter_earning = ((morg["hours_worked_per_week"] >= 35) |
               (morg["earnings_per_week"] > 1000))
ft_1k = morg[filter_earning]
ft_1k

#12

counts = morg.loc[:, "employment_status"].value_counts()[:5]
counts

#13

groupby = morg.groupby("employment_status").size()
groupby 

### Task 14

students = pd.read_csv("students.csv")
extended_grades = pd.read_csv("extended_grades.csv")

merge_df = pd.merge(students, extended_grades, on="UCID", how="inner")
merge_df
grouped = df.groupby(["Grade", "Major"]).size().reset_index()
grouped
grouped.rename(columns={0:"Count"}, inplace=True)
grouped
