from TP_ArbolYListas.NodoLista import NodoLista
 # coding=utf8

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        
    '''FUNCION PARA CONSULTAR SI ESTA VACIA
    LA LISTA'''    
    def estaVacia(self):
        return self.primero == None
    
    
    def append(self, dato):
        nuevoNodo = NodoLista(dato)
        if self.estaVacia():
            self.primero = nuevoNodo
        else:
            self.primero.append(nuevoNodo)
    
    '''FUNCION QUE AGREGA LOS ELEMENTOS DE FORMA ORDENADA DE MAYOR A MENOS'''        
    def appendOrd(self, dato):
        nuevoNodo = NodoLista(dato)
        '''SI ESTA VACIA EL PRIMER NODO ES EL QUE SE ENVIA'''
        if self.estaVacia():
            self.primero = nuevoNodo
            '''SINO ESTA VACIA LLAMO A LA RECURSIVA PARA AGREGAR EL NODO'''
        else:
            self.primero.appendOrd(nuevoNodo)
                
            
        
            
    
    '''FUNCION QUE DEVUELVE LA CANTIDAD DE
    NODOS DE LA LISTA. SI ESTA VACIA DEVUELVE 
    0 SINO LLAMA A LA FUNCION LEN DE NODO 
    LISTA'''        
    def len(self):
        cant = 0
        if not self.estaVacia():
            cant = self.primero.len()
        return cant
    
    '''CONSULTO QUE LA POSICION SEA MAYOR IGUAL A 0,
        QUE LA POSICION ENVIADA SEA MENOR QUE EL TAMANIO DE LA LISTA
        Y QUE LA LISTA NO ESTE VACIA'''
    def validarPosicion(self, pos):
        return 0<= pos < self.len() and not self.estaVacia()
    
    '''LEE EL DATO SEGUN LA POSICION SOLICITADA'''
    def getDato(self, pos):
        if self.validarPosicion(pos):
            return self.primero.getDato(pos)
        else:
            raise Exception("La posicion es invalida ")
    
    '''FUNCION QUE ELIMINA UN NODO EN LA LISTA EN LA POSICION ENVIADA
    SI LA POSICION EN LA PRIMERA SE ELIMINA Y EL NODO RAIZ PASA A SER EL SIGUIENTE
    SINO ES LA POSICION 0 SE LLAMA A LA FUNCION RECURSIVA DE NODO LISTA'''    
    def delete(self, pos):
        if self.validarPosicion(pos):
            if pos == 0:
                self.primero = self.primero.siguiente
            else:
                self.primero.delete(pos)
        else:
            raise Exception("La posicion es invalida ")
    
    '''BUSCA SI UN DATO SE ENCUENTRA EN LA LISTA'''
    def buscarDato(self, datoABuscar):
        if not self.estaVacia():
            return self.primero.buscarDato(datoABuscar)
    
    '''ELIMINA UN DATO EN LA LISTA, PASANDO EL DATO QUE SE DESEA ELIMINAR'''    
    def eliminarDato(self, datoAEliminar):
        if not self.estaVacia():
            if self.primero.dato == datoAEliminar:
                if self.primero.siguiente == None:
                    self.primero = None
                else:
                    self.primero = self.primero.siguiente
            else:
                self.primero.eliminarDato(datoAEliminar)
        
        
    def recPre(self):
        if not self.estaVacia():
            self.primero.recPre()
            
    def clonar(self):
        listaClon = ListaEnlazada()
        if not self.estaVacia():
            self.primero.clonar(listaClon)
        return listaClon     
    
    def __repr__(self):
        out = "["
        aux = self.primero
        while aux != None:
            out +=  str(aux.dato) + " , " 
            aux = aux.siguiente
        out += " ]"
        return out  
    
    def deleteAll(self):
        if not self.estaVacia():
            if self.len() == 1:
                self.delete(0)
            else:
                self.primero.deleteAll()
                
            
        