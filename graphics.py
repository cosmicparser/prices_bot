import pandas
import requests, json, pandas, xlsxwriter
import tabulate
import time, matplotlib.pyplot as plt
import numpy as np


df = pandas.read_excel(r'C:\Users\User\PycharmProjects\objectoriented1\output.xlsx', sheet_name="Sheet1")
#df = df.drop(columns=['Unnamed: 0'])

print(df)

df2 = pandas.read_excel(r'C:\Users\User\Desktop\trial_messaround.xlsx', sheet_name="Sheet1")
a=[]
n = df2.shape
for i in range(n[0]):
    a.append(df2.iloc[i]['tags'])

print(a)

for i in a:
    plt.plot(df["tags"], df[i])
    plt.title(i)
    plt.show()




#df2 = df2.T
#df2.to_excel(r"C:\Users\User\Desktop\prices.xlsx")