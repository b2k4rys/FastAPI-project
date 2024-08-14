from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session 
from typing import Literal
from sqlalchemy.orm import sessionmaker


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
Session = sessionmaker(bind=engine)
session = Session()



car_brands = session.query(models.Car_Brands).all()
brand = {}
for i in car_brands:
  brand[i.title] = i.title


class UserBase(BaseModel):
  username: str

class CarBrandBase(BaseModel):
  title: str
  country: str

class Car(BaseModel):
  brands: Literal[brand] = ''


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependecy = Annotated[Session, Depends(get_db)]


@app.post('/user_create/')
async def create_users(user: UserBase, db: db_dependecy):
  db_user = models.User(username = user.username)
  db.add(db_user)
  db.commit()


@app.post('/car_brand_create/')
async def create_car_brand(car_brand: CarBrandBase, db: db_dependecy):
  db_car_brand = models.Car_Brands(title = car_brand.title, country = car_brand.country)
  db.add(db_car_brand)
  db.commit()


@app.post('/car_create')
async def create_car(db: db_dependecy, data: Car = Depends()):
  return data

