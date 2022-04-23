from typing import Optional
from interface_adapters.controller.user_controller import UserController
from interface_adapters.presenter.user_presenter import UserPresenter
from enterprise_business_rules.entity.user import User
from fastapi import FastAPI, Form, Request
from mysql import connector
from fastapi.responses import JSONResponse
from werkzeug.exceptions import Conflict, NotFound
from http import HTTPStatus
from pydantic import BaseModel

from frameworks_and_drivers.db.user_repository import UserRepository

app = FastAPI()

# MySQL Connection
config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',
    'database': 'db',
    'autocommit': True
}

conn = connector.connect(**config)


@app.get("/")
def read_root():
    user = User(user_id=2, name='ABC',
                hashed_password='password', line_token='token')
    repository = UserRepository(conn)
    repository.save(user)
    user_db = repository.get(user_id=2)
    return JSONResponse(
        content={"Hello": user_db.name}
    )


class UserForPost(BaseModel):
    name: str
    password: str
    line_token: Optional[str] = None


@app.post("/users")
def post(user: UserForPost):
    return JSONResponse(
        content={"Hello": user.name}
    )


@app.exception_handler(NotFound)
async def handle_404(request: Request, exc: NotFound):
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={"message": exc.description},
    )


@app.exception_handler(Conflict)
async def handle_409(request: Request, exc: Conflict):
    return JSONResponse(
        status_code=HTTPStatus.CONFLICT,
        content={"message": exc.description},
    )
