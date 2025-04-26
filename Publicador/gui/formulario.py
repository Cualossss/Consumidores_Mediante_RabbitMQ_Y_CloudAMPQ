import tkinter as tk
from tkinter import messagebox
from modelos.usuario import Usuario
from servicios.servicio_publicador import ServicioPublicador

class FormularioPreRegistro:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Pre-Registro")
        
        self.etiquetas = ['Nombre', 'Apellido', 'Correo', 'Teléfono', 'Programa']
        self.entradas = {}
        
        for idx, etiqueta in enumerate(self.etiquetas):
            tk.Label(root, text=etiqueta).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entrada = tk.Entry(root, width=40)
            entrada.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[etiqueta.lower()] = entrada
        
        self.boton_enviar = tk.Button(root, text="Enviar", command=self.enviar_formulario)
        self.boton_enviar.grid(row=len(self.etiquetas), column=0, columnspan=2, pady=10)

    def enviar_formulario(self):
        datos = {campo: self.entradas[campo].get() for campo in self.entradas}
        
        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        if "@" not in datos['correo']:
            messagebox.showerror("Error", "Ingrese un correo válido.")
            return
        
        usuario = Usuario(
            nombre=datos['nombre'],
            apellido=datos['apellido'],
            correo=datos['correo'],
            telefono=datos['teléfono'],
            programa=datos['programa']
        )
        
        ServicioPublicador.publicar_usuario(usuario)
        messagebox.showinfo("Éxito", "¡Formulario enviado exitosamente!")
        
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
