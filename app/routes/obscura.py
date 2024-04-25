from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import random
from app.utility import control_buttons_html

router = APIRouter(prefix="/obscura")
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def obscura_handler(request: Request):

    img = "/static/images/" + random.choice(os.listdir("static/images/"))

    return templates.TemplateResponse(
        request=request, 
        name="generator.html", 
        context={"title": "Obscura", "img": img, "control": control_buttons_html("/obscura/", img)},
    )