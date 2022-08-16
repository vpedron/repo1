import datetime
#from beanie import Document
from pydantic import BaseModel
from typing import Optional
from beanie import Document, init_beanie
from datetime import timedelta, timezone

GMT = timedelta(hours=-3)
timezoneGMT = timezone(GMT)

date_time = datetime.datetime.now()
date = date_time.astimezone(timezoneGMT)

 
class Noticias(Document):
    title: str
    datetime: datetime
    link: str
    site: str 


class Settings:
    name = "db_noticias"
 
class Config:
    schema_extra = {
        "example": {
            "title": "Abdulazeez",
            "date": datetime.today(),
            "link": "TestDriven TDD Course",
            "site": "Excellent course!",
            
        }
    }
 
 
class UpdateNoticias(BaseModel):
    title: Optional[str]
    date: Optional[date]
    link: Optional[str]
    site: Optional[str]
 
class Config:
    schema_extra = {
        "example": {
            "title": "Abdulazeez Abdulazeez",
            "date": datetime.now(),
            "link": "Excellent course!",
            "site": "Excellent course!",
            
        }
    }