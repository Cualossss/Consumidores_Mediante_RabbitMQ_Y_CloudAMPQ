import json
from utils.rabbitmq import RabbitMQ
from modelos.usuario import Usuario
from servicios.servicio_base_datos import ServicioBaseDatos

class ServicioConsumidor:
    @staticmethod
    def iniciar():
        ServicioBaseDatos.inicializar_bd()
        conexion, canal = RabbitMQ.conectar()

        def callback(ch, method, properties, body):
            print("[x] Mensaje recibido:", body.decode())
            datos = json.loads(body.decode())
            usuario = Usuario(**datos)
            ServicioBaseDatos.guardar_usuario(usuario)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        canal.basic_consume(queue=RabbitMQ.COLA, on_message_callback=callback)
        print(' [*] Esperando mensajes. Para salir presiona CTRL+C')
        canal.start_consuming()