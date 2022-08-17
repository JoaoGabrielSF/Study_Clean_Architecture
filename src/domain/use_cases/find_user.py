from abc import ABC, abstractclassmethod
from src.domain.models import Users
from typing import Dict, List

class FindUser(ABC):
    """ Interface to FindUser use case"""
    
    @abstractclassmethod
    def by_id(self, id: int) ->Dict[bool, List[Users]]:
        """ Specific Case"""
        
        raise Exception(" Should implement method: by_id")
    
    @abstractclassmethod 
    def by_name(self, name: str) ->Dict[bool, List[Users]]:
        """ Specific Case"""
        
        raise Exception(" Should implement method: by_name")