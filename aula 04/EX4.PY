class sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
    def get_temperatura(self):
        return self.__temperatura
    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("erro: temperatura fora do limite físico do sensor")

    def status(self):
        if -50 <= self.__temperatura <= 80:
            return "normal"
        elif 81 <= self.__temperatura <= 120:
            return "alerta"
        elif self.__temperatura > 120:
            return "critico"

s = sensor(25)

s.set_temperatura(30)
print(f"temperatura: {s.get_temperatura()} status: {s.status()}")
s.set_temperatura(95)
print(f"temperatura: {s.get_temperatura()} status: {s.status()}")
s.set_temperatura(130)
print(f"temperatura: {s.get_temperatura()} status: {s.status()}")
s.set_temperatura(160)