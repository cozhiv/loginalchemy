from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import pymysql

engine = create_engine(
      "mysql+pymysql://root:root@localhost/back")
#?encoding=utf8
#?host=localhost?port=3306
#engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    #from flaskr.models import User
    Base.metadata.create_all(bind=engine)


#>>> from yourapplication.database import init_db
#>>> init_db()
#>>> from yourapplication.database import db_session
#>>> from yourapplication.models import User
#>>> u = User('admin', 'admin@localhost')
#>>> db_session.add(u)
#>>> db_session.commit()

#>>> User.query.all()
#[<User u'admin'>]
#>>> User.query.filter(User.name == 'admin').first()