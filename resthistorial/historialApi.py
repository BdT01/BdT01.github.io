#!usr/bin/env python3

'''
Implementacion del servicio RESTHISTORIAL
'''

class Historial:
    def __init__(self, nombre="", id=0, fecha="", hora="", antecedentes={'Alergias': [], 'Enfermedades': [], 'Medicamentos': [], 'Cirugias': [], 'Otros': []}, tratamiento= [], problemas= [], observaciones= []):
        self.nombre = nombre
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.antecedentes = antecedentes
        self.tratamiento = tratamiento
        self.problemas = problemas
        self.observaciones = observaciones

    def get_historial(self):
        return self
    
    def add_antecendentes(self, antecedentes, tipo):
        self.antecedentes[tipo].append(antecedentes)
    
    def add_tratamiento(self, tratamiento):
        self.tratamiento.append(tratamiento)
    
    def add_problemas(self, problemas):
        self.problemas.append(problemas)
    
    def add_observaciones(self, observaciones):
        self.observaciones.append(observaciones)
