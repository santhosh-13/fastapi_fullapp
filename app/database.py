from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Construct DB URL from separate fields
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.database_username}:{settings.database_password}"
    f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
)

# SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal class to interact with DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



'''while(True):
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='santhu',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print('db connection was successful')
        break
    except Exception as error:
        print('connection failed')
        print("Error:",error)
        time.sleep(2)'''
 