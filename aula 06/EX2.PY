class instrumento:
    def tocar(self):
        print("som")

class violao(instrumento):
    def tocar(self):
        print("vioão tum tum")

class bateria(instrumento):
    def tocar(self):
        print("bateria: pa pum")

class piano(instrumento):
    def tocar(self):
        print("piano: pi pi pi pi")

instrumentos = [violao(), bateria(), piano()]
for instrumento in instrumentos:
    instrumento.tocar()