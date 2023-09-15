from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        if isinstance(otro_conjunto, Conjunto):
            for elemento in otro_conjunto.elementos:
                self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        if isinstance(conjunto1, Conjunto) and isinstance(conjunto2, Conjunto):
            nombre_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
            elementos_interseccion = [e for e in conjunto1.elementos if conjunto2.contiene(e)]
            nuevo_conjunto = Conjunto(nombre_resultante)
            nuevo_conjunto.elementos = elementos_interseccion
            return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"

# Ejemplo de uso:
elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

conjunto1 = Conjunto("Set1")
conjunto2 = Conjunto("Set2")

conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

print(conjunto1)
print(conjunto2)

union = conjunto1 + conjunto2
print(union)

interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(interseccion)
