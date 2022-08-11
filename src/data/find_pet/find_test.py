from faker import Faker
from .find import FindPet 
from src.infra.test import PetRepositorySpy

faker = Faker()

def test_by_id():
    """ Testing find Pet by_id method """
    
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)
    
    attributes = {
        "id" : faker.random_number()
    }
    response = find_pet.find_pet_by_id(pet_id=attributes["id"])
    
    #testing input
    assert pet_repo.select_pet_by_id_params["id"] == attributes["id"]
    
    #testing output
    assert response["Sucess"] is True
    assert response["Data"]




def test_by_user_id():
    """ Testing find Pet by_use_id method """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)
    
    attributes = {
        "user_id" : faker.random_number()
    }
    response = find_pet.find_pet_by_user_id(user_id=attributes["user_id"])
    
    #testing input
    assert pet_repo.select_pet_by_user_id_params["user_id"] == attributes["user_id"]
    
    #testing output
    assert response["Sucess"] is True
    assert response["Data"]


