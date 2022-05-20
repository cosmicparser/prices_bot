import requests, json, pandas
from datetime import datetime


def createxl():
    # counter = int(input("how many datapoints do you want to scrape and plot?"))
    counter = 30
    a = 0
    text = requests.get("https://crypto.com/fe-ex-api/market-data/v2/public/get-ticker").text
    data = json.loads(text)
    print(data)
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


    data_sorted = {}
    for i in range(len(data["result"]["data"])):
        data["result"]["data"][i]['Final Volume'] = data["result"]["data"][i]["b"] * data["result"]["data"][i]["v"]

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
        tags.append(key)

    df = pandas.DataFrame(tags)

    df.to_excel(r"C:\Users\User\Desktop\prices.xlsx", index=False)
    df.to_excel(r"C:\Users\User\Desktop\volumes.xlsx", index=False)
    df.to_excel(r"C:\Users\User\Desktop\marketcap.xlsx", index=False)


def getdata():
    #парсим
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current parse time b4: ", datetime.now())

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
    #находим время


    current_time = now.strftime("%H:%M:%S")

    print("Current parse time after: ", datetime.now())


    data_sorted = {}
    for i in range(len(data["result"]["data"])):
        data["result"]["data"][i]['Final Volume']=data["result"]["data"][i]["b"]*data["result"]["data"][i]["v"]




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


    prices_sorted=dict(sorted_tupleP)
    keys_sorted=dict(sorted_tupleV)
    FV_sorted = dict(sorted_tupleFV)

    tags = []
    prices = []
    volumes = []
    Fvolumes = []

    for key in prices_sorted:
       #print(key,prices_sorted[key],keys_sorted[key],FV_sorted[key])
       tags.append(key)

       prices.append(prices_sorted[key])
       volumes.append("{:.12f}".format(float(keys_sorted[key])))
       Fvolumes.append(FV_sorted[key])


    dfp = pandas.DataFrame(list(zip(tags, prices)), columns = ["tags", "prices"])
    dfv = pandas.DataFrame(list(zip(tags, volumes)), columns = ["tags", "Volumes"])
    dfcap = pandas.DataFrame(list(zip(tags, Fvolumes)), columns = ["tags", "Market Caps"])

    #print(dfp, dfv, dfcap)


    A=now.strftime("%H:%M:%S")
    dfp[A]=prices
    dfv[A]=volumes
    dfcap[A]=Fvolumes
    del dfp["prices"]



    pricesdoc = pandas.read_excel(r"C:\Users\User\Desktop\prices.xlsx", sheet_name="Sheet1")
    volumesdoc = pandas.read_excel(r"C:\Users\User\Desktop\volumes.xlsx", sheet_name="Sheet1")
    mcdoc = pandas.read_excel(r"C:\Users\User\Desktop\marketcap.xlsx", sheet_name="Sheet1")



    pricesdoc[A] = prices
    pricesdoc.to_excel(r"C:\Users\User\Desktop\prices.xlsx",index=False)


    volumesdoc[A] = volumes
    volumesdoc.to_excel(r"C:\Users\User\Desktop\volumes.xlsx",index=False)


    mcdoc[A] = Fvolumes
    mcdoc.to_excel(r"C:\Users\User\Desktop\marketcap.xlsx",index=False)


    dfp = pandas.read_excel(r"C:\Users\User\Desktop\prices.xlsx", engine='openpyxl')
    dfv = pandas.read_excel(r"C:\Users\User\Desktop\volumes.xlsx", engine='openpyxl')
    dfm = pandas.read_excel(r"C:\Users\User\Desktop\marketcap.xlsx", engine='openpyxl')

    current_time = now.strftime("%H:%M:%S")

    print("Current parse time after all: ", datetime.now())

    return dfp,dfv,dfm
    # ----------------------------------------------------------------------------------------



