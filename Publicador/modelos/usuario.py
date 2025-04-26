from dataclasses import dataclass, asdict
import json

@dataclass
class Usuario:
    nombre: str
    apellido: str
    correo: str
    programa: str
    telefono: str

    def a_json(self) -> str:
        return json.dumps(asdict(self))
