import matplotlib.pyplot as plt
nombres = ["Ana", "Juan", "Pedro", "Lucia"]
notas = [8, 7, 9, 10]
plt.bar(nombres, notas)
plt.title("Notas de alumnos")
plt.xlabel("Estudiantes")
plt.ylabel("Notas")
plt.show()
print("Gráfico de barras generado correctamente.")
print(plt)