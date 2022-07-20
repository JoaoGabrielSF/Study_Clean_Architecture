class DBConnectionHandler:
    """Sqlalchemy database connection"""
    
    def __init__(self):
        self.__connection__string = "sqlite://storage.db"
        self.session = None