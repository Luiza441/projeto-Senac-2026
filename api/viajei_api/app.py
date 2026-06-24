from http import HTTPStatus

from fastapi import FastAPI

from viajei_api.schemas.user import User

from viajei_api.schemas.User_public import UserPublic

app = FastAPI()



@app.post('/auth/',
           status_code=HTTPStatus.CREATED,
           response_model=User)
def create_user(user: User):
   user_with_id = userDB(**user.model_dump(),
                         id=len (database) + 1)
    