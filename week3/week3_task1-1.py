#task1-1
import urllib.request as request
import json
import csv
src1 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
src2 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
with request.urlopen(src1) as response1:
    data1= json.load(response1)
with request.urlopen(src2) as response2:
    data2= json.load(response2)

clist1=data1["list"]
clist2=data2["list"]

delete=["tel","fax","the total number of rooms"]

for english in clist2:
     for d in delete:
          if d in english:
               english.pop(d)


for c in clist1:
     for l in clist2:
          if c["_id"]==l["_id"]:
               c.update(l)

for a in clist1:
    if "區" in a["地址"]:
        b = a["地址"].find("區")
        a["地址"] = a["地址"][b + 1:]
    
    if "road" in a["address"].lower():
        e = a["address"].lower().find("road")
        a["address"]=a["address"][:e+4]
    elif "rd" in a["address"].lower():
        f = a["address"].lower().find("rd")
        a["address"]=a["address"][:f+3]
    elif "st" in a["address"].lower():
        g = a["address"].lower().find("st")
        a["address"]=a["address"][:g+3]


with open("hotels.csv","w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for company in clist1:
            writer.writerow([company["旅宿名稱"],company["hotel name"],company["地址"],company["address"],company["電話或手機號碼"],company["房間數"]])

with open("hotels.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for r in reader:
        print(", ".join(r))




