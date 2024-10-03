from typing import Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base, str_256

type_intpk = Annotated[int, mapped_column(primary_key=True)]


class BreedsOrm(Base):
    __tablename__ = "breeds"

    id: Mapped[type_intpk]
    title: Mapped[str_256] = mapped_column(unique=True)

    kittens: Mapped[list["KittensOrm"]] = relationship(
        back_populates="breed",
    )


class KittensOrm(Base):
    __tablename__ = "kittens"

    id: Mapped[type_intpk]
    color: Mapped[str_256]
    age: Mapped[int]
    description: Mapped[str_256]
    breed_title: Mapped[str] = mapped_column(ForeignKey("breeds.title"))

    breed: Mapped["BreedsOrm"] = relationship(
        back_populates="kittens",
    )
