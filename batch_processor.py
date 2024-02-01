from database import get_remote_session, get_local_session
from sqlalchemy.exc import SQLAlchemyError
from models import Distancia, Technician, Establishment
from distance_calculator import haversine

BATCH_SIZE = 100  # Número de inserts a calcular antes de hacer un INSERT

def calculate_and_store_distances():
    remote_session = get_remote_session()
    local_session = get_local_session()

    establishments = remote_session.query(Establishment).all()
    technicians = remote_session.query(Technician).all()

    distances = []
    for est in establishments:
        for other_est in establishments:
            if est.id != other_est.id:
                distance = haversine(est.longitude, est.latitude, other_est.longitude, other_est.latitude)
                distances.append((est.id, other_est.id, distance))

        for tech in technicians:
            distance = haversine(est.longitude, est.latitude, tech.longitude, tech.latitude)
            distances.append((est.id, tech.id, distance))

            if len(distances) >= BATCH_SIZE:
                insert_distances_batch(local_session, distances)
                distances = []

    if distances:
        insert_distances_batch(local_session, distances)

def insert_distances_batch(session, distances_batch):
    try:
        for id_origen, id_destino, distancia in distances_batch:
            nueva_distancia = Distancia(id_origen=id_origen, id_destino=id_destino, distancia=distancia)
            session.add(nueva_distancia)

        session.commit()
    except SQLAlchemyError as e:
        print(f"Error al insertar el lote de distancias: {e}")
        session.rollback()

