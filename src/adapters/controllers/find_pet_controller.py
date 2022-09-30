from typing import Type 
from src.adapters.helpers.http_models import HttpRequest, HttpResponse
from src.domain.use_cases import FindPet

class FindPetController:
    """ Class to define controller to find_user use case"""
    
    def __init__(self, find_pets_use_case):
        self.find_pets_use_case = find_pets_use_case
        
    
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse :
        """ Method to call use case """

