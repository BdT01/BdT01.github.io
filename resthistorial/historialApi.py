#!usr/bin/env python3

'''
Implementacion del servicio RESTHISTORIAL
'''


class Historial:
    def __init__(self, nombre="", id=0, fecha="", hora="", alergias=[], medicamentos=[], enfermedades=[], cirugias=[], otros=[], tratamientos=[], problemas=[], observaciones=[]):
        self.nombre = nombre
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.alergias = alergias
        self.enfermedades = enfermedades
        self.medicamentos = medicamentos
        self.cirugias = cirugias
        self.otros = otros
        self.tratamientos = tratamientos
        self.problemas = problemas
        self.observaciones = observaciones

    def get_historial(self):
        return {"nombre": self.nombre, "id": self.id, "fecha": self.fecha, "hora": self.hora, "alergias": self.alergias,
                "enfermedades": self.enfermedades, "medicamentos": self.medicamentos, "cirugias": self.cirugias, "otros": self.otros,
                "tratamientos": self.tratamientos, "problemas": self.problemas, "observaciones": self.observaciones}

    def add_tratamiento(self, tratamiento):
        self.tratamiento.append(tratamiento)

    def add_problemas(self, problemas):
        self.problemas.append(problemas)

    def add_observaciones(self, observaciones):
        self.observaciones.append(observaciones)

    def add_alergias(self, alergias):
        self.alergias.append(alergias)

    def add_enfermedades(self, enfermedades):
        self.enfermedades.append(enfermedades)

    def add_medicamentos(self, medicamentos):
        self.medicamentos.append(medicamentos)

    def add_cirugias(self, cirugias):
        self.cirugias.append(cirugias)

    def add_otros(self, otros):
        self.otros.append(otros)
