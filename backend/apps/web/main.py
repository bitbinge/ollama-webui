from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from apps.web.routers import auths, users, chats, modelfiles, utils
from config import WEBUI_VERSION, WEBUI_AUTH

app = FastAPI()

origins = ["*"]

app.state.ENABLE_SIGNUP = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auths.router, prefix="/auths", tags=["auths"])

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(chats.router, prefix="/chats", tags=["chats"])
app.include_router(modelfiles.router, prefix="/modelfiles", tags=["modelfiles"])
app.include_router(utils.router, prefix="/utils", tags=["utils"])


@app.get("/")
async def get_status():
    return {"status": True, "version": WEBUI_VERSION, "auth": WEBUI_AUTH}
