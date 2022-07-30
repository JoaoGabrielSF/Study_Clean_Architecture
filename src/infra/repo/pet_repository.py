from typing import List
from src.data.interfaces import PetRepositoryInterface
from src.domain.models.pets import Pets
from src.infra.config import DBConnectionHandler 
from src.infra.entities import Pets as PetsModel

class PetRepository(PetRepositoryInterface):
    """ Class to manage Pet Repository """
    
    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> List[Pets]:
        """ Insert data in pet entity
        :param  - name: pet name
                - specie: pet specie
                - age: pet age
                - user_id: id of the owner
        :return - tuple with new pet inserted
        """
         
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()
                
                return Pets(
                 id=new_pet.id,
                 name=new_pet.name,
                 specie=new_pet.specie.value,
                 age=new_pet.age,
                 user_id=new_pet.user_id
                 
                )
            except:
                db_connection.session.rollback()
                raise          
            finally:
                db_connection.session.close()
        
        return None
    
    @classmethod
    def select_pet_by_id(cls, id: int = None) -> List[Pets]:
         """
        Select data in pet entity by id and/or name
        :param - id: Id of the registry
        :return - List with Pets selected
        """    
         try:
                query_data = None
      
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=id)
                        .one()
                )
                query_data = [data]
                    
                return query_data
            
         except:
                        db_connection.session.rollback()
                        raise  
         finally: 
                    db_connection.session.close()
                
         return None
     
    @classmethod
    def select_pet_by_name(cls, name: str = None) -> List[Pets]:
         """
        Select data in user entity by id and/or name
        :param  - name: Pet name
        :return - List with Pets selected
        """
         try:
                query_data = None
      
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(name=name)
                        .one()
                )
                query_data = [data]
                    
                return query_data
         except:
                        db_connection.session.rollback()
                        raise  
         finally: 
                    db_connection.session.close()
                
         return None
     
     