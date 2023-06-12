import schema
from database import SessionLocal, engine
import model
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse


model.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependency
def get_database_session():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/properties", response_class=HTMLResponse)
async def fetch_properties(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(model.Property).all()
    return templates.TemplateResponse("index.html", {"request": request, "properties": records})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)