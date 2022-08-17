from faker import Faker
from src.domain.models import Pets
from .register import RegisterPet
from src.infra.test import PetRepositorySpy

faker = Faker()

def test_register():
    """ Testing registry method """
    
    pet_repo = PetRepositorySpy()
    register_pet = RegisterPet(pet_repo)
    attributes = {
        "name" : faker.name(),
        "specie" : "fish",
        "age" : faker.random_number(),
        "user_id" : faker.random_number()
    }
    
    response = register_pet.register(name=attributes["name"], specie=attributes["specie"],age=attributes["age"],user_id=attributes["user_id"])
    
    print(response)
    
    # Test input
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["user_id"] == attributes["user_id"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]
    
    
    # Test Output 
    assert response["Sucess"] is True
    assert response["Data"]
    
