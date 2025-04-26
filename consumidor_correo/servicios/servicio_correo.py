import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from modelos.usuario import Usuario

class ServicioCorreo:
    @staticmethod
    def enviar_correo(usuario: Usuario):
        remitente = "Tu correo"
        destinatario = "Correo del destinatario"
        contraseña = "Tu contraseña proporcionada por Google(Ver el readme)"

        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = f"Nuevo interés en el programa {usuario.programa}"

        cuerpo = f"""
Hola equipo de admisiones,

El siguiente usuario ha mostrado interés en el programa {usuario.programa}:

Nombre: {usuario.nombre} {usuario.apellido}
Correo: {usuario.correo}
Teléfono: {usuario.telefono}

Por favor, contáctenlo lo antes posible.
"""

        mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

        try:
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()
            servidor.login(remitente, contraseña)
            servidor.send_message(mensaje)
            servidor.quit()
            print("Correo enviado exitosamente.")
        except Exception as e:
            print("Error al enviar correo:", e)
