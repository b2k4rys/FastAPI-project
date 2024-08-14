from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), unique=True)



class Car_Brands(Base):
  __tablename__ = 'car_brands'

  id = Column(Integer, primary_key = True, autoincrement=True)
  title = Column(String, index=True, unique=True)
  country = Column(String)


class Car_models(Base):
  __tablename__ = 'car_models'

  id = Column(Integer, primary_key = True, autoincrement=True)
  car_brand = Column(String, ForeignKey('car_brands.title'))
  model = Column(String, unique=True)





