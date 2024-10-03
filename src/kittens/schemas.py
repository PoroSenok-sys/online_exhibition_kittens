from pydantic import BaseModel


# Схемы для таблицы Kitten
class KittenPostDTO(BaseModel):
    color: str
    age: int
    description: str
    breed_title: str


class KittenGetDTO(KittenPostDTO):
    id: int


class KittenRelDTO(KittenGetDTO):
    breed: "BreedGetDTO.title"


# Схемы для таблицы Breed
class BreedPostDTO(BaseModel):
    title: str


class BreedGetDTO(BreedPostDTO):
    id: int


class BreedRelDTO(BreedGetDTO):
    kittens: list["KittenGetDTO"]
