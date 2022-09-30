from typing import Type
from src.adapters.helpers.http_models import HttpRequest, HttpResponse
from src.domain.use_cases import FindUser

class FindUserController:
    """ Class to define controller to find_user use case"""
    
    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case


    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """
        
        response = None  
        
        if http_request.query:
            # if query
        
            query_string_params = http_request.query.keys()
 
            if "user_id" in query_string_params and "user_name" in query_string_params:
                user_id = http_request.param["user_id"]
                user_name = http_request.param["user_name"]
                response = [self.find_user_use_case.by_id(user_id=user_id)
                            , self.find_user_use_case.by_name(name=user_name)] 
                
                    
            elif "user_id" in query_string_params and "user_name" not in query_string_params:
                  user_id = http_request.param["user_id"]
                  response = self.find_user_use_case.by_id(user_id=user_id)
           
            
            elif "user_id" not in query_string_params and "user_name" in query_string_params:
                  user_name = http_request.param["user_name"]
                  self.find_user_use_case.by_name(name=user_name)
                             