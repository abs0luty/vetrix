import datetime
from fastapi import APIRouter, status, HTTPException
from bcrypt import hashpw, gensalt

from app.settings import settings
from app.database import User

from . import schema

router = APIRouter()

@router.post('/v1/users', status_code=status.HTTP_201_CREATED)
async def create_user(payload: schema.CreateUserSchema):
    user = User.find_one({'email': payload.email.lower()})
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Account already exists')

    now = datetime.datetime.now(datetime.UTC)

    User.insert_one({
        "role": 'user',
        "password": str(hashpw(payload.password.encode('utf-8'), gensalt(14))),
        "email": payload.email.lower(),
        "created_at": now,
        "is_verified": True,
    })

    return {'status': 'success', 
            'message': 'User successfully created.'}
