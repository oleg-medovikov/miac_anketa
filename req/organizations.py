from func import get_organizations
from .app import app
from typing import List


@app.get("/organizations", response_model=List[list])
async def organizations():
    return get_organizations()
