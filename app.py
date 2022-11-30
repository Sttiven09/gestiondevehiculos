from uuid import uuid4
from pydantic import BaseModel
from fastapi import FastAPI
#from typing import List

app = FastAPI()


class Vehiculo(BaseModel):

    id: int
    marca: str
    modelo: int
    caracteristicas: str
    tipo_vehiculo: str
    ubicacion: str
#skills: List[str] = []
vehiculos = []

@app.get("/vehiculos")
def get_vehiculos():

    return vehiculos

@app.get("/vehiculos/{id}")
def get_vehiculo(id: int):

    for vehiculo in vehiculos:
        if vehiculo["id"] == id:
            return vehiculo
    return "El Vehiculo no existe"

@app.post("/vehiculos")
def save_vehiculo(vehiculo: Vehiculo):

    vehiculo.id = str(uuid4())
    vehiculo.append(vehiculo.dict())
    return "Vehiculo Registrado"

@app.put("/vehiculos/{id}")
def update_vehiculo(updated_updated: Vehiculo, id: int):

    for Vehiculo in vehiculos:
        if Vehiculo["id"] == id:
            Vehiculo["Marca"] = updated_updated.marca
            Vehiculo["Modelo"] = updated_updated.modelo
            Vehiculo["Caracteristicas"] = updated_updated.caracteristicas
            Vehiculo["Tipo Vehiculo"] = updated_updated.tipo_vehiculo
            Vehiculo["Ubicación"] = updated_updated.ubicacion
            #student["skills"] = updated_updated.skills
        return "Vehiculo Modificado"
    return "No existe el Vehiculo"

@app.delete("/vehiculos/{id}")
def delete_vehiculos(id: int):

    for vehiculo in vehiculos:
        if vehiculo["id"] == id:
            vehiculo.remove(vehiculo)
        return "Vehiculo Eliminado"
    return "No existe el Vehiculo"
