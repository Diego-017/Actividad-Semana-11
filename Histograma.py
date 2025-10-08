import matplotlib.pyplot as plt

tiempos = [15, 15, 20, 30, 40, 45, 60, 60, 80, 100]

# Crear el histograma
plt.figure(figsize=(8, 6))
plt.hist(
    tiempos,
    bins=8,                # número de divisiones (puedes ajustar a gusto)
    color='#1B5F6E',        # color de las barras
    edgecolor='black'      # borde negro
)

# Títulos y etiquetas
plt.title('Tiempo para llegar a la universidad (muestra actualizada)')
plt.xlabel('Minutos')
plt.ylabel('Cantidad de personas')

# Mostrar el gráfico
plt.show()
