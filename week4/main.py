from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import urllib.request as request
import json

src1 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
src2 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
with request.urlopen(src1) as response1:
    data1= json.load(response1)
with request.urlopen(src2) as response2:
    data2= json.load(response2)

clist1=data1["list"]
clist2=data2["list"]

for c in clist1:
    for l in clist2:
        if c["_id"]==l["_id"]:
            c.update(l)


app=FastAPI()

app.mount("/static", StaticFiles (directory="static"),  name="static")

app.add_middleware(SessionMiddleware, secret_key="middleware_key")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_index(request: Request):
    return templates.TemplateResponse("week4.html",{"request":request})


@app.post("/login")
async def login(request:Request,username:str=Form(...), password:str=Form(...), checkbox: bool = Form(False)):
    
    if username=="abc@abc.com" and password=="abc" and checkbox== True:
        request.session["logged_in"]=True
        return RedirectResponse(url="/member", status_code=302)
    elif checkbox== False:
        return RedirectResponse(url="/", status_code=302)
    elif username=="" or password=="":
        msg = "請輸入信箱和密碼"
        return RedirectResponse(url=f"/ohoh?msg={msg}", status_code=302)
    else:
        msg = "信箱或密碼輸入錯誤"
        return RedirectResponse(url=f"/ohoh?msg={msg}", status_code=302)
    
@app.get("/member")
async def get_new_page(request: Request):
    if 'logged_in' not in request.session:
        return RedirectResponse(url="/", status_code=302)
    
    content={"request":request,"header_text":"歡迎光臨，這是會員頁", "statement_content":"恭喜您，成功登入系統","success": True}
    return templates.TemplateResponse("statement.html", content)

@app.get("/ohoh")
async def get_new_page(request: Request, msg:str):
    content={"request":request,"header_text":"失敗頁面", "statement_content":msg,"success": False}
    return templates.TemplateResponse("statement.html", content)

@app.get("/logout")
async def logout_member(request:Request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
    return RedirectResponse(url="/", status_code=302)


@app.get("/hotel/{item_id}")
async def read_item(request: Request,item_id: int):

        info=None

        for company in clist1:
            if item_id==company["_id"]:
                info = company 
        
        if info !=None:
            information= f"{info['旅宿名稱']}、{info['hotel name']}、{info['電話或手機號碼']}"
            content={"request": request,"header_text": "旅館的資訊","statement_content":information ,"found": True}
        else:
            content={"request": request,"header_text": "旅館的資訊","statement_content": "查不到相關的資料","found": True}
        return templates.TemplateResponse("statement.html", content)
    
    
    

