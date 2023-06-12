from pydantic import BaseModel

class Property(BaseModel):
    id = int
    name = str
    address = str
    type = str
    rent = int

    class Config:
        orm_mode = True