import urllib.request as req
import bs4
import csv
import re

def getTime(timeurl):
    request=req.Request(timeurl,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    post_time = None
   
    time_pattern = re.compile(r'\s*時間\s*')
    find_section = root.find("span", string=time_pattern)
    
    if find_section:
        time_value = find_section.find_next_sibling("span") 
        if time_value:
            post_time = time_value.string.strip()
            return post_time

all_data=[]
def getData(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    whole_record=[]
    articles=root.find_all("div",class_="r-ent")
    for article in articles:
        likes=article.find("div",class_="nrec")
        likecontent=None
        if likes.span !=None:
            likecontent=likes.span.string
        titles=article.find("div",class_="title")
        if titles.a !=None:
            titlecontent=titles.a.string
        if titles.a !=None:
            titlecontent=titles.a.string.strip()
            article_link = titles.a["href"]
        if article_link != None:
            full_url = "http://www.ptt.cc/"+ article_link
            time = getTime(full_url)
        record={'Title': titlecontent,'like':likecontent,'link':article_link,'Time':time}
        whole_record.append(record)
        all_data.append(record)

    nextLink=root.find("a",string="‹ 上頁")
    
    return nextLink["href"]
   

pageURL="https://www.ptt.cc/bbs/Steam/index.html"
count=0
while count<3:
    pageURL="http://www.ptt.cc/"+getData(pageURL)
    count+=1
if all_data:
    fieldnames = ['Title', 'Likes', 'Link', 'Time']
    with open("articles.csv","w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for record in all_data:
                writer.writerow([record["Title"],record["like"],record["Time"]])
with open("articles.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for r in reader:
        print(", ".join(r))
   