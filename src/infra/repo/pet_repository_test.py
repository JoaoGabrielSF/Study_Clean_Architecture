import enum
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities.pets import AnimalType
from .pet_repository import PetRepository
from src.infra.entities import Pets as PetsModel


faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_pet():
    """Should Insert Pet"""

    name = faker.name()
    specie = 'fish'
    age = faker.random_number(digits=2)
    user_id = faker.random_number()
    engine = db_connection_handler.get_engine()
    
   
    #SQL Commands 
    new_pet = pet_repository.insert_pet(name, specie, age, user_id)
    engine = db_connection_handler.get_engine()
    query_pet = engine.execute("SELECT * FROM pets WHERE id='{}';".format(new_pet.id)).fetchone()
    
    print(new_pet)
    print(query_pet)
    
    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id
    
    engine.execute("DELETE FROM pets WHERE id= '{}';".format(new_pet.id))
    
