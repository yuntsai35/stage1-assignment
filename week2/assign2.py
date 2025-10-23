#task1
def func1(name): 
    item = [
    {"point": "悟空",   "x1":0, "y1":0,   "distance": None},
    {"point": "丁滿",   "x1":-1, "y1":4,  "distance": None},
    {"point": "⾟巴",   "x1":-3, "y1":3,  "distance": None},
    {"point": "貝吉塔", "x1":-4, "y1":-1, "distance": None},
    {"point": "特南克斯","x1":1, "y1":-2, "distance": None},
    {"point": "弗利沙", "x1":4, "y1":-1,  "distance": None}] 
    
    for i in item:
        if name== i["point"]:
            x2=i["x1"]
            y2=i["y1"]

    for t in item:
        t["distance"] = abs(t["x1"] - x2) + abs(t["y1"] - y2)

    for e in item:
        if name in ("⾟巴","悟空","特南克斯","貝吉塔"):
            if e["point"] in ("丁滿","弗利沙"):
                e["distance"]+=2
        else:
            if e["point"] in ("⾟巴","悟空","特南克斯","貝吉塔"):
                e["distance"]+=2
    
    long=[]
    short=[]

    for m in item:
            if m["distance"] == max(x["distance"] for x in item if x["distance"] > 0):
                long.append(m["point"])
            if m["distance"] == min(x["distance"] for x in item if x["distance"] > 0):
                short.append(m["point"])

    
    print("最遠" + "、".join(long) + "；最近" + "、".join(short))


func1("⾟巴")  # print 最遠弗利沙；最近丁滿、⾙吉塔
 
func1("悟空")  # print 最遠丁滿、弗利沙；最近特南克斯
 
func1("弗利沙")  # print 最遠⾟巴，最近特南克斯
 
func1("特南克斯")  # print 最遠丁滿，最近悟空


#task2
reserve=[]
s1=[]
s2=[]
s3=[]

def func2(ss, start, end, criteria):      
    c=None
    r=None
    name=None

    if "c" in criteria:
        c = criteria[3:]
    elif "r" in criteria:
        r = criteria[3:]
    elif "name" in criteria:
        name = criteria[5:]
    

    diff_name=""
    if "name" in criteria and "=" in criteria:
        diff_name=criteria[5:]
        for s in ss:
            if diff_name == s["name"]:
             reserve.append(diff_name)
        time = list(range(start, end+1))
        if diff_name == "S1":
            for t in time:
                if t in s1:
                    print("Sorry")
                    return
            else:
                s1.extend(time)
                print("S1")
                return
        elif diff_name == "S2":
            for m in time:
                if m in s2:
                    print("Sorry")
                    return
            else:
                s2.extend(time)
                print("S2")
                return
        elif diff_name == "S3":
            for e in time:
                if e in s3:
                    print("Sorry")
                    return
            else:
                s3.extend(time)
                print("S3")
                return
        
    possible_list=[]
    if "c" in criteria and ">=" in criteria:
        for s in ss:
            if s["c"] >= int(c):
                possible_list.append((s["name"], abs(s["c"]-int(c))))
    elif "c" in criteria and "<=" in criteria: 
        for s in ss:
            if s["c"] <= int(c):
                possible_list.append((s["name"], abs(s["c"]-int(c))))

    if "r" in criteria and ">=" in criteria:
        for s in ss:
            if s["r"] >= float(r):
                possible_list.append((s["name"], abs(s["r"]-float(r))))     
    elif "r" in criteria and "<=" in criteria: 
        for s in ss:
            if s["r"] <= float(r):
                possible_list.append((s["name"], abs(s["r"]-float(r))))

    if not possible_list:
        print("Sorry")
        return


    time = list(range(start, end+1))

    while possible_list:
        
        min_index = 0
        for i in range(1, len(possible_list)):
            if possible_list[i][1] < possible_list[min_index][1]:
                min_index = i
        diff_name = possible_list[min_index][0]
        possible_list.remove(possible_list[min_index]) 

        if diff_name == "S1":
            for t in time:
                if t in s1:
                    break  
            else:
                s1.extend(time)
                print("S1")
                return

        elif diff_name == "S2":
            for t in time:
                if t in s2:
                    break
            else:
                s2.extend(time)
                print("S2")
                return

        elif diff_name == "S3":
            for t in time:
                if t in s3:
                    break
            else:
                s3.extend(time)
                print("S3")
                return

    print("Sorry")
    return
        

services=[ 
    {"name":"S1", "r":4.5, "c":1000}, 
    {"name":"S2", "r":3, "c":1200}, 
    {"name":"S3", "r":3.8, "c":800} 
]

func2(services, 15, 17, "c>=800")  # S3 
func2(services, 11, 13, "r<=4")  # S3 
func2(services, 10, 12, "name=S3")  # Sorry 
func2(services, 15, 18, "r>=4.5")  # S1 
func2(services, 16, 18, "r>=4")  # Sorry 
func2(services, 13, 17, "name=S1")  # Sorry 
func2(services, 8, 9, "c<=1500")  # S2

#task3
def func3(index): 
    q=index // 4
    r=index % 4
    p=[0,-2,-3,1]
    
    if r == 0:
        x=p[0]
    elif r==1:
        x=p[1]
    elif r==2:
        x=p[1]+p[2]
    else:
        x=p[1]+p[2]+p[3]
        
    value= 25 + q *(-2) + x
    print(value)

func3(1)  # print 23 
func3(5)  # print 21 
func3(10)  # print 16 
func3(30)  # print 6

#task4
def func4(sp, stat, n): 
    stat_list=[] 
    stat_list.extend(list(stat))
    
    list_index=[] 
    tag=0

    #https://blog.csdn.net/Jerry_1126/article/details/88924288
    for s in stat_list:
        if "0" == s:
            list_index.append(tag)
        tag +=1

    sp_list=[]
    for i in list_index:
        sp_list.append(sp[i])
    
    fit_number=[]
    diff=100
    for p in sp_list:
        if p >= n:
            num=abs(n-p)
            if num<=diff:
                diff=num
                fit_number=[p]
        elif p < n:
            num=abs(n-p)
            if num<=diff:
                diff=num
                fit_number=[p]
    
    fit_value= fit_number[0]
    a=sp.index(fit_value) 
    print(a)        

                
func4([3, 1, 5, 4, 3, 2], "101000", 2)  # print 5 
func4([1, 0, 5, 1, 3], "10100", 4)  # print 4 
func4([4, 6, 5, 8], "1000", 4)  # print 2 
