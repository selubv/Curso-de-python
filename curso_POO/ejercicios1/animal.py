class Animal:
    def __init__(self, especie, sonido):
        self.especie = especie
        self.sonido = sonido
        
    def emitir_sonido(self):
        print(f"The {self.especie} says {self.sonido}!")

# Usage example
dog = Animal("dog", "woof")
cat = Animal("cat", "meow")

dog.emitir_sonido()
cat.emitir_sonido()