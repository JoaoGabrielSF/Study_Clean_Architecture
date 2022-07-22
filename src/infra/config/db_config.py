from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    """Sqlalchemy database connection"""
    
    def __init__(self):
        self.__connection__string = "sqlite:///storage.db"
        self.session = None
        
    def get_engine(self):
        """Return connection Engine
        :param - None
        :return - engine connection to Database
        """
        
        engine = create_engine(self.__connection__string)   
        return engine 
    
    def __enter__(self):
        engine = create_engine(self.__connection__string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close() #pylint: disable=no-menber