# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Graficamos los puntos y la línea
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# Título y etiquetas
plt.title("Nominal GDP")
plt.ylabel("Billions of $")

# Añadir etiquetas de cada valor en el eje y y líneas de referencia
for x, y in zip(years, gdp):
    plt.annotate(f"${y:.1f}", (x, y), textcoords="offset points", xytext=(0, 5), ha='center')
    plt.axhline(y, color='blue', linestyle='dashed', linewidth=0.5)

plt.show()
