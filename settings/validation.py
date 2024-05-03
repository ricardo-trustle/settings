from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ValidationError


class Cluster(BaseModel):
    cloud: str
    name: str
    region: str
    subnet_ids: List[str]
    vpc_id: str


class Database(BaseModel):
    host: str
    name: str
    password: str
    port: int
    sslmode: str
    sslrootcert: Optional[str] = None
    username: str


class Model(BaseModel):
    cluster: Cluster
    database: Database


def valid(data: dict) -> bool:
    try:
        Model(**data)
        return True
    except ValidationError:
        return False
