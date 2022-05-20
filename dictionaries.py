

import requests, json, pandas, xlsxwriter
import tabulate


text = requests.get("https://crypto.com/fe-ex-api/market-data/v2/public/get-ticker").text
data = json.loads(text)
data.pop("code")
data.pop("method")
for i in data["result"]["data"]:
    i.pop("k")
    i.pop("a")
    i.pop("t")
    i.pop("v")
    i.pop("l")
    i.pop("c")
    i.pop("h")

text2 = requests.get("https://crypto.com/fe-ex-api/market-data/v2/public/get-ticker").text
data2 = json.loads(text)
data2.pop("code")
data2.pop("method")
for i in data2["result"]["data"]:
    i.pop("k")
    i.pop("a")
    i.pop("t")
    i.pop("v")
    i.pop("l")
    i.pop("c")
    i.pop("h")

num = 0

for i in data["result"]["data"]:
    if (i in data2["result"]["data"]) and (data["result"]["data"] == data2["result"]["data"]):
        num+=1
print(num)




tags = []
prices = []

for i in data["result"]["data"]:
    tags.append(i["i"])
    prices.append(i["b"])





'''
data_sorted = {}
for item in data["result"]["data"]:
   name = item["i"]
   data_sorted[name] = item

for i in data_sorted:
    data_sorted[i].pop("i")

print(data_sorted)
'''



list1 = list(zip(tags, prices))
df = pandas.DataFrame(list(zip(tags, prices)), columns = ["tags", "prices"])
print(df)



df.to_excel("output.xlsx")


'''
over2_natselo = lambda x : x//2

print(over2_natselo(3))


'''