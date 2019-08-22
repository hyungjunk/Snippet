from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

meta = MetaData()
engine = create_engine('sqlite:///test.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# customers = Table(
#     'Invoice', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('customers_id', Integer)
# )

# The create_all() function uses the engine object to create all the defined table objects and stores the information in metadata.
# meta.create_all(engine)


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    invoice = relationship('Invoice', back_populates='customers')
    
    # 이렇게 하면 Customers 모델에 있는 attribute의 filter를 선행으로 걸어버릴 수 있음.
    jun_invoice = relationship("Invoice", primaryjoin="and_(Customers.id==Invoice.customers_id, Invoice.name=='jun')", backref='customers_only_jun')

    def __repr__(self):
        return str(self.id) + ' ' + self.name


class Invoice(Base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    customers_id = Column(Integer, ForeignKey('customers.id'))
    customers = relationship('Customers', back_populates='invoice')


    def __repr__(self):
        return str(self.id) + ' ' + self.name


# scalar 는 one_or_none이랑 같은거 같은데..
c1 = session.query(Customers).first()
i1 = session.query(Invoice).first()
print(i1.customers_only_jun)
