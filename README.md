## Ejercicio - RaceCar class en Python

Es necesario crear una clase RaceCar que contemple el nombre del carro y los tiempos de cada lap (vuelta) que ha registrado. También hay que crear una clase Team que permita formar equipos de carros. 

Restricciones:

- Se necesita medir para cada carro la velocidad promedio de acuerdo a 
cinco laptimes registrados. 
- El lapdistance de la pista es de 100 metros. Esta 
distancia es importante que la consideres constante en el programa.
- Hay que considerar un método que retorne la velocidad promedio de cada carro.
- Hay que considerar un método que muestre el nivel de cada carro dependiendo de su velocidad (Principiante, Normal, Medio, Avanzado):

```python
"""Ejemplo de nivel del racecar de acuerdo a velocidad"""

      |  Velocidad |      Nivel     |
      -------------------------------
        15..17 	    "Avanzado"
        12...14.99  "Medio"
        10...11.99  "Normal"
        9..9.99     "Principiante"

```

- Crea un método en team que regrese el promedio de velocidad del equipo.
- Hay que tomar en cuenta una función que permita buscar si existe un determinado carro en un equipo. 

```python
class RaceCar:


  """método para obtener velocidad promedio"""
  ...

  
  """método que muestra nivel de cada race car"""
  ...
  


class Team:


  """método para agregar nuevo race car"""
  ...


  """método para calcular promedio de velocidad del equipo"""
  ...



"""función para buscar racecar en equipo"""
...

```

```python
"""Ejemplo de salida"""

#calculate average speed of racecar in m/s
print(car1.average_speed)
#>> 9.5 

#calculate average speed of team in m/s
print(team_one.average_speed_of_team)
#>> 23.34 

#search race car in team
print(search("Power", team_one))
#>> "Power is a racer"

```

```ruby
$ test_racecar.py
```

