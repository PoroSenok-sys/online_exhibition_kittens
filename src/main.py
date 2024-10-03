import os
import sys

from fastapi import FastAPI

from src.kittens.router import router as router_kittens

sys.path.insert(1, os.path.join(sys.path[0], '..'))

app = FastAPI(
    title="Online exhibition kittens"
)

app.include_router(router_kittens)
