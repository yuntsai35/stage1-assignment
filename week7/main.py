import os
from dotenv import load_dotenv
load_dotenv()

import mysql.connector
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password=os.getenv("DB_PASSWORD"),
  database="website"
)
print("database ready")

from fastapi import FastAPI,Body
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()

app.mount("/static", StaticFiles (directory="static"),  name="static")


app.add_middleware(SessionMiddleware, secret_key="middleware_key")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_index(request: Request):
    return templates.TemplateResponse("week7.html",{"request":request})

@app.post("/signup")
def signup(body: dict = Body(...)):
    name=body["name"]
    email=body["email"].lower()
    password=body["password"]

    cursor=con.cursor()
    cursor.execute("SELECT * FROM member WHERE email=%s",[email])
    result=cursor.fetchone()

    if result==None:
        cursor.execute("INSERT INTO member (name,email,password) VALUES (%s,%s,%s)",[name,email,password])
        con.commit()
        return RedirectResponse(url="/", status_code=302)
    else:
        msg = "重複的電子郵件"
        return RedirectResponse(url=f"/ohoh?msg={msg}", status_code=302)

@app.post("/login")
async def login(request:Request,body: dict = Body(...)):
    
    email=body["email"]
    password=body["password"]

    cursor=con.cursor()
    cursor.execute("SELECT * FROM member WHERE email=%s AND password=%s",[email,password])
    result=cursor.fetchone()
    if result==None:
        request.session["member"]=None
        request.session["login_status"] = {"ok": False}

        msg = "電⼦郵件或密碼錯誤"
        return RedirectResponse(url=f"/ohoh?msg={msg}", status_code=302)
    else:
        request.session["member"]={"id":result[0],"name":result[1],"email":result[2]}
        request.session["login_status"] = {"ok": True} 

        return RedirectResponse(url="/member", status_code=302)

    
@app.get("/member")
async def get_new_page(request: Request):
    if "member" in request.session and request.session["member"] !=None:
        member=request.session["member"]

        content={"request":request, "statement_content":member["name"],"current_id":member["id"]}
        return templates.TemplateResponse("message.html", content)
    else:
        return RedirectResponse(url="/", status_code=302)
    

@app.get("/ohoh")
async def get_new_page(request: Request, msg:str):
    content={"request":request,"header_text":"失敗頁面", "statement_content":msg,"success": False}
    return templates.TemplateResponse("statement.html", content)

@app.get("/logout")
async def logout_member(request:Request):
    if "member" in request.session:
        del request.session["member"]
    if "login_status" in request.session:
        del request.session["login_status"]
    return RedirectResponse(url="/", status_code=302)


@app.get("/api/member/{member_id}")
async def getDetail(request: Request,member_id: int):
    member=request.session["member"]
    id=member["id"]
    cursor=con.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email FROM member WHERE id = %s",[member_id])
    result=cursor.fetchone()
    if result:
        member_data = {
            "id": result['id'],
            "name": result['name'],
            "email": result['email']
        }
        cursor.execute("INSERT INTO records (searched_member_id, searcher_id) VALUES (%s,%s)",[member_id, id])
        con.commit()
        return {"data": member_data}
    else:
        return {"data": None}
    
@app.patch("/api/member")
async def updateName(request: Request, body: dict = Body(...)):
    if "member" in request.session:
        member=request.session["member"]
        new_name = body.get("name")
        member_id=member["id"]

        cursor=con.cursor()
        cursor.execute("UPDATE member SET name = %s WHERE id = %s", [new_name, member_id])
        con.commit()
        request.session["member"]["name"] = new_name
        return {"ok": True}
    else:
        return {"error": True}
    
@app.get("/api/records")
async def getFullrecords(request: Request):
    member=request.session["member"]
    id=member["id"]
    cursor=con.cursor(dictionary=True)
    cursor.execute("SELECT member.name, records.time FROM records INNER JOIN member ON records.searcher_id= member.id WHERE records.searched_member_id = %s ORDER BY records.time DESC LIMIT 10",[id])
    result=cursor.fetchall()
    if result:
        return {"data": result}
    else:
        return {"data": None}


    
    
    

