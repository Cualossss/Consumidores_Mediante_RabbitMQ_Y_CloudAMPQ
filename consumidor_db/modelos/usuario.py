from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    apellido: str
    correo: str
    programa: str
    telefono: str