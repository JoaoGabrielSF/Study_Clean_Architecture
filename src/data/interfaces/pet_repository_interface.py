from abc import ABC 
from abc import abstractmethod
from src.domain.models import Pets

@abstractmethod
class PetRepositoryInterface(ABC):
    """ Interface to Pet Repository """
    
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """ abstractmethod """
        
        raise Exception("Method not implemented")

    def select_pet_by_id(self, pet_id: int) -> Pets:
        """ abstractmethod """
        
        raise Exception("Method not implemented")

    def select_pet_by_user_id(self, user_id: id) -> Pets:
        """ abstractmethod """
        
        raise Exception("Method not implemented")
