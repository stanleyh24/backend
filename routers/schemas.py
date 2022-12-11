from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from typing import List

class CategoryBase(BaseModel):
    name : str
        
    class Config():
        orm_mode= True

class CategoryDisplay(BaseModel):
    id: int
    name : str
    created_At: datetime
    updated_At: datetime | None

    class Config():
        orm_mode= True