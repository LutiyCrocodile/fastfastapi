from pydantic import BaseModel, Field
class UserAge(BaseModel):
    name: str = Field(max_length=15)
    age: int = Field(ge=0)

