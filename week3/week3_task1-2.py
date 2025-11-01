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


#task1-2
districts=[]
for company in clist1:
    if "區" in company["地址"]:
        h = company["地址"].find("區")
        district_name = company["地址"][h-2:h+1]
        districts.append([district_name,1 ,int(company["房間數"])])

count_amount=[]

for district in districts: 
    for place in count_amount:
        if place[0] == district[0]:
            place[1] += district[1]
            place[2] += district[2]
            break
    else:
        count_amount.append(list(district)) 

with open("districts.csv","w", encoding="utf-8") as csvfile2:
    writer = csv.writer(csvfile2)
    for company in count_amount:
            writer.writerow(company)

with open("districts.csv", mode="r", encoding="utf-8") as file2:
    reader = csv.reader(file2)
    for r in reader:
        print(", ".join(r))





            
 