from urllib import response
from faker import Faker
from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()

def test_by_name():
    """ Testing find by_name method"""
    
    user_repo = UserRepositorySpy()
    find_user= FindUser(user_repo)
   
    attributes ={
        "name" : faker.name()
    }
    response = find_user.by_name(name=attributes["name"])
    
    print(response)
    
    #Testing input
    assert user_repo.select_user_by_name_params["name"] == attributes["name"]
    
    
    #Testing output
    assert response["Sucess"] is True
    assert response["Data"]
    
    def test_by_id():
        """ Testing find by_id method"""
    
    user_repo = UserRepositorySpy()
    find_user= FindUser(user_repo)
   
    attributes ={
        "id" : faker.random_number()
    }
    response = find_user.by_id(id=attributes["id"])
    
    print(response)
    
    #Testing input
    assert user_repo.select_user_by_name_params["id"] == attributes["id"]
    
    
    #Testing output
    assert response["Sucess"] is True
    assert response["Data"]
    

