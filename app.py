from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from requests import post, get
from validators import url as url_validation

# define the app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data to show when the user visits the homepage
@app.get("/")
def read_root():
    return {
        "message": "Hi, this is a simple API used to verify the status of a hcaptcha verification token"
    }


@app.get("/ping-back")
def ping_back(
    remote_url: str = None,
    method: str = "get",
):
    if remote_url is None:
        return HTTPException(status_code=400, detail="No remote url provided")
    elif remote_url == "":
        return HTTPException(status_code=400, detail="Please provide a valid URL")
    if not url_validation(remote_url):
        return HTTPException(status_code=400, detail="Invalid remote url")

    r = None
    method = method.lower()

    if method == "get":
        r = get(remote_url)
    elif method == "post":
        r = post(remote_url)
    else:
        return HTTPException(status_code=400, detail="Invalid method provided")

    return {
        "success": r.status_code == 200,
        "url": remote_url,
        "status_code": r.status_code,
    }
