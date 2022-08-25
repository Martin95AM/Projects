from tkinter import messagebox

class Tema:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)
        

    def notificar(self, titulo, mensaje):
        for observador in self.observadores:
            observador.update(titulo, mensaje)    

class ConcreteObservador:
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)
        

    def update(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
        
         
