from pydantic import BaseModel, Field

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
