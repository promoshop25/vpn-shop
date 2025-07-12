from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/buy")
async def buy_code():
    with open("codes.txt", "r+") as f:
        codes = f.readlines()
        if not codes:
            return {"error": "Нет кодов"}
        code = codes[0].strip()
        f.seek(0)
        f.writelines(codes[1:])
        f.truncate()
    return {"code": code}
