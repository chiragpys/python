from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey


engine = create_engine("mysql+mysqlconnector://root:admin123@localhost/Shop", echo=True)
meta = MetaData()
connection = engine.connect()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(50))
)

shop = Table(
    'shop', meta,
    Column('id', Integer, primary_key=True),
    Column('shop_name', String(50)),
    Column('owner_id', Integer, ForeignKey('user.id')),
    Column('partner_id', Integer, ForeignKey('user.id')),
)
# meta.create_all(engine)

# used for insert data
# # ins = user.insert().values(id=5, username='rumit')
# connection = engine.connect()
# result = connection.execute(ins)
# connection.commit()
# connection.close()

# Select query
# sect = user.select().where(user.c.id>2)   # c attribute is an alias for column.
# result = connection.execute(sect)
#
# for row in result:
#     print(row)

# Update Query
# upt = user.update().where(user.c.id == 3).values(username='vishal')
# result = connection.execute(upt)
# connection.commit()
# connection.close()

# delete Query
# data_del = user.delete().where(user.c.username == 'rumit')
# result = connection.execute(data_del)
# connection.commit()
# connection.close()

# Insert into shop table
# ins = shop.insert().values(shop_name='Big Bazar', owner_id=1, )
# result = connection.execute(ins)
# connection.commit()
# connection.close()

# and() & or() Query
# from sqlalchemy import and_, or_
# sect = user.select().where(and_(user.c.username == 'chirag', user.c.id <3))
# result = connection.execute(sect)
# print(result.fetchall())
#
# sect = user.select().where(or_(user.c.username == 'chirag', user.c.id <3))
# result = connection.execute(sect)
# print(result.fetchall())











