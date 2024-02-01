from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

REMOTE_DB_URL = "mysql+pymysql://dbuseror:securepwdor@88.77.66.55/dbname"
remote_engine = create_engine(REMOTE_DB_URL)
RemoteSession = sessionmaker(bind=remote_engine)

LOCAL_DB_URL = "mysql+pymysql://dbuseror:securepwdor@localhost/dbname"
local_engine = create_engine(LOCAL_DB_URL)
LocalSession = sessionmaker(bind=local_engine)

def get_remote_session():
    return RemoteSession()

def get_local_session():
    return LocalSession()