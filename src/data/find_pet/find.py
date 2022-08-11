from src.domain.models.pets import Pets
from typing import Dict, List,Type
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository 


class FindPet(FindPetInterface):
    """ Class to definite usercase: Find Pet """
    
    def __init__(self, pet_repository: Type[PetRepository]):
     self.pet_repository = pet_repository
     
     
    def find_pet_by_id(self, pet_id: int) -> Dict[bool,List[Pets]]:
        """ Select Pet by pet_id
        :params - id : pet's id
        :return - Dictionary with informations of the process
        """
        
        response = None
        validate_entry = isinstance(pet_id, int)
        
        if validate_entry:
            response = self.pet_repository.select_pet_by_id(pet_id)
          
        return{"Sucess" : validate_entry, "Data" : response}
         
     
    def find_pet_by_user_id(self, user_id: int) -> Dict[bool,List[Pets]]:
        """ Select Pet by user_id
        :params - user_id : pet's User_id
        :return - Dictionary with informations of the process
        """
        
        response = None
        validate_entry = isinstance(user_id, int)
        
        if validate_entry:
            response = self.pet_repository.select_pet_by_user_id(user_id)
        
        return{"Sucess" : validate_entry, "Data" : response}