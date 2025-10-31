print("Hello, World!")

class Perro:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def ladrar(self):
		return f"{self.nombre} dice: ¡Guau!"
mi_perro = Perro("Firulais", 3)
print(mi_perro.ladrar())