from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId


class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str


class CreateSessionSchema(BaseModel):
    email: EmailStr
    password: str
