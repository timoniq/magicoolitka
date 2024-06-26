from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import random
from app.utility import control_buttons_html

router = APIRouter(prefix="/library")
templates = Jinja2Templates(directory="app/templates")

def get_title(identifier: str) -> str:
    return identifier.capitalize().replace("-", " ")

def random_poem() -> str:
    poems = os.listdir("poems")
    return random.choice(poems).removesuffix(".txt")
    

def get_poem(poem_identifier: str) -> tuple[str, str]:
    with open("poems" + os.sep + poem_identifier + ".txt") as fs:
        return get_title(poem_identifier), fs.read()


def process_content(content: str) -> str:
    return content


@router.get("/{poem}", response_class=HTMLResponse)
async def library_poem(request: Request, poem: str, control_buttons: bool = False):
    if not os.path.exists("poems" + os.sep + poem + ".txt"):
        return HTMLResponse(status_code=404)
    
    title, content = get_poem(poem)
    ctx = {"title": title, "content": content}

    if control_buttons:
        ctx["control"] = control_buttons_html("/library/", "/library/" + poem)

    return templates.TemplateResponse(
        request=request, 
        name="generator.html", 
        context=ctx,
    )

@router.get("/", response_class=HTMLResponse)
async def library_random_poem(request: Request):
    return await library_poem(request, random_poem(), control_buttons=True)
