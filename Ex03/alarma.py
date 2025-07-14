def alarm_simulator(total_time):
    current_second = 0
    while current_second < total_time:
        current_second += 1

        if current_second % 10 == 0:
            print(f"Pausa de alarma en el segundo {current_second} (omitido)")
            continue
        
        print(f"Alarma activada en el segundo {current_second}")

        if current_second == total_time:
            break

    print(f"La alarma se ha desactivado tras {total_time} segundos activos.")

def main():
    try:
       time = int(input("Cuantos segundos deseas que pasen: "))
    except ValueError: 
        print("Los segundos deben ser números enteros")
    alarm_simulator(time)

if __name__ == "__main__":
    main()