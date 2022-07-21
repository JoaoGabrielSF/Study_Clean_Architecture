#pylint: disable=E1101


from src.infra.config import DBConnectionHandler
from src.infra.config import Users

class FakerUser:
    """A simples Repository"""
   
    @classmethod
    def insert_use(cls, name: str, password: str):
        """ Class method """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Bagos", password="Lhama")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finaly:
                db_connection.session.close()