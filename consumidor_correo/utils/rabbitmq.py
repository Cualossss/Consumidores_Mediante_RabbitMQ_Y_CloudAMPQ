import pika

class RabbitMQ:
    URL_CONEXION = 'amqps://hnmrybcu:Q4MMohjaHfaIWjTbxmsMaSWFM8Inmagj@moose.rmq.cloudamqp.com/hnmrybcu'
    COLA = 'pre_registro_correo'

    @staticmethod
    def conectar():
        parametros = pika.URLParameters(RabbitMQ.URL_CONEXION)
        conexion = pika.BlockingConnection(parametros)
        canal = conexion.channel()
        canal.queue_declare(queue=RabbitMQ.COLA, durable=True)
        return conexion, canal
