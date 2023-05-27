from pydantic import BaseModel

class Query(BaseModel):
    question: str

class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str

class Consulta(BaseModel):
    query: Query
    user_id: str
    file_name: str

class QueryRequest(BaseModel):
    query: str
    user_id: str
    file_name: str

class NodoCreateRequest(BaseModel):
    etiqueta: str
    propiedades: dict

class RelacionCreateRequest(BaseModel):
    nodo1_etiqueta: str
    nodo1_propiedades: dict
    nodo2_etiqueta: str
    nodo2_propiedades: dict
    relacion_nombre: str
    relacion_propiedades: dict

class PreguntaYML(BaseModel):
    file_name: str
    query: str

# Definir el modelo de datos para la solicitud
class PreguntaJson(BaseModel):
    json_obj: dict
    query: str