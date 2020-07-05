

class NodoLista:
    def __init__(self, dato = None):
        self.dato=dato
        self.siguiente = None
        
    '''FUNCION PARA CONSULTAR SI EL
    NODO TIENE SIGUIENTE'''    
    def tieneSiguiente(self):
        return self.siguiente != None
    
    '''FUNCION RECURSIVA QUE AniADE UN 
    NODO A LA LISTA'''
    def append(self, nuevoNodo):
        if self.tieneSiguiente():
            self.siguiente.append(nuevoNodo)
        else:
            self.siguiente = nuevoNodo
            
    def appendOrd(self, nuevoNodo):
        if self.tieneSiguiente():
            if nuevoNodo.dato < self.siguiente.dato:
                nuevoNodo.siguiente = self.siguiente
                self.siguiente = nuevoNodo
                
                 
                         
            else:
                self.siguiente.appendOrd(nuevoNodo)
        else:
            self.siguiente = nuevoNodo
    
    '''FUNCION RECURSIVA QUE SUMA LA
    CANTIDAD DE NODOS DE LA LISTA'''       
    def len(self):
        cant = 1
        if self.tieneSiguiente():
            cant += self.siguiente.len()
        return cant
    
    def getDato(self, getPos, actPos = 0):
        dato = None
        if actPos == getPos:
            dato = self.dato
        else:
            dato = self.getDato(getPos, actPos +1)
        return dato
    
    def buscarDato(self, datoABuscar, actPos = 0):
        
        encontrado = None
        if datoABuscar == self.dato:
            encontrado = True
        else:
            if self.tieneSiguiente():
                encontrado = self.siguiente.buscarDato(datoABuscar, actPos + 1)
        return  encontrado
    
    def eliminarDato(self, datoABuscar, actPos = 0):  
        if datoABuscar == self.dato:        
            self.delete(actPos)
        else:
            if self.tieneSiguiente():
                self.siguiente.eliminarDato(datoABuscar, actPos + 1)
          
            
    def delete(self, deletePos, actPos = 0):
        
        if actPos == deletePos - 1:
            self.siguiente = self.siguiente.siguiente
        else:
            dato = self.delete(deletePos, actPos +1)
            
    def recPre(self):
        print(self.dato)
        if self.tieneSiguiente():
            self.siguiente.recPre()
            
    def clonar(self, listaClon):
        listaClon.append(self.dato)
        if self.tieneSiguiente():
            self.siguiente.clonar(listaClon)
        