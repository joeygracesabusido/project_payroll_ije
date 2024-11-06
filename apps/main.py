from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

from apps.routes.admin import api
from apps.routes.login import login_router


from fastapi.staticfiles import StaticFiles

from apps.routes.graphql import graphql_app
app = FastAPI()
app.mount("/static", StaticFiles(directory="apps/static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)



app.include_router(api, tags=["admin"])
app.include_router(login_router, tags=['Login'])




# Mount Strawberry's GraphQL app onto FastAPI
app.mount("/graphql", graphql_app)


