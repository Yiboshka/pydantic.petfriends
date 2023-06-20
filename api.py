import requests
from pydantic import BaseModel, Field

class PetFriends:
    """апи библиотека к веб приложению Pet Friends"""

    valid_email = "bobo@mail.ru"
    valid_password = "sirius"
    api_key = "0caa2973502c2bebab72af3ba9a72c25913674901dc6b306303974ce"

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self):

        headers = {
            'email': self.valid_email,
            'password': self.valid_password,
        }
        response = requests.get(self.base_url+'api/key', headers=headers)
        return response

    def add_new_pet_simple(self, name, animal_type,
                           age):
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': self.api_key}
        response = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        return response

    def update_pet(self, pet_id, name,
                   animal_type, age):
        headers = {'auth_key': self.api_key}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        response = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        return response
