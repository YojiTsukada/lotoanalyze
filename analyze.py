import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Read CSV
csv_data  = pd.read_csv('./csv/loto6.csv',encoding='cp932')

# Change Colmuns
csv_data.columns = ['no', 'date', '1','2','3','4','5','6','bounus','Hit1','Hit2','Hit3','Hit4','Hit5','1st Prize','2nd prize','3rd prize','4th prize','5th prize','carry over']

# Extract 1-6 Count
listdata = csv_data.loc[:,['1','2','3','4','5','6']]

listdata

# merged columns
count = pd.melt(listdata)

# To set colmns name
count.columns = ["position","all_no"]

# show data count (and sort)
group = count.groupby('all_no').count().sort_values('position', ascending=False)


group

#df = pd.DataFrame({'val': np.random.rand(300)})
#graph = group.plot(kind='bar', align='center')
