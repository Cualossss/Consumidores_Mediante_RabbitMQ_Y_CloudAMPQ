# Aplicativo para tomar mensajes mediante RabbitMQ y distribuirlos
##### los mensajes del rabbitmq se distribuiran a una base de datos relacional(sql) y a un consumidor que envia un correo automaticamente.

## COMO USAR
1. Clona o descarga el repositorio en tu workspace.
2. Abre tres terminales **Asegurate que tienes CMD y no Powershell** para ejecutar cada uno de los codigos.
3. Te mueves a la carpeta `cd/nombre de la carpeta` este comando va en el CMD
4. Coloca en cada cmd el siguiente comando `python app.py`

# Q&A
### - ¿Como puedo probar esto en mi computadora?
Muy sencillo, en los apartados del codigo ***servicio_correo.py*** en el segmento de codigo:
```python
class ServicioCorreo:
    @staticmethod
    def enviar_correo(usuario: Usuario):
        remitente = "Tu correo"
        destinatario = "Correo del Remitente"
        contraseña = "Contraseña proporcionada por google"
```

Para obtener la contraseña debes buscar Contraseña de Aplicaciones Google. te pedira la contraseña de tu correo y tranquilo porque es un sitio oficial de Google.
Reemplazas todo en ese segmento de codigo y creo que es todo lo necesario (Pido disculpas si no es asi)
