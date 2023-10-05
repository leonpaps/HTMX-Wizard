from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

# @app.get("/favicon.ico")
# def favicon():
#     return {"content": "Hello World!"}

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/step1")
def step1(request: Request):
    return templates.TemplateResponse("step1.html", {"request": request})

@app.post("/welcome")
def step1(request: Request, name: str = Form(...)):
    return templates.TemplateResponse("welcome.html", {"request": request, "name": name})
