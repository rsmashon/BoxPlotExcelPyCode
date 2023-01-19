# Import libraries
import matplotlib.pyplot as plt
import pandas

excel_df = pandas.read_excel('testexcel.xlsx', sheet_name='Sheet3')
print(excel_df)

x = {k:g['WBC'].tolist() for k,g in excel_df.groupby('Grading')}
print(x)

# excel_data_df.set_index('Grade').T.to_dict('list')
# excel_df.groupby(level=0).apply(lambda x: x.to_dict('r')).to_dict()

z =[]
li =[]

for i,p in x.items():
    li.append(f'Grade{i}')
    z.append(p)
    
ax = plt.subplot()
ax.boxplot(z , labels=li, showmeans= True )
ax.grid()
ax.set_ylabel('WBC Count(/μl)')

# plt.show()
 
# plt.boxplot(data)
 


plt.savefig('Grasheet3.jpg')
