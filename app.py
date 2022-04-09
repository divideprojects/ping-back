from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from requests import post, get
from validators import url as url_validation
from fastapi.staticfiles import StaticFiles

# define the app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define the '/alive' endpoint
@app.get("/alive")
async def alive():
    return {"status": "alive"}


# define the '/pingback' endpoint which does main work
@app.get("/pingback")
async def ping_back(
    link: str = None,
    method: str = "get",
):
    if link is None:
        return HTTPException(status_code=400, detail="No remote url provided")
    elif link == "":
        return HTTPException(status_code=400, detail="Please provide a valid URL")
    if not url_validation(link):
        return HTTPException(status_code=400, detail="Invalid remote url")

    r = None
    method = method.lower()  # lowercase the method

    if method == "get":
        r = get(link)
    elif method == "post":
        r = post(link)
    else:
        return HTTPException(status_code=400, detail="Invalid method provided")

    return {
        "success": r.status_code == 200,
        "url": link,
        "status_code": r.status_code,
    }


# Data to show when the user visits the homepage
app.mount("/", StaticFiles(directory="static", html=True), name="static")
