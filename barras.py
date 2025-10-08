# Hazme un grafico de barra usando matplotlib con la respuesta de la pregunta ¿Cuántas tazas de café tomas al día? con una muestra de 10 personas.
import matplotlib.pyplot as plt

# Datos
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
tazas = [1, 2, 3, 4, 2, 1, 3]

# Crear gráfico de barras
plt.bar(dias, tazas)

# Añadir título y etiquetas
plt.title('Tazas de café consumidas por día')
plt.xlabel('Días de la semana')
plt.ylabel('Número de tazas')

# Mostrar gráfico

plt.show()