class Circulo:

    raio : float


    def __init__(self, raio:float):
        self.raio = raio if raio > 10 else 10
        # ou
        self.raio = 10 if raio < 10 else raio 



# instancia

circulo = Circulo(3.14 ,10)
