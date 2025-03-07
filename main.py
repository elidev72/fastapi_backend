from fastapi import FastAPI, HTTPException
from cursos import Curso, List, cursos_db, ultimo_id

app = FastAPI()

@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return cursos_db

@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    global ultimo_id
    ultimo_id+=1
    curso.id = ultimo_id
    cursos_db.append(curso)
    return curso

@app.get("/cursos/{curso_id}/", response_model=Curso)
def obtener_curso(curso_id: int):
    curso = next((c for c in cursos_db if c.id == curso_id), None) # Solo toma la 1er coicidencia por el next

    if curso is None:
        raise HTTPException(status_code=404, detail='Curso no encontrado')
    
    return curso

@app.put("/cursos/{curso_id}/", response_model=Curso)
def actualizar_curso(curso_id: int, curso_actualizado: Curso):
    curso = next((c for c in cursos_db if c.id == curso_id), None)

    if curso is None:
        raise HTTPException(status_code=404, detail='Curso no encontrado')
    
    curso_actualizado.id = curso_id
    
    index = cursos_db.index(curso)
    cursos_db[index] = curso_actualizado
    
    return curso_actualizado

@app.delete("/cursos/{curso_id}/", response_model=Curso)
def eliminar_curso(curso_id: int):
    curso = next((c for c in cursos_db if c.id == curso_id), None)

    if curso is None:
        raise HTTPException(status_code=404, detail='Curso no encontrado')
    
    cursos_db.remove(curso)
    
    return curso
