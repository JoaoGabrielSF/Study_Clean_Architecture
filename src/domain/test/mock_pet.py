from faker import Faker
from src.domain.models import Pets


faker = Faker()


def mock_pets() -> Pets:
    """ Mocking Users """
    
    return Pets(
       id=faker.random_number(), 
       namer=faker.name(),  
       specie="fish", 
       age=faker.random_number, 
       user_id=faker.random_number 
    )
    

    
