from fastapi import APIRouter
from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from src.database import async_session_factory
from src.kittens.model import BreedsOrm, KittensOrm
from src.kittens.schemas import KittenPostDTO, BreedPostDTO

router = APIRouter(
    prefix="/kittens",
    tags=["Kittens"]
)


@router.get("/breeds")
async def get_breeds():
    async with async_session_factory() as session:
        query = select(BreedsOrm)
        print("query", query)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None,
        }


@router.get("/kittens")
async def get_kittens():
    async with async_session_factory() as session:
        query = select(KittensOrm)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None,
        }


# @router.get("/kittens_filter")
# async def get_kittens_filter(breed_kitten: str) -> dict:
#     async with async_session_factory() as session:
#         query = select(KittensOrm).options(joinedload(KittensOrm.breed)).filter(KittensOrm.breed.title == breed_kitten)
#         result = await session.execute(query)
#         return {
#             "status": "success",
#             "data": result.mappings().all(),
#             "details": None,
#         }

@router.post("")
async def add_kittens(new_kitten: KittenPostDTO) -> dict:
    async with async_session_factory() as session:
        select_breed_title = select(BreedsOrm).filter(BreedsOrm.title == new_kitten.breed_title)
        print("select_breed_title", select_breed_title)

        if select_breed_title:
            breed = BreedsOrm(title=new_kitten.breed_title)
            session.add(breed)
            await session.commit()

        kitten = insert(KittensOrm).values(**new_kitten.model_dump())
        await session.execute(kitten)
        await session.commit()

        return {"status": "success"}
