# Representacion de horas de sueño de 10 personas 
import matplotlib.pyplot as plt
import numpy as np
import random
# Datos
personas = [f'Persona {i+1}' for i in range(10)]
horas_dormidas = [random.randint(4, 10) for _ in range(10)]
# Crear la gráfica de líneas
plt.plot(personas, horas_dormidas, marker='o', linestyle='-', color='b')
plt.title('Horas de Sueño Anoche de 10 Personas')
plt.xlabel('Personas')
plt.ylabel('Horas Dormidas')
plt.ylim(0, 12)
plt.grid(True)
# Mostrar la gráfica
plt.show()
# Guardar la gráfica como imagen
plt.savefig('horas_dormidas.png')