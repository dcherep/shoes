from sqlalchemy import create_engine,Column, Integer, String, ForeignKey, Date,Float,Text
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("postgresql://admin:12345@217.71.129.139:6075/chudo_obuv")

class Base(DeclarativeBase): pass
class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    surname=Column(String,nullable=False)
    name=Column(String,nullable=False)
    patr=Column(String)
    login=Column(String,nullable=False )
    role_id=Column(Integer,ForeignKey("roles.id"),nullable=False)
    role=relationship("Role", lazy="joined")
    #def __str__(self):
        #return f'{self.surname} {self.name} {self.patr}

class Role(Base):
    __tablename__="roles"
    id = Column(Integer, primary_key=True,index=True)
    name=Column(String,nullable=False)

class Size(Base):
    __tablename__="sizes"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=True)

class Category(Base):
    __tablename__="categories"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)

class SubCategory(Base):
    __tablename__="sub_categories"
    id = Column(Integer, primary_key=True, index=True)
    category_id=Column(Integer,ForeignKey("categories.id"),nullable=False )
    name=Column(String,nullable=False)
    category = relationship("Category", lazy="joined")

class Manufacturers(Base):
    __tablename__="manufacturers"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)

class Tovars(Base):
    __tablename__="tovars"
    id = Column(Integer, primary_key=True, index=True)
    sub_cat_id=Column(Integer,ForeignKey("sub_categories.id"),nullable=False )
    manufactures_id=Column(Integer,ForeignKey("manufacturers.id"),nullable=False )
    name=Column(String,nullable=False)
    description=Column(String,nullable=False)
    content=Column(String,nullable=False)
    price=Column(Float,nullable=False )
    image_path=Column(String)

    manufacture = relationship("Manufacturers", lazy="joined")
    sub_cat = relationship("SubCategory", lazy="joined")
    category = association_proxy("sub_cat", "category")
    items = relationship("TovarItems", lazy="joined")
    order_items = relationship("OrdersItems", lazy="joined")

class TovarItems(Base):
    __tablename__="tovar_items"
    id = Column(Integer, primary_key=True, index=True)
    tovar_id=Column(Integer,ForeignKey("tovars.id"),nullable=False )
    size_id=Column(Integer,ForeignKey("sizes.id"),nullable=False )
    amount=Column(String,nullable=False)

class Orders(Base):
    __tablename__="orders"
    id = Column(Integer, primary_key=True, index=True)
    date=Column(Date,nullable=False )
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False )

class OrdersItems(Base):
    __tablename__="orders_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id=Column(Integer,ForeignKey("orders.id"),nullable=False )
    tovar_id=Column(Integer,ForeignKey("tovars.id"),nullable=False )
    size_id=Column(Integer,ForeignKey("sizes.id"),nullable=False )
    amount=Column(String,nullable=False)
    price=Column(Float,nullable=False )
    orders=relationship("Orders", lazy="joined")


def create():
    Base.metadata.create_all(bind=engine)
    print("Созданыь бд и таблицы")


