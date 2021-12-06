from pydantic import BaseModel


class Company(BaseModel):
    company_name: str

