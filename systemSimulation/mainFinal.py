""" 
    Proyecto: Simulacion del comportamiento de un flujo de vehiculos en una via transitaria
    Integrantes:
        - Luis Sanchez, cedula: 26.388.923
        - Lanchez, Brando, cedula: 25.239.611
"""
from random import randint
from datetime import time, timedelta, date, datetime
import argparse

parser = argparse.ArgumentParser(description="Simulacion del comportamiento de un flujo de vehiculos en una via transitaria")
parser.add_argument("--date-start", help="fecha de inicio del programa, ejemplo: \"2021/01/1 12:20:20\"", default="2021/01/1 12:00:00")
parser.add_argument("--end-date", help="fecha de finalizado el programa, ejemplo: \"2021/12/31 11:59:00\"", default="2021/12/31 11:59:00")
args = parser.parse_args()
north_traffic = 0
south_traffic = 0
addressing_north = 0
addressing_south = 0
start_time = datetime.strptime(args.date_start, "%Y/%m/%d %H:%M:%S")
end_time = datetime.strptime(args.end_date, "%Y/%m/%d %H:%M:%S")
add_time = timedelta(hours=1)
holidays = ["1/1", "2/15", "2/16", "4/1", "4/02", "4/19", "5/1", "5/09", "6/24", "7/05", "7/24", "10/12", "12/24", "12/25", "12/31"]
index = 0

# Diferenciador de dias y horas de la semana para el flujo vehicular
def differenceBetweenDays(weekday):
    weekday = date.isoweekday(weekday)
    global north_traffic
    global south_traffic
    current_time = start_time.time()
    
    if weekday == 1 or weekday == 2 or weekday == 3 or weekday == 4 or weekday == 5:    
        if current_time >= time(6) and current_time <= time(9):
            north_traffic = randint(1, 300)
            south_traffic = randint(1, 300)

        elif current_time >= time(11) and current_time <= time(13):
            north_traffic = randint(1, 300)
            south_traffic = randint(1, 300)

        elif current_time >= time(15) and current_time <= time(20):
            north_traffic = randint(1, 300)

        elif current_time >= time(15) and current_time <= time (22):
            south_traffic = randint(1, 300)

        else:
            north_traffic = randint(1, 300)
            south_traffic = randint(1, 300)

        return [north_traffic, south_traffic]

    else:
        if current_time >= time(3) and current_time <= time(3):
            south_traffic = randint(1, 200)
        
        elif current_time >= time(6) and current_time <= time(20):
            south_traffic = randint(1, 120)

        elif current_time >= time(7) and current_time <= time(9):
            north_traffic = randint(1, 100)
        
        elif current_time >= time(4) and current_time <= time(22):
            north_traffic = randint(1, 60)
        
        return [north_traffic, south_traffic]

# Verificando cantidad de vehiculos para habilitar la nueva via en el flujo requerido
def increasedVehicleFlow(north, south):
    global addressing_north
    global addressing_south

    if north > south:
        addressing_north += 1
    else:
        addressing_south += 1
    return [addressing_north, addressing_south]

while start_time < end_time:
    transform_date = str(start_time.month) + "/" + str(start_time.day)

    print(f"\nInicio de la simulacion: {start_time}")

    # Verificando dias festivos
    if transform_date == holidays[index]:
        differenceBetweenDays_values = differenceBetweenDays(start_time)
        increasedVehicleFlow_values = increasedVehicleFlow(north_traffic, south_traffic)
        differenceBetweenDays_values = north_traffic, south_traffic
        increasedVehicleFlow_values = addressing_north, addressing_south

        print(f"Cantidad de vehiculos en direccion NORTE: {north_traffic * 3}")
        print(f"Cantidad de vehiculos en direccion SUR: {south_traffic * 3}")
        print(f"Cantidad de desvios hacia el NORTE: {addressing_north}")
        print(f"Cantidad de desvios hacia el SUR: {addressing_south}")
        index += 1

    else:
        differenceBetweenDays_values = differenceBetweenDays(start_time)
        increasedVehicleFlow_values = increasedVehicleFlow(north_traffic, south_traffic)
        differenceBetweenDays_values = north_traffic, south_traffic
        increasedVehicleFlow_values = addressing_north, addressing_south

        print(f"Cantidad de vehiculos en direccion NORTE: {north_traffic}")
        print(f"Cantidad de vehiculos en direccion SUR: {south_traffic}")
        print(f"Cantidad de desvios hacia el NORTE: {addressing_north}")
        print(f"Cantidad de desvios hacia el SUR: {addressing_south}")

    start_time += add_time

print(f"\nFin de la simulacion: {start_time}")
