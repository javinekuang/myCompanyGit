__author__ = 'Administrator'

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('sqlite:///test.db')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='3', name='Bob')
session.add(new_user)
session.commit()

user = session.query(User).filter(User.id=='3').one()

print 'type: ',type(user)
print 'name:', user.name

session.close()
