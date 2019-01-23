import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Read Result CSV
res_csv  = pd.read_csv('./csv/loto6.csv',encoding='cp932')

# Change Colmuns
res_csv.columns = ['no', 'date', '1','2','3','4','5','6','bounus','Hit1','Hit2','Hit3','Hit4','Hit5','1st Prize','2nd prize','3rd prize','4th prize','5th prize','carry over']

# Extract 1-6 Count
listdata = res_csv.loc[:,['no','1','2','3','4','5','6']]

# To change list
array = listdata.values


# check repeat Number
repeat = []
for x in array:
    for y in array:
        if (x[0] == y[0]):
            break
        if (x[1:] == y[1:]).all():
            repeat.append(x[1:])
            print(repeat)


# Read My Number
my_number = pd.read_csv('./csv/my_number.csv')
my_number_array = my_number.values

# Comparison
matched_list = []
for i in array:
    for n in my_number_array:
        if (i[:1] == n).all():
            matched_list.append(i)

# print result
print(matched_list)

# merged columns
count = pd.melt(listdata)

# To set colmns name
count.columns = ["position","all_no"]

# show data count (and sort)
group = count.groupby('all_no').count().sort_values('position', ascending=False)

# show
print(group)
