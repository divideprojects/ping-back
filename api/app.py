from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from requests import get, post
from pydantic import validator
from typing import Optional

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


class PingBackRequest:
    method: str = "get"
    link: Optional[str] = None

    @validator("link")
    def validate_link(cls, v):
        if not v:
            raise ValueError("Please provide a valid URL")
        if not url_validation(v):
            raise ValueError(
                "Invalid remote URL, make sure your URL contains scheme such 'http://' or 'https://'"
            )
        return v


# define the '/pingback' endpoint which does main work
@app.get("/pingback")
async def ping_back(request: PingBackRequest):
    try:
        if request.method.lower() == "get":
            r = get(request.link)
        elif request.method.lower() == "post":
            r = post(request.link)
        else:
            raise HTTPException(status_code=400, detail="Invalid method provided")
        r.raise_for_status()
        return {
            "success": r.ok,
            "url": request.link,
            "status_code": r.status_code,
        }
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
