from typing import Dict, List
from src.domain.models import Pets 
from src.domain.test import mock_pets

class FindPetSpy:
    """ Class to mock usecase: Find Pet"""
    
    def __init__(self, pet_repository: any):
        self.pet_repository = pet_repository
        self.by_pet_id_params = {}
        self.by_user_id_params = {}
    
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """ Find Pet by pet_id """

        self.by_pet_id_params["pet_id"] = pet_id
        response = None
        validate_entry = isinstance(pet_id, int)
        
        if validate_entry:
            response = [mock_pets()]

        return { "Sucess": validate_entry, "Data": response}
    
    
    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """ Find Pet by user_id """
        
        self.by_user_id_params["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)
        
        if validate_entry:
            response = [mock_pets()]

        return { "Sucess": validate_entry, "Data": response}