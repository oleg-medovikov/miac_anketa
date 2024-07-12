from fastapi.responses import HTMLResponse
from .app import app


@app.get("/")
def get_main_page():
    # Читаем HTML-файл
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/login")
def get_login_page():
    # Читаем HTML-файл
    with open("static/login.html", "r") as f:
        html_content = f.read()

    return HTMLResponse(content=html_content, status_code=200)
