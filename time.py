import requests, json, pandas, xlsxwriter,time
from datetime import datetime
from openpyxl import load_workbook


text = requests.get("https://crypto.com/fe-ex-api/market-data/v2/public/get-ticker").text
data = json.loads(text)
data.pop("code")
data.pop("method")
for i in data["result"]["data"]:
    i.pop("k")
    i.pop("a")
    i.pop("t")
    i.pop("l")
    i.pop("c")
    i.pop("h")
# находим время
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

print("Current parse time: ", current_time)

data_sorted = {}
for i in range(len(data["result"]["data"])):
    data["result"]["data"][i]['Final Volume'] = data["result"]["data"][i]["b"] * data["result"]["data"][i]["v"]
print(data["result"]["data"])

data_prices = {}
for item in data["result"]["data"]:
    name = item["i"]
    data_prices[name] = item["b"]

data_volume = {}
for item in data["result"]["data"]:
    name = item["i"]
    data_volume[name] = item["v"]

data_Fvolume = {}
for item in data["result"]["data"]:
    name = item["i"]
    data_Fvolume[name] = item["Final Volume"]

sorted_tupleP = sorted(data_prices.items(), key=lambda x: x[0])

sorted_tupleV = sorted(data_volume.items(), key=lambda x: x[0])

sorted_tupleFV = sorted(data_Fvolume.items(), key=lambda x: x[0])

prices_sorted = dict(sorted_tupleP)
keys_sorted = dict(sorted_tupleV)
FV_sorted = dict(sorted_tupleFV)

tags = []
prices = []
volumes = []
Fvolumes = []

for key in prices_sorted:
    #print(key, prices_sorted[key], keys_sorted[key], FV_sorted[key])
    tags.append(key)

df = pandas.DataFrame(tags)

df.to_excel(r"C:\Users\User\Desktop\prices.xlsx", index = False)


