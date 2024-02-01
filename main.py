from fastapi import FastAPI
import uvicorn
from typing import List
import threading
import scheduler  # Asume que scheduler.py contiene la lógica de programación de tareas

app = FastAPI()

# Endpoint para obtener técnicos cerca de un establecimiento
@app.get("/tecnicos-cercanos/")
async def tecnicos_cercanos(establecimiento_id: int, radio: float, servicios: List[int]):
    # Lógica para obtener técnicos cercanos
    # Debes implementar esta función utilizando tus bases de datos
    return {"message": "Técnicos cercanos"}

# Endpoint para obtener establecimientos cercanos a otro establecimiento
@app.get("/establecimientos-cercanos/")
async def establecimientos_cercanos(establecimiento_id: int, radio: float):
    # Lógica para obtener establecimientos cercanos
    # Debes implementar esta función utilizando tus bases de datos
    return {"message": "Establecimientos cercanos"}

def iniciar_scheduler():
    # Inicia el scheduler en un hilo separado
    thread = threading.Thread(target=scheduler.iniciar)
    thread.start()

if __name__ == "__main__":
    iniciar_scheduler()
    uvicorn.run(app, host="0.0.0.0", port=8000)
