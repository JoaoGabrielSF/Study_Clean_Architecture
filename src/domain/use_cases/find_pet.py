from abc import ABC, abstractclassmethod
from src.domain.models  import Pets
from typing import Dict, List

class FindPet(ABC):
    """ Interface to FindPet use case"""
    
    @abstractclassmethod
    def by_pet_id(self, id: int) ->Dict[bool, List[Pets]]:
        """ Specific Case"""
        
        raise Exception(" Should implement method: by_pet_id")
    
    @abstractclassmethod 
    def by_user_id(self, user_id: int) ->Dict[bool, List[Pets]]:
        """ Specific Case"""
        
        raise Exception(" Should implement method: by_user_id")