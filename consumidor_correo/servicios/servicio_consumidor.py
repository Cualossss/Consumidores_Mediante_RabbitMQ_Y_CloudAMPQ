import json
from utils.rabbitmq import RabbitMQ
from modelos.usuario import Usuario
from servicios.servicio_correo import ServicioCorreo

class ServicioConsumidor:
    @staticmethod
    def iniciar():
        conexion, canal = RabbitMQ.conectar()

        def callback(ch, method, properties, body):
            print("[x] Mensaje recibido:", body.decode())
            datos = json.loads(body.decode())
            usuario = Usuario(**datos)
            ServicioCorreo.enviar_correo(usuario)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        canal.basic_consume(queue=RabbitMQ.COLA, on_message_callback=callback)
        print(' [*] Esperando mensajes para enviar correos. Presiona CTRL+C para salir.')
        canal.start_consuming()
