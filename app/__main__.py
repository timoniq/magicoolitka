from app.routes import index, library, obscura
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import run

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

routes = [
    index.router,
    library.router,
    obscura.router,
]

for route in routes:
    app.include_router(route)

run(app)
