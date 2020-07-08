from TP_ArbolYListas.NodoArbol import NodoArbol
from TP_ArbolYListas.ListaEnlazada import ListaEnlazada
class ArbolBuscador:
  def __init__(self):
    self.raiz = None
  
  '''FUNCION PARA SABER SI EL ARBOL ESTA VACIO'''
  def estaVacio(self):
    return self.raiz == None

  '''RECORRE EL ARBOL EN FORMA DE PREORDEN.
  PRIMERO IMPRIME EL VALOR'''
  def preOrden(self):
    if not self.estaVacio():
      self.raiz.preOrden()
    else:
      print("El Arbol esta vacio")

  def inOrden(self):
    if not self.estaVacio():
      self.raiz.inOrden()
    else:
      print("El Arbol esta vacio")

  def postOrden(self):
    if not self.estaVacio():
      self.raiz.postOrden()
    else:
      print("El Arbol esta vacio")
  
  '''FUNCION QUE BUSCA EL VALOR MAXIMO DEL ARBOL'''    
  def maximo(self):
    maximo = None 
    if not self.estaVacio():
      maximo = self.raiz.buscaMaximo().dato
    return maximo

  '''DEVUELVE LA ALTURA DE UN NODO'''
  def altura(self):
    alt = 0
    if not self.estaVacio():
      alt = self.raiz.altura()
    return alt


  def eliminar(self, palabra):
    if not self.estaVacio():
      if palabra == self.raiz.palabra:
        if self.raiz.grado() == 2:
          nodoPred = self.raiz.predecesor()
          self.eliminar(nodoPred.palabra)
          nodoPred.izquierda = self.raiz.izquierda
          nodoPred.derecha = self.raiz.derecha
          self.raiz = nodoPred
        elif self.raiz.tieneIzquierda():
          self.raiz = self.raiz.izquierda
        elif self.raiz.tieneDerecha():
          self.raiz = self.raiz.derecha
        else:
          self.raiz = None
      else:
        self.raiz.eliminar(palabra)
        
  def nivelALista(self, nivel):
      listaNivel = []
      if not self.estaVacio():
          self.raiz.nivelALista(nivel, listaNivel)
      return listaNivel
      
  def existeNodo(self, palabraBuscar):
    existe = None
    '''SI EL ARBOL NO ESTA VACIO BUSCO LA PALABRA EN TODOS LOS NODOS
    PARA VER SI SE ENCUNTRA'''
    if not self.estaVacio():
        existe = self.raiz.existeNodo(palabraBuscar)
    return existe
  
  '''FUNCION QUE AGREGA LA DIRECCION WEB A LA LISTA DEL NODO'''      
  def agregarDirWeb(self, lista, direccionWeb):
    lista.append(direccionWeb)
            

  def insertarPalabra(self, palabraNueva, direccionWeb):
    '''CONSULTO SI LA PLABRA QUE SE DESEA AGREGAR AL ARBOL EXISTE'''
    nodoExistente =  self.existeNodo(palabraNueva)
    '''SINO EXISTE AGREGO LA PALABRA AL ARBOL JUNTO CON LA LISTA DE LA 
    PAGINA WEB'''
    if nodoExistente == None:
        '''GENERO LA LISTA NUEVA Y AGREGO LA DIRECCION WEB'''
        listaNueva = ListaEnlazada()
        self.agregarDirWeb(listaNueva, direccionWeb)
        nuevoNodo = NodoArbol(listaNueva, palabraNueva )
        if self.estaVacio():
            self.raiz = nuevoNodo
        else:
            self.raiz.insertar(nuevoNodo)
    else:
        '''SI EL NODO YA SE ENCONTRABA EN EL ARBOL CONSULTO
        SI EN LA LISTA QUE POSEE SE ENCUENTRA LA PAGINA WEB'''
        if not nodoExistente.listaPaginas.buscarDato(direccionWeb):
            self.agregarDirWeb(nodoExistente.listaPaginas, direccionWeb)
        '''else:
            raise Exception("La palabra y la direccion ya se encuentran en el buscador ")'''
  
  '''FUNCION QUE AGREGA UNA PAGINA WEB RECIBIENDO POR PARAMETRO UNA LISTA DE PALABRAS'''      
  def insertarPagina(self, listaDePalabras, paginaWeb, pos = 0):
      if not listaDePalabras.estaVacia() and pos < listaDePalabras.len():
          self.insertarPalabra(listaDePalabras.getDato(pos), paginaWeb)
          pos+=1
          self.insertarPagina(listaDePalabras, paginaWeb, pos)
  
  '''FUNCION QUE COMPARA ENTRE DOS LISTAS LAS SIMILITUDES. ESTO SE REALIZA PARA QUE EN LA LISTA RESULTANTE NO
  SOLO SE MUESTREN LAS PAGINAS QUE SE ENCUENTRAN EN LAS DOS LISTAS'''        
  def buscarSimilitudes(self, listaPaginas, paginasEncontradas, listaSimilitud = ListaEnlazada(), pos=0): 
      if pos < paginasEncontradas.len():
          pagina = paginasEncontradas.getDato(pos)
          if listaPaginas.buscarDato(pagina):
              listaSimilitud.append(pagina)
          pos+=1
          self.buscarSimilitudes(listaPaginas, paginasEncontradas, listaSimilitud, pos)
      return listaSimilitud
      
      
       
  '''FUNCION QUE RECIBIENDO UNA LISTA DE PALABRAS, DEVUELVE LAS PAGINAS DONDE SE ENCUENTRAN ESTAS PALABRAS'''
  def buscarPalabras(self, listaPalabras, paginasEncontradas = ListaEnlazada(), vacio = False, pos = 0): 
      if pos < listaPalabras.len() and vacio == False: 
          nodoExistente =  self.existeNodo(listaPalabras.getDato(pos))
          if nodoExistente != None:
              listaPaginas = nodoExistente.listaPaginas.clonar()
              if not paginasEncontradas.estaVacia():
                  listaSimilitud = ListaEnlazada()
                  paginasEncontradas = self.buscarSimilitudes(listaPaginas, paginasEncontradas, listaSimilitud)
                  if paginasEncontradas.estaVacia():
                      vacio = True
              else:
                  paginasEncontradas = listaPaginas.clonar()
          '''listaPalabras.delete(0)'''
          pos +=1
          self.buscarPalabras(listaPalabras, paginasEncontradas, vacio, pos)
      return paginasEncontradas
  
  '''DEVUELVE LAS PALABRAS QUE CONTIENE ESA PAGINA WEB'''        
  def palabrasDePagina(self, dirWeb):
      if not self.estaVacio():
          listaPalabras = ListaEnlazada()
          return self.raiz.palabrasDePagina(dirWeb, listaPalabras)
      else:
          print("El Arbol esta vacio")
  
  '''ELIMINA UNA PALABRA, POR LO QUE ELIMINA EL NODO DEL ARBOL QUE CONTENGA LA PALABRA INDICADA'''        
  def eliminarPalabra(self, palabra):
      self.eliminar(palabra)
  
  '''ELIMINA LA PAGINA INDICADA EN TODO EL ARBOL'''    
  def eliminarPagina(self, pagina):
      if not self.estaVacio():
          return self.raiz.eliminarPagina(pagina)
      else:
          print("El Arbol esta vacio")
  
  '''DEVUELVE SI EL ARBOL ESTA BALANCEADO
  1_ CONSULTA SI TIENE IZQUIERDO Y DERECHO PARA CONSULTAR LA ALTURA DE AMBOS
  2_ CALCULA QUE LA DIFERENCIA ENTRE AMBAS ALTURAS NO SEA SUPERIOR A 1'''        
  def estaBalanceado(self):
      altIzq = 0
      altDer = 0
      balanceado = False
      if self.raiz.izquierda != None:
          altIzq = self.raiz.izquierda.altura()
      if self.raiz.derecha != None:
          altDer = self.raiz.derecha.altura()
      if altIzq > altDer:
          balanceado =  (altIzq - altDer) <= 1
      else:
          balanceado =  (altDer - altIzq) <= 1
      return balanceado
      
  '''FUNCION QUE DEVUELVE UNA LISTA DE PALABRAS, ESTAS DEBEN TENER IGUAL O MAYOR CANTIDAD DE CARACTERES
  QUE LA CANTIDAD RECIBIDA'''        
  def cantidadTotalPalabras(self, cantidad):
      if not self.estaVacio():
          listaPalabras = ListaEnlazada()
          return self.raiz.cantidadPalabras(cantidad, listaPalabras)
      else:
          print("El Arbol esta vacio")
          
  '''FUNCION QUE COMPARA QUE ENTRE DOS LISTAS NO SE REPITAN VALORES '''
  def buscarPaginasNoRepetidas(self, listaPaginas, paginasEncontradas): 
      if not paginasEncontradas.estaVacia():
          pagina = paginasEncontradas.getDato(0)
          if not listaPaginas.buscarDato(pagina):
              listaPaginas.append(pagina)
          paginasEncontradas.delete(0)
          self.buscarSimilitudes(listaPaginas, paginasEncontradas)
      return listaPaginas
  
  '''RECIBE UNA LISTA DE PALABRAS Y BUSCA LAS PAGINAS DE CADA UNA'''
  def buscarPaginas(self, listaPalabras, paginasEncontradas = None): 
      if not listaPalabras.estaVacia(): 
          nodoExistente =  self.existeNodo(listaPalabras.getDato(0))
          listaPaginas = nodoExistente.listaPaginas.clonar()
          if paginasEncontradas != None:
              paginasEncontradas = self.buscarPaginasNoRepetidas(listaPaginas, paginasEncontradas)
          else:
              paginasEncontradas = listaPaginas.clonar()
          listaPalabras.delete(0)
          paginasEncontradas = self.buscarPaginas(listaPalabras, paginasEncontradas)
      return paginasEncontradas
  
  '''FUNCION QUE DEVUELVE UNA LISTA CON LAS PAGINAS QUE SE ENCUENTRAN EN EL NIVEL RECIBIDO '''
  def paginasEnNivel(self, nivel):
      palabras = self.nivelALista(nivel)
      listaPalabras = ListaEnlazada()
      for palabra in palabras:
          listaPalabras.append(palabra)
      return self.buscarPaginas(listaPalabras)
  
  '''DEVUELVE UNA LISTA DE PALABRAS, DONDE LA CANTIDAD DE PAGINAS QUE CONTENGA SEA MAYOR O IGUAL QUE LA CANTIDAD RECIBIDA'''
  def cantidadPalabrasMasUsadas(self, cantPaginas):
      if not self.estaVacio():
          listaPalabras = ListaEnlazada()
          return self.raiz.cantidadPalabrasConPaginas(cantPaginas, listaPalabras)
      else:
          print("El Arbol esta vacio")
  
  '''DEVUELVE LAS PALABRAS DE LOS SUBNODOS QUE COMIENCEN CON MAYUSCULA'''        
  def internasMayusculasAlfabetico(self):
       if not self.estaVacio():
          return self.raiz.internasMayusculas()
       else:
          print("El Arbol esta vacio")
      
          
      
      
                
            
        
           
        
    
    