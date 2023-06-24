from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+mysqlconnector://root:admin123@localhost/Shop", echo=True)
Base = declarative_base()


class Customers(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    address = Column(String(50))
    email = Column(String(50))


Base.metadata.create_all(engine)

from sqlalchemy.orm import Session

# Create session
session = Session(engine)

# c1 = Customers(name='Ravi Kumar', address='Station Road Nanded', email='ravi@gmail.com')

# To add single data in table
# session.add(c1)

# To add multiple data into table
# session.add_all([
#     Customers(name='Komal Pande', address='Koti, Hyderabad', email='komal@gmail.com'),
#     Customers(name='Rajender Nath', address='Sector 40, Gurgaon', email='nath@gmail.com'),
#     Customers(name='S.M.Krishna', address='Budhwar Peth, Pune', email='smk@gmail.com')]
# )
# session.commit()
# session.close()

# all the data get used all()
# result = session.query(Customers).all()

# for i in result:
#     print ("Name: ",i.name, "Address:",i.address, "Email:",i.email)

# Update in data into table with pk id
# x = session.query(Customers).get(2)
# print(x.name, x.address, x.email)
# x.address = 'Khambha'
# session.commit()

# x = session.query(Customers).first()
# print ("Name: ", x.name, "Address:", x.address, "Email:", x.email)
#
# x.name = 'Chirag'
# print ("Name: ", x.name, "Address:", x.address, "Email:", x.email)
#
# session.rollback()
# print ("Name: ", x.name, "Address:", x.address, "Email:", x.email)


# update into multiple raw in table
# session.query(Customers).filter(Customers.id != 2).update(
#     {Customers.name: f"Mr.{Customers.name}"}, synchronize_session=False
# )
# session.commit()

# filter into table
# result = session.query(Customers).filter(Customers.id>2)

# for i in result:
#     print("ID:", i.id, "Name: ", i.name, "Address:", i.address, "Email:", i.email)

# x = session.query(Customers).get(3)
# session.delete(x)
# session.commit()
