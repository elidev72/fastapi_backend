from pydantic import BaseModel
from typing import List

class Curso(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    nivel: str
    duracion: int

cursos_db: List[Curso] = []
ultimo_id: int = 0

