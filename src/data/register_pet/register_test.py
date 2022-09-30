from faker import Faker
from .register import RegisterPet
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy

faker = Faker()

def test_register():
    """ Testing registry method """
    
    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)
    attributes = {
        "name" : faker.name(),
        "specie" : "fish",
        "age" : faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name()
        }
    }
    
    response = register_pet.register(
        name=attributes["name"], 
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"])


    # Test input
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]

    # Testing FindUser inputs
    assert find_user.by_id_param["user_id"] == attributes["user_information"]["user_id"]
    assert find_user.by_name_param["name"] == attributes["user_information"]["user_name"]
    
    # Test Output 
    assert response["Sucess"] is True
    assert response["Data"]
    
    print(attributes["age"])
    print(response["Data"])
    print(find_user.by_name_param["name"])
    
   
    