    
class Animal:
    def __init__(self,name,especie,edad):
        self.name = name
        self.especie = especie
        self.edad = edad
        self.energia = 50

    def presentarse(self):
        text= f"Hola,soy{self.name},|Especie:({self.especie}),|Edad:{self.edad}ã"
        print(text)

    def comer(self,gramos:int):
        self.energia += (gramos//10)
        if self.energia > 100:
            self.energia = 100
            print("!! Para coche ¡¡")
        print(f"Comiendo.... energía nueva: {self.energia}")
        
    def jugar(self):
        self.energia -= 20
        if self.energia < 0:
            self.energia = 0
            print("Es hora de dormir")
        print(f"jugando.... energía nueva: {self.energia}")

    def dormir(self):
        self.energia += 30
        if self.energia > 100:
            self.energia = 100
            print("¡¡Deja de chingar!!")
        print(f"Durmiendo.... energía nueva: {self.energia}")  
        

    