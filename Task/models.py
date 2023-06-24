from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    ForeignKey, Float, Date, insert
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

engine = create_engine("mysql+mysqlconnector://root:admin123@localhost/python", echo=False)
Base = declarative_base()
session = Session(engine)

user_shop_partner = Table('user_shop_partner', Base.metadata,
                          Column('user_id', Integer, ForeignKey('user.id')),
                          Column('shop_id', Integer, ForeignKey('shop.id'))
                          )

order_stock_table = Table(
    'order_stock_table',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('order.id')),
    Column('stock_id', Integer, ForeignKey('stock.id')),
    Column('quantity_sold', Integer)
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False, default='owner')
    owner_id = Column(Integer, ForeignKey('user.id'))
    shop_id = Column(Integer, ForeignKey('shop.id'))
    partner_shops = relationship('Shop', secondary=user_shop_partner, backref='user', lazy='dynamic')


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    shop_name = Column(String(50))
    owner_id = Column(Integer, ForeignKey('user.id'))


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product = Column(String(100))


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    date = Column(Date, default=func.current_date())
    price = Column(Float)
    quantity = Column(Integer)
    shop_id = Column(Integer, ForeignKey('shop.id'))

    product = relationship("Product", backref="stock")


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    date = Column(Date, default=func.current_date())
    sell_price = Column(Float)
    sold_quantity = Column(Integer)
    shop_id = Column(Integer, ForeignKey('shop.id'))
    owner_id = Column(Integer, ForeignKey('user.id'))
    staff_id = Column(Integer, ForeignKey('user.id'))

    stocks = relationship(
        'Stock',
        secondary=order_stock_table,
        backref='order'
    )
    product = relationship("Product", backref="order")

# Base.metadata.create_all(engine)

