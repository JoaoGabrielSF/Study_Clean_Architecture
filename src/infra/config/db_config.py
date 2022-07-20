from sqlalchemy import create_engine

class DBConnectionHandler:
    """Sqlalchemy database connection"""
    
    def __init__(self):
        self.__connection__string = "sqlite://storage.db"
        self.session = None
        
    def get_engine(self):
        """Return connection Engine
        :param - None
        :return - engine connection to Database
        """
        
        engine = create_engine(self.__connection__string)   
        return engine 