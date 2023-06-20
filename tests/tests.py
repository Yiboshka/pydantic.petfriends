from api import PetFriends
from pydantic import BaseModel, Field
import pytest

class apikey(BaseModel):
    key: str = Field()

class pets_param(BaseModel):
    age: str = Field()
    animal_type: str = Field()
    created_at: str = Field()
    id: str = Field()
    name: str = Field()
    pet_photo: str = Field()
    user_id: str = Field(None)

pf = PetFriends()

def test_api_key_received():
    response = pf.get_api_key()
    result = apikey.parse_raw(response.text)
    assert response.status_code == 200
    assert result.key == pf.api_key

@pytest.mark.parametrize('name, animal_type, age', [
    ('Чжань-гэ', 'кролик', '4'),
    ('Бобо', 'львенок', '2'),
    ('Орешек', 'кошка', '1')
])

def test_add_pet_simple_received(name, animal_type, age):
    response = pf.add_new_pet_simple(name, animal_type, age)
    result = pets_param.parse_raw(response.text)
    assert response.status_code == 200
    assert result.name == name
    assert result.animal_type == animal_type
    assert result.age == age
    assert result.id != ''
    assert result.pet_photo == ''

@pytest.mark.parametrize('name, animal_type, age', [
    ('Чжань-гэ', 'заец', '6'),
    ('Бобо', 'собака', '4'),
    ('Орешек', 'кошка', '3')
])

def test_update_pet_simple_received(name, animal_type, age):
    response = pf.add_new_pet_simple(name, animal_type, age)
    result = pets_param.parse_raw(response.text)
    assert response.status_code == 200
    assert result.name == name
    assert result.animal_type == animal_type
    assert result.age == age
    assert result.id != ''
    assert result.pet_photo == ''


