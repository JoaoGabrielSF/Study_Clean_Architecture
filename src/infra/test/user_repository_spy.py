from typing import List
from src.domain.test import mock_users
from src.domain.models import Users


class UserRepositorySpy:
    """ Spy to User Repository"""
    
    def __init__(self):
        self.insert_user_params = {}
        self.select_user_by_id_params = {}
        self.select_user_by_name_params ={}
        
        
        
    def insert_user(self, name: str, password: str) -> Users:
        """ Spy to all the attributes"""
   
        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password
        
        return mock_users()
   
   
   
    def select_user_by_id(self, id: int = None) -> List[Users]: 
        """ Spy to all the attributes"""  
        self.select_user_by_id_params["id"] = id
        
        return mock_users()
   
          
    def select_user_by_name(self, name: str = None) -> List[Users]:
        self.select_user_by_name_params["name"] = name   
        
        return mock_users()