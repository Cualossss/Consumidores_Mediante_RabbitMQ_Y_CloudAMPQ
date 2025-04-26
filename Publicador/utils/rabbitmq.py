import pika

class RabbitMQ:
    URL_CONEXION = 'amqps://hnmrybcu:Q4MMohjaHfaIWjTbxmsMaSWFM8Inmagj@moose.rmq.cloudamqp.com/hnmrybcu'  # Tu URL real

    COLAS = ['pre_registro_db', 'pre_registro_correo']

    @staticmethod
    def publicar(mensaje: str):
        parametros = pika.URLParameters(RabbitMQ.URL_CONEXION)
        conexion = pika.BlockingConnection(parametros)
        canal = conexion.channel()

        for cola in RabbitMQ.COLAS:
            canal.queue_declare(queue=cola, durable=True)
            canal.basic_publish(
                exchange='',
                routing_key=cola,
                body=mensaje,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Persistente
                )
            )
        
        conexion.close()
