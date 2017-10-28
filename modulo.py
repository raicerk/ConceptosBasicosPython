class Autentificacion():
	
	usuario = ""
	contrasena = ""

	def Login(self):
		if self.usuario == "juan" and self.contrasena == "holiwis":
			return True
		else:
			return False

aut = Autentificacion()
aut.usuario = "juan"
aut.contrasena = "holiwis"
print aut.Login()