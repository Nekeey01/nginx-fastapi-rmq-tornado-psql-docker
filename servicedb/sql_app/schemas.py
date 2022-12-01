from pydantic import BaseModel

class ProblemBase(BaseModel):
    Name: str
    Surname: str
    Midname: str
    Phone: int
    Problem: str


class ProblemCreate(ProblemBase):
    pass


class Problem(ProblemBase):
    id: int

    class Config:
        orm_mode = True