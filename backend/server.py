from fastapi import FastAPI

from pds.endpoints import router


def app_maker():
    app = FastAPI()
    app.include_router(router)

    return app
