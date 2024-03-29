from abc import ABC 
from abc import abstractmethod
from src.domain.models import Users

@abstractmethod
class UserRepositoryInterface(ABC):
    """ Interface to User Repository """
    
    def insert_user(self, name: str, password: int) -> Users:
        """ abstractmethod """
        
        raise Exception("Method not implemented")

    def select_user_by_name(self, name: str) -> Users:
        """ abstractmethod """
        
        raise Exception("Method not implemented")

    def select_user_by_id(self, id: int) -> Users:
        """ abstractmethod """
        
        raise Exception("Method not implemented")
    

    
 
    
