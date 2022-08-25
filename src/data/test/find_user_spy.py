from typing import Dict, List
from src.domain.models import Users
from src.domain.test import mock_users

class FindUserSpy:
    """ Class to define usecase: Select User"""
    
    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.by_id_param = {}
        self.by_name_param = {}
  
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """ Select User by id """
        
        self.by_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)
        
        if validate_entry:
            response = [mock_users()]
            
        return {"Sucess": validate_entry, "Data": response}
    
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """ Select User by name """
        
        self.by_name_param["name"] = name
        response = None
        validate_entry = isinstance(name, str)
        
        if validate_entry:
            response = [mock_users()]
            
        return {"Sucess": validate_entry, "Data": response}
    
    