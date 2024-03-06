from enum import StrEnum


class UnidadMedida(StrEnum):
    GRAMO = "gr"
    KILOGRAMO = "kg"
    LITRO = "l"
    MILILITRO = "ml"
    TAZA = "taza"
    CUCHARADA = "cda"
    CUCHARADITA = "cdita"
    UNIDAD = "unidad"

    @classmethod
    def list(cls) -> list[str]:
        return list(map(lambda c: c.value, cls))


# TODO: Implementar la clase Ingrediente
class Ingrediente:
    def __init__(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        self.alimento: str = alimento
        self.cantidad: float = cantidad
        self.unidad: UnidadMedida = unidad


    def __str__(self) -> str:
        return f"{self.cantidad} - {self.unidad}> - <{self.alimento}>"         ####

# TODO: Implementar la clase Receta
class Receta:
    def __init__(self, nombre: str, description: str, etiquetas: None):
        self.nombre: str = nombre
        self.ingredientes: list[Ingrediente] = []
        self.description: str = description

        self.etiquetas: list[str] = [etiquetas]
        if self.etiquetas == None:         #####
            lista = []


    def agregar_ingrediente(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        ingrediente = Ingrediente()
        self.ingredientes.append(ingrediente)


    def __str__(self):
        return f"Receta {self.no}"

# TODO: Implementar la clase Chef

class Chef:
    def __init__(self):
        pass


    def registrar_receta(self, nombre: str, ingredientes: list(str, float),()):
        pass


    def buscar_receta(self):
        pass
