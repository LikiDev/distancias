import schedule
import time
from batch_processor import calculate_and_store_distances

def tarea_programada():
    print("Iniciando el cálculo de distancias...")
    calculate_and_store_distances()
    print("Cálculo de distancias completado.")

# Programa la tarea para que se ejecute cada cierto tiempo, por ejemplo, cada hora
schedule.every(1).hour.do(tarea_programada)

# Bucle infinito para mantener el script corriendo y ejecutando las tareas programadas
while True:
    schedule.run_pending()
    time.sleep(60)  # Espera 60 segundos antes de verificar nuevamente

