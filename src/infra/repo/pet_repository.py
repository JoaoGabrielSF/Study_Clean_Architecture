from src.infra.config import DBConnectionHandler 
from src.infra.entities import Pets

class PetRepository:
    """ Class to manage Pet Repository """
    
    @classmethod
    def insert_pet(cls, name:str, specie:str, age:int):
        """ Insert data in pet entity
        :param  -name: pet name
                -specie: pet specie
                -age: pet age
        """
         
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = Pets(name=name, specie=specie, age=age )
                db_connection.session.add(new_pet)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise          
            finally:
                db_connection.session.close()