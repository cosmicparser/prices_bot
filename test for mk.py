from selenium import webdriver
import time
import tkinter as tk
import re




result = re.findall(r'\d\d\d\d/\d\d/\d\d', 'https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/')

print(result)

import re
result = re.findall(r'\d{2,4}', 'https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/')
print(result)

pricesdoc[A] = prices
pricesdoc.to_excel(r"C:\Users\User\Desktop\prices.xlsx", index=False)

volumesdoc[A] = volumes
pricesdoc.to_excel(r"C:\Users\User\Desktop\volumes.xlsx", index=False)

mcdoc[A] = Fvolumes
mcdoc.to_excel(r"C:\Users\User\Desktop\marketcap.xlsx", index=False)