from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    ForeignKey, Float, Date, ARRAY, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

engine = create_engine("mysql+mysqlconnector://root:admin123@localhost/Shop", echo=True)
Base = declarative_base()
session = Session(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    shop_name = Column(String(50))
    owner_id = Column(Integer, ForeignKey('user.id'))
    partner_id = Column(Integer, ForeignKey('user.id'))


class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    staff_name = Column(String(50))
    owner_id = Column(Integer, ForeignKey('user.id'))
    shop_id = Column(Integer, ForeignKey('shop.id'))


class Stock(Base):
    __tablename__ = 'stock'
    stock_id = Column(Integer, primary_key=True)
    date = Column(Date, default=func.current_date())
    shop_id = Column(Integer, ForeignKey('shop.id'))
    owner_id = Column(Integer, ForeignKey('user.id'))
    product = Column(String(100))
    price = Column(Float)
    quantity = Column(Integer)


class Order(Base):
    __tablename__ = 'order'
    order_id = Column(Integer, primary_key=True)
    date = Column(Date, default=func.current_date())
    shop_id = Column(Integer, ForeignKey('shop.id'))
    owner_id = Column(Integer, ForeignKey('user.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))
    product = Column(String(100))
    sell_price = Column(Float)
    sold_quantity = Column(Integer)
    stock_Id = Column(Integer, ForeignKey('stock.stock_id'))
    quantity = Column(Integer)

# Base.metadata.create_all(engine)
