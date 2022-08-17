from abc import ABC
from abc import abstractmethod
from src.domain.models import Pets
from typing import Dict, List

class RegisterPet(ABC):
    """ Interface to RegisterPet use case """

    @abstractmethod
    def register(cls, name: str, specie: str, age: int, user_id:int)-> Dict[bool,Pets]:
        """ Case """   
        
        raise Exception("Should implement method: register")     

