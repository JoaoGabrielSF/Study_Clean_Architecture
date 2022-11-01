from typing import Type
from abc import ABC, abstractclassmethod
from src.adapters.helpers import HttpRequest, HttpResponse

class RouteInterface(ABC):
    """ Interface to Routes """
    
    @abstractclassmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Defining Route """
        
        raise Exception("Should implement method: route")
    
