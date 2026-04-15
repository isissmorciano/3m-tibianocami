import matplotlib.pyplot as plt
import numpy as np

#es1

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])


plt.figure(figsize=(8, 5))
plt.plot(xpoints, ypoints)
plt.title('Grafico a Linea Semplice')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('grafico_linea_semplice.png')


#es2
ypoints = np.array([3, 8, 1, 10])

plt.figure(figsize=(8, 5))
plt.plot(ypoints, linestyle='dotted')
plt.title('Grafico a Linea Punteggiata')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('grafico_linea_punteggiata.png')


#es3
categorie = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile']
valori = [10, 15, 7, 12]

plt.figure(figsize=(8, 5))
plt.bar(categorie, valori, color='skyblue')
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('grafico_a_barre.png')



#es4
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 15, 25])

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title('Grafico a Linea')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('grafico_linea.png')