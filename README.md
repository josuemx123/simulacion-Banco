# simulacion-Banco
El programa permite representar la llegada de diferentes clientes al banco y simular el tiempo que esperan en una fila antes de ser atendidos por un cajero. También calcula estadísticas sobre la atención de los clientes.

##  ¿Cuál es el objetivo?

El objetivo del programa es *analizar el funcionamiento de un sistema de cajeros automáticos mediante una simulación*.

Con los resultados obtenidos se puede conocer:

* Cuántos clientes fueron atendidos.
* Cuánto tiempo esperaron los clientes en la fila.
* Cuál fue el tiempo promedio de espera.
* Cuál fue el tiempo máximo de espera.

Esto permite analizar si la cantidad de cajeros disponibles es suficiente para atender a los clientes de manera eficiente.

## ¿Cómo funciona el algoritmo?

El programa funciona mediante una simulación de eventos discretos.

El algoritmo realiza los siguientes pasos:

1. El usuario introduce el número de cajeros disponibles.
2. Se introduce el tiempo promedio entre las llegadas de los clientes.
3. Se introduce el tiempo promedio que tarda una transacción.
4. Se establece el tiempo total que durará la simulación.
5. Se crea un entorno de simulación utilizando SimPy.
6. Se crea un recurso que representa los cajeros disponibles.
7. Se generan clientes de manera aleatoria durante la simulación.
8. Cada cliente solicita un cajero.
9. Si todos los cajeros están ocupados, el cliente espera en una fila.
10. Cuando un cajero queda disponible, el cliente comienza su transacción.
11. Se calcula y registra el tiempo que el cliente esperó.
12. Se genera aleatoriamente la duración de la transacción.
13. Cuando termina la transacción, el cliente sale del sistema.
14. Al finalizar la simulación, se muestran las estadísticas obtenidas.

El programa utiliza una *distribución exponencial* mediante random.expovariate() para generar tanto el tiempo entre llegadas de clientes como la duración de las transacciones.

##  ¿Qué datos recibe?

El programa solicita cuatro datos al usuario:

### Número de cajeros disponibles

Indica cuántos cajeros pueden atender clientes simultáneamente.

Ejemplo:

text
2


### Tiempo promedio entre llegadas de clientes

Indica cada cuánto tiempo, en promedio, llega un nuevo cliente al banco.

Ejemplo:

text
1.5 minutos


### Tiempo promedio de transacción

Indica cuánto tiempo tarda, en promedio, un cliente en realizar su operación.

Ejemplo:

text
3.0 minutos


### Tiempo total de simulación

Indica cuánto tiempo se ejecutará la simulación.

Ejemplo:

text
45 minutos


## ¿Qué resultados produce?

Al terminar la simulación, el programa muestra:

* *Total de clientes atendidos:* cantidad de clientes que terminaron su transacción.
* *Tiempo de espera promedio en fila:* promedio del tiempo que los clientes esperaron antes de utilizar un cajero.
* *Tiempo máximo de espera registrado:* mayor tiempo que tuvo que esperar un cliente en la fila.

Por ejemplo, el resultado puede ser:

text
--- RESULTADOS DEL SISTEMA SIMULADO ---
Total de clientes atendidos: 25
Tiempo de espera promedio en fila: 2.34 minutos
Tiempo máximo de espera registrado: 6.72 minutos


Los resultados pueden cambiar en cada ejecución porque los tiempos de llegada y de transacción se generan aleatoriamente.

El programa solicitará los datos necesarios para iniciar la simulación.

## Librerías utilizadas

El programa utiliza las siguientes librerías:

### SimPy

SimPy es una librería de Python utilizada para realizar *simulaciones de eventos discretos*. En este programa se utiliza para crear el entorno de simulación y controlar los recursos disponibles, en este caso los cajeros.

### Random

random es una librería incluida en Python que permite generar valores aleatorios. En este programa se utiliza random.expovariate() para generar los tiempos aleatorios de llegada de los clientes y de duración de las transacciones.

## Estructura del programa

El programa está dividido principalmente en tres funciones:

* cliente(): representa el comportamiento de cada cliente.
* generador_clientes(): genera nuevos clientes durante la simulación.
* main(): solicita los datos al usuario, inicia la simulación y muestra los resultados.

De esta manera, el programa permite representar el comportamiento de una fila de clientes que utilizan un número determinado de cajeros y obtener estadísticas sobre el rendimiento del sistema.
