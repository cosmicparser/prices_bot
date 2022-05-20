import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import requests, json, pandas, xlsxwriter,time
from datetime import datetime


lsv = []
ysv = []
xsv = []
dfv = pandas.read_excel(r"C:\Users\User\Desktop\volumes.xlsx")
dfv = dfv.T
for col in dfv.columns:
    col_lsv = dfv[col].tolist()
    lsv.append(col_lsv)
print(lsv)
for i in lsv:
    for name in i:
        if name == value:
            ysv = i
for i in dfv.index:
    xsv.append(i)
xsv.pop(0)
cryptonameforgraph = ysv[0]
ysv.pop(0)
