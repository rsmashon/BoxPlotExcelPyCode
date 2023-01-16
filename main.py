# Import libraries
import matplotlib.pyplot as plt
import pandas

excel_df = pandas.read_excel('testexcel.xlsx', sheet_name='Sheet2')
print(excel_df)

x = {k:g['HGB'].tolist() for k,g in excel_df.groupby('Grade')}
print(x)

# excel_data_df.set_index('Grade').T.to_dict('list')
# excel_df.groupby(level=0).apply(lambda x: x.to_dict('r')).to_dict()

z =[]
li =[]

for i,p in x.items():
    li.append(i)
    z.append(p)
    
    
plt.boxplot(z , labels=li, showmeans= True)
# plt.show()
 
# plt.boxplot(data)
 


plt.savefig('Gra.pngP')
