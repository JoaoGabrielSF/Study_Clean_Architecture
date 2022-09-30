from typing import Type
from src.adapters.helpers.http_models import HttpRequest, HttpResponse
from src.domain.use_cases import FindPet

class FindPetController:
    """ Class to define controller to find_user use case"""
    
    def __init__(self, find_pets_use_case: Type[FindPet]):
        self.find_pets_use_case = find_pets_use_case
        
    
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None
        
        if http_request:
            # if query
            
            query_string_params = http_request.query 

            if "pet_id" in query_string_params and "user_id" in query_string_params:
                pet_id = http_request.param["pet_id"]
                user_id = http_request.param["user_id"]
                response = [self.find_pets_use_case.by_pet_id(id=pet_id),
                            self.find_pets_use_case.by_user_id(user_id=user_id)]
                
            elif "pet_id" not in query_string_params and "user_id" in query_string_params:
                user_id = http_request.param["user_id"]
                response = self.find_pets_use_case.by_user_id(user_id=user_id)
            
            elif "pet_id" in query_string_params and not "user_id" in query_string_params:
                pet_id = http_request
                response = self.find_pets_use_case.by_pet_id(id=pet_id)
                
            