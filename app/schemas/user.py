from pydantic import BaseModel, Field

class UsersSchema(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=7, max_length=25)

class FindUsersSchema(BaseModel):
    username: str = Field(min_length=3, max_length=20)