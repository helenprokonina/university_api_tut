import pytest
from fastapi.testclient import TestClient
from random import randint
from app.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
        
        
def test_when_app_running_status_endpoint_should_return_OK(client):
    response = client.get("/status")
    assert response.status_code == 200 
    data = response.json()
    assert data['message']=='OK'     
    
    
def test_when_given_user_name_should_create_a_student_in_db(client):
    random = randint(0, 100000)
    first_name = f"John {random}"
    last_name = f"World {random}"
    create_response = client.post("/student/", json={"first_name": first_name, "last_name": last_name})      
    assert create_response.status_code == 200
    student_id = create_response.json()['id']
    assert student_id != None
    
    
def test_get_all_students_should_retuen_list_of_students(client):
    response = client.get("/students/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data)>0
    for student in data:
        assert "id" in student
        assert "first_name" in student
        assert "last_name" in student
            
def test_delete_student_should_delete_student_from_db(client):
    #Create a new student
    random = randint(0, 100000)
    first_name = f"John {random}"
    last_name = f"World {random}"
    create_response = client.post("/student/", json={"first_name": first_name, "last_name": last_name})  
    assert create_response.status_code == 200
    student_id = create_response.json()['id']
    assert student_id != None    
    
    #Delete the student 
    delete_response = client.delete(f"/student/{student_id}") 
    assert delete_response.status_code == 200
    
    #Verify that the student is no longer exists in the list of students
    response = client.get("/students/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data)>0
    for student in data:
        assert student["id"] != student_id
        
    