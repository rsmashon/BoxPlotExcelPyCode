import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel('testexcel.xlsx', sheet_name='Sheet3')
# print(df)

# Access the values of the DataFrame
my_values = df.values
# print(values)

di ={}

for i in my_values:
    if i[1] not in di:
        di[i[1]]=[i[0]] #give i[0] value to key i[1]
    else :
        di[i[1]].append(i[0])

print(di)

li =[]
z =[]

for i,p in di.items():
    li.append(f'Grade{i}')
    z.append(p)
   
print(li)
print(z)
ax = plt.subplot()
ax.boxplot(z , labels=li, showmeans= True , )
ax.grid()
ax.set_ylabel('WBC Count(/μl)')

# plt.savefig('Grasheet3.jpg')


plt.show()
