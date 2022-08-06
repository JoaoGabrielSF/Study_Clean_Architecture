from typing import Dict,Type, List
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users

class FindUser(FindUserInterface):
    """ Class to definite usercase: Find User """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository
    
    def by_name(self, name: str) -> Dict[bool,List[Users]]:
        """ Select User by name 
        :param - user: name's user
        :return - Dictionary with informations of the process
        """
        response = None     
        validate_entry = isinstance(name, str) 
        
        if validate_entry:
            response = self.user_repository.insert_user(name)
            
        return { "Sucess": validate_entry, "Data": response}
  
    def by_id(self, id: int) -> Dict[bool,List[Users]]:
        """ Select User by id
        :param - user: id's user 
        :return - Dictionary with informations of the process
        """
        response = None     
        validate_entry = isinstance(id, int) 
        
        if validate_entry:
            response = self.user_repository.insert_user(id, int)
            
        return { "Sucess": validate_entry, "Data": response}