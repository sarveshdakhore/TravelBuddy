import uvicorn
from fastapi import Request
from fastapi import FastAPI, Request
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.route("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/lol")
async def read_root(request: Request):
    json_data = await request.json()
    stat = json_data["status"]
    if stat == "1":
        return {"Akarsh bhadwa hai"}
    return {"Akarsh bhadwa nahi hai"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

