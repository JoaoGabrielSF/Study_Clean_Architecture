from faker import Faker
from .find_user_controller import FindUserController
from src.data.test import FindUserSpy
from src.adapters.helpers import HttpRequest
from src.infra.test import UserRepositorySpy

faker = Faker()

def test_handle():
    """ Testing Handle method"""
    
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest( query= {
        "user_id": faker.random_number(), "user_name": faker.word()}    
    )

    response = find_user_controller.route(http_request)
    
    # Testing Inputs
    assert( 
           find_user_use_case.by_id_param["user_id"]
           ==  http_request.query["user_id"]
           )
    assert (
        find_user_use_case.by_name_param["user_name"]
           ==  http_request.query["user_name"]
    )
    
    # Testing Output
    assert response.status_code == 200
    assert response.body