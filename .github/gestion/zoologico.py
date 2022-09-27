from gestion.zona import Zona
class Zoologico:
    def __init__(self,nombre,ubicacion):
            self._nombre=nombre
            self._ubicacion=ubicacion
            self._zona=[]
        
    
    def agregarZonas(self,zona):
        self._zona.append(zona)


    def cantidadTotalAnimales(self):
        count=0
        for i in self._zona:
            count+=i.cantidadAnimales()
        return count

    #getter and setters methods

    def setNombre(self,nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    def getUbicacion(self):
        return self._ubicacion

    def setZona(self,zona):
        self._zona=zona
    def getZona(self):
        return self._zona