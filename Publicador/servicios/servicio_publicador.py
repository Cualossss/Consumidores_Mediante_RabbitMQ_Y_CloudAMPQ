from utils.rabbitmq import RabbitMQ
from modelos.usuario import Usuario

class ServicioPublicador:
    
    @staticmethod
    def publicar_usuario(usuario: Usuario):
        mensaje = usuario.a_json()
        RabbitMQ.publicar(mensaje)
