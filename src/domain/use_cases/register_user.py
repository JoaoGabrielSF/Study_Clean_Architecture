from abc import ABC
from abc import abstractmethod
from src.domain.models import Users
from typing import Dict

class RegisterUser(ABC):
    """ Interface to RegisterUser use case """
    
    @abstractmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """ Case """
        
        raise Exception("Should implement method: register")
    
    