import matplotlib.pyplot as plt

# Datos obtenidos (respuestas de 10 personas)
redes = ['Instagram', 'Facebook', 'TikTok', 'WhatsApp']
cantidades = [1, 1, 7, 1]  # número de personas por red

# Colores personalizados (similares al gráfico original)
colores = ["#A72791", "#1D0DB0", "#686765", "#0BA534"]

# Crear gráfico de pastel
plt.figure(figsize=(7, 7))
plt.pie(
    cantidades,
    labels=redes,
    colors=colores,
    autopct='%1.0f%%',  # porcentaje sin decimales
    startangle=90,
    shadow=True,
    wedgeprops={'edgecolor': 'white'}
)

# Título
plt.title('¿Qué red social usas más? (10 respuestas)', fontsize=13, fontweight='bold')

# Mostrar gráfico
plt.show()
