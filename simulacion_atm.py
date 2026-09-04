import simpy
import random

# Variables globales para estadísticas
tiempos_espera = []
clientes_atendidos = 0

def cliente(env, nombre, cajeros, tiempo_transaccion_promedio):
    global clientes_atendidos
    tiempo_llegada = env.now
    print(f"[{env.now:.2f} min] {nombre} llega al banco.")

    # El cliente solicita un cajero
    with cajeros.request() as peticion:
        yield peticion # Espera su turno si están ocupados
        
        tiempo_espera = env.now - tiempo_llegada
        tiempos_espera.append(tiempo_espera)
        print(f"[{env.now:.2f} min] {nombre} pasa al cajero (Esperó en fila: {tiempo_espera:.2f} min).")

        # Simular el tiempo que tarda la transacción
        tiempo_uso = random.expovariate(1.0 / tiempo_transaccion_promedio)
        yield env.timeout(tiempo_uso)

        print(f"[{env.now:.2f} min] {nombre} termina su transacción y sale.")
        clientes_atendidos += 1

def generador_clientes(env, cajeros, tasa_llegada, tiempo_transaccion_promedio):
    i = 1
    while True:
        # Generar el tiempo de llegada del siguiente cliente
        yield env.timeout(random.expovariate(1.0 / tasa_llegada))
        env.process(cliente(env, f"Cliente {i}", cajeros, tiempo_transaccion_promedio))
        i += 1

def main():
    print("--- SIMULACIÓN DE CAJEROS AUTOMÁTICOS (ATM) ---")
    print("Ingrese los datos recabados en su trabajo de campo:\n")
    
    try:
        num_cajeros = int(input("1. Número de cajeros disponibles (ej. 2): "))
        tasa_llegada = float(input("2. Tiempo promedio entre llegadas de clientes (minutos, ej. 1.5): "))
        tiempo_transaccion = float(input("3. Tiempo promedio de transacción (minutos, ej. 3.0): "))
        tiempo_simulacion = float(input("4. Tiempo total a simular (minutos, ej. 45): "))
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
        return

    print("\n--- INICIANDO SIMULACIÓN ---")
    env = simpy.Environment()
    cajeros = simpy.Resource(env, capacity=num_cajeros)

    env.process(generador_clientes(env, cajeros, tasa_llegada, tiempo_transaccion))
    env.run(until=tiempo_simulacion)

    print("\n--- RESULTADOS DEL SISTEMA SIMULADO ---")
    print(f"Total de clientes atendidos: {clientes_atendidos}")
    if tiempos_espera:
        espera_promedio = sum(tiempos_espera) / len(tiempos_espera)
        espera_max = max(tiempos_espera)
        print(f"Tiempo de espera promedio en fila: {espera_promedio:.2f} minutos")
        print(f"Tiempo máximo de espera registrado: {espera_max:.2f} minutos")
    else:
        print("No se registraron clientes durante el tiempo de simulación.")

if __name__ == "__main__":
    main()
    
    #EK MEX LIBNI ALEXANDER
    #MEX SANSORES JOSUE ISRAEL
    
