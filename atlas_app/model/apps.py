from typing import List

from pydantic import BaseModel


class Company(BaseModel):
    companies: List

