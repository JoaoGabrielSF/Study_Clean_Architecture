from faker import Faker
from src.data.interfaces import PetRepositoryInterface
from src.infra.entities.pets import AnimalTypes
from src.infra.config import DBConnectionHandler
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

def test_select_pet():
    """ Should select a user in Users table and compare it """
        
    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=2)
    
    
    specie_mock = AnimalTypes("fish")
    data =PetsModel(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)
        

    engine = db_connection_handler.get_engine()
    engine.execute(
            "INSERT INTO pets (id, name, specie, age, user_id ) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
                pet_id, name, specie, age, user_id
            )
        )
        
    query_user1 = pet_repository.select_pet_by_id(id=pet_id)
    query_user2 = pet_repository.select_pet_by_name(name=name)
    query_user3 = pet_repository.select_pet_by_id(id=pet_id)
    
    assert data in query_user1
    assert data in query_user2
    assert data in query_user3
        
    engine.execute("DELETE FROM pets WHERE id= '{}';".format(data.id))
