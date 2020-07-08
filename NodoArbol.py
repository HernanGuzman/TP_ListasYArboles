from TP_ArbolYListas.ListaEnlazada import ListaEnlazada
class NodoArbol:
  def __init__(self, listaPaginas, palabra = None ):
    self.palabra = palabra
    self.listaPaginas = listaPaginas
    self.izquierda = None
    self.derecha = None

  def tieneIzquierda(self):
    return self.izquierda != None

  def tieneDerecha(self):
    return self.derecha != None

  def esHoja(self):
      return not self.tieneDerecha() and not self.tieneIzquierda()
  
  

  def preOrden(self):
    print(self.palabra)
    if self.tieneIzquierda():
      self.izquierda.preOrden()
    if self.tieneDerecha():
      self.derecha.preOrden()

  def inOrden(self):
    if self.tieneIzquierda():
      self.izquierda.preOrden()
    print(self.palabra)
    if self.tieneDerecha():
      self.derecha.preOrden()

  def postOrden(self):
    if self.tieneIzquierda():
      self.izquierda.preOrden()
    if self.tieneDerecha():
      self.derecha.preOrden()
    print(self.palabra)
    
  def existeNodo(self, palabraBuscar):
      encontrado = None
      if self.palabra == palabraBuscar:
          encontrado = self
      else:
          if palabraBuscar < self.palabra:
              if self.tieneIzquierda():
                  encontrado = self.izquierda.existeNodo(palabraBuscar)
          else:
              if self.tieneDerecha():
                  encontrado = self.derecha.existeNodo(palabraBuscar)
      return encontrado
          
      
  def insertar(self, nuevoNodo):
    if nuevoNodo.palabra < self.palabra:
      if self.tieneIzquierda():
          self.izquierda.insertar(nuevoNodo)
      else:
          self.izquierda = nuevoNodo
    else:
      if self.tieneDerecha():
          self.derecha.insertar(nuevoNodo)
      else:
          self.derecha = nuevoNodo
          
  def palabrasDePagina(self, dirWeb, listaPalabras):
      if self.listaPaginas.buscarDato(dirWeb):
          listaPalabras.append(self.palabra) 
      if self.tieneIzquierda():
          self.izquierda.palabrasDePagina(dirWeb, listaPalabras)
      if self.tieneDerecha():
          self.derecha.palabrasDePagina(dirWeb, listaPalabras)
      return listaPalabras 
  
  '''DEVUELVE EL GRADO DEL NODO
  0 SI ES UNA HOJA
  1 SI TIENE IZQUIERDA O DERECHA
  Y 2 SI TIENE IZQUIERDA Y DERECHA''' 
  def grado(self):
    grado = 0
    if self.tieneIzquierda():
      grado += 1
    if self.tieneDerecha():
      grado += 1
    return grado

  '''DEVUELVE LA ALTURA DE UN NODO'''
  def altura(self):
    altura = 0
    '''SI EL GRADO ES DOS. LO QUE SIGNIFICA QUE EL NODO TIENE DERECHA E IZQUIERDA
    LLAMO A LA FUNCION RECURSIVA PARA SABER CUAL DE LOS DOS SIGUIENTE TIENE LA ALTURA MAYOR'''
    if self.grado() == 2:
        altura = 1 + max(self.izquierda.altura() , self.derecha.altura())
    elif self.tieneIzquierda():
      altura = 1 + self.izquierda.altura()
    elif self.tieneDerecha():
      altura = 1 + self.derecha.altura()
    return altura

  '''MIENTRAS EL NODO TENGA DERECHA CAMBIA EL DATO MAXIMO'''
  def buscaMaximo(self):
    dato = None
    if self.tieneDerecha():
      dato = self.derecha.buscaMaximo()
    else:
      dato = self
    return dato  
  '''BUSCA EL MAXIMO VALOR DE LA PARTE IZQUEIRDA DEL NODO LO QUE DARA EL PREDECESOR'''
  def predecesor(self):
    predecesor = None
    if self.tieneIzquierda():
      predecesor = self.izquierda.buscaMaximo()
    return predecesor

  '''DEVUELVE LA LISTA DE NODOS QUE SE ENCUENTRAN EN EL NIVEL ENVIADO'''
  def nivelALista(self, nivel, listaNivel, nivelNodo = 0):
    if nivelNodo == nivel:
      listaNivel.append(self.palabra)
    else:
      if self.tieneDerecha():
        self.derecha.nivelALista(nivel, listaNivel, nivelNodo+1)
      if self.tieneIzquierda():
        self.izquierda.nivelALista(nivel, listaNivel, nivelNodo+1)
  


  def buscaPadre(self, palabra):
    nodoHijo = None
    nodoPadre = None
    lado = None
    if palabra < self.palabra:
      if self.tieneIzquierda():
        if self.izquierda.palabra == palabra:
          nodoHijo = self.izquierda
          nodoPadre = self
          lado = "izq"
        else:
          nodoHijo, nodoPadre, lado = self.izquierda.buscaPadre(palabra)
    else:
      if self.tieneDerecha():
        if self.derecha.palabra == palabra:
          nodoHijo = self.derecha
          nodoPadre = self
          lado = "der"
        else:
          nodoHijo, nodoPadre, lado = self.derecha.buscaPadre(palabra)
    return nodoHijo, nodoPadre, lado
   
  def eliminar(self, palabra):
    nodoEliminar, nodoPadre, lado = self.buscaPadre(palabra)  ##lado = "izq" / "der"
    if nodoEliminar != None:
      if nodoEliminar.grado() == 2:
        nodoPred = nodoEliminar.predecesor()
        self.eliminar(nodoPred.palabra)
        nodoPred.izquierda = nodoEliminar.izquierda
        nodoPred.derecha = nodoEliminar.derecha
        if lado == "izq":
          nodoPadre.izquierda = nodoPred
        else:
          nodoPadre.derecha = nodoPred
      elif nodoEliminar.tieneIzquierda():
        if lado == "izq":
          nodoPadre.izquierda = nodoEliminar.izquierda
        else:
          nodoPadre.derecha = nodoEliminar.izquierda
      elif nodoEliminar.tieneDerecha():
        if lado == "izq":
          nodoPadre.izquierda = nodoEliminar.derecha
        else:
          nodoPadre.derecha = nodoEliminar.derecha
      else:
        if lado == "izq":
          nodoPadre.izquierda = None
        else:
          nodoPadre.derecha = None  
  '''FUNCION QUE ELIMINA UNA PAGINA WEB EN EL ARBOL
  1_ BUSCA SI SE ENCUENTRA LA PAGINA EN EL NODO RAIZ
  2_ SI SE ENCUENTRA ELIMINO LA PAGINA LLAMANDO A LA FUNCION ELIMINAR DATO, PASANDOLE LA DIRECCION WEB
  3_ SE CONSULTA SI EL NODO TIENE IZQUIERDA PARA LLAMAR RECURSIVAMENTE A LA FUNCION Y CONTINUAR CON LA BUSQUEDA
  4_ IGUAL QUE EL ANTERIOR PERO CONSULTANDO SI TIENE DERECHA'''
  def eliminarPagina(self, dirWeb):
      if self.listaPaginas.buscarDato(dirWeb):
          self.listaPaginas.eliminarDato(dirWeb)
      if self.tieneIzquierda():
          self.izquierda.eliminarPagina(dirWeb)
      if self.tieneDerecha():
          self.derecha.eliminarPagina(dirWeb)
          
  '''FUNCION QUE DEVUELVE LAS PALABRAS EN EL NODO QUE TENGAN IGUAL O MAYOR CANTIDAD DE CARACTERES QUE LOS SOLICITADOS
  1_ CONSULTA SI LA CANTIDAD DE CARACTERES ES MAYOR O IGUAL A LOS SOLICITADO
  2_ SI LA PALABRA CUMPLE CON LA CONDICION SE AGREGA A LA LISTA QUE SE DEVOLVERA
  3_ SE CONSULTA SI EL NODO TIENE IZQUIERDA PARA LLAMAR RECURSIVAMENTE A LA FUNCION Y CONTINUAR CON LA BUSQUEDA
  4_ IGUAL QUE EL ANTERIOR PERO CONSULTANDO SI TIENE DERECHA'''        
  def cantidadPalabras(self, cant, listaPalabras):
      if len(self.palabra) >= cant:
          listaPalabras.append(self.palabra)
      if self.tieneIzquierda():
          self.izquierda.cantidadPalabras(cant, listaPalabras)
      if self.tieneDerecha():
          self.derecha.cantidadPalabras(cant, listaPalabras)
      return listaPalabras.len()
  
  '''FUNCION QUE DEVUELVE LAS PALABRAS EN EL NODO QUE TENGAN IGUAL O MAYOR NUMERO DE PAGINAS QUE LAS SOLICITADAS
  1_ CONSULTA SI LA CANTIDAD DE PAGINAS ES MAYOR O IGUAL A LOS SOLICITADO
  2_ SI LA CANTIDAD DE PAGINAS CUMPLE CON LA CONDICION SE AGREGA A LA LISTA QUE SE DEVOLVERA
  3_ SE CONSULTA SI EL NODO TIENE IZQUIERDA PARA LLAMAR RECURSIVAMENTE A LA FUNCION Y CONTINUAR CON LA BUSQUEDA
  4_ IGUAL QUE EL ANTERIOR PERO CONSULTANDO SI TIENE DERECHA'''
  def cantidadPalabrasConPaginas(self, cant, listaPalabras):
      if self.listaPaginas.len() >= cant:
          listaPalabras.append(self.palabra)
      if self.tieneIzquierda():
          self.izquierda.cantidadPalabrasConPaginas(cant, listaPalabras)
      if self.tieneDerecha():
          self.derecha.cantidadPalabrasConPaginas(cant, listaPalabras)
      return listaPalabras.len()
  
  '''FUNCION QUE DEVUELVE LOS SUBARBOLES EN LOS QUE LA PALABRA COMIENZA CON MAYUSCULA
  1_ CONSULTA SI EL NODO NO ES UNA HOJA
  2_ SI EL NODO NO ES UNA HOJA, TOMO LA PRIMERA LETRA Y CONSULTO SI ESTA EN MAYUSCULA
  3_ SI ESTA EN MAYUSCULA LO AGREGO A LA LISTA QUE SE DEVOLVERA
  4_ SE CONSULTA SI EL NODO TIENE IZQUIERDA PARA LLAMAR RECURSIVAMENTE A LA FUNCION Y CONTINUAR CON LA BUSQUEDA
  5_ IGUAL QUE EL ANTERIOR PERO CONSULTANDO SI TIENE DERECHA'''
  def internasMayusculas(self, listaPalabras = ListaEnlazada()):
      if not self.esHoja():
          '''TOMO EL PRIMER CARACTER PARA COMPARAR'''
          letra = self.palabra[0]
          if letra.isupper():
              listaPalabras.appendOrd(self.palabra)
      if self.tieneIzquierda():
          self.izquierda.internasMayusculas(listaPalabras)
      if self.tieneDerecha():
          self.derecha.internasMayusculas(listaPalabras)
      return listaPalabras
  
  
      
     

  def imprimirArbol(self, palabra):
    if self.tieneizquierda():
      palabra.node(str(self.izquierda.palabra), str(self.izquierda.palabra))
      palabra.edge(str(self.palabra), str(self.izquierda.palabra))
      self.izquierda.imprimirArbol(palabra)
    else:
      palabra.node("Vacio" + str(self.palabra)+"l","Vacio")
      palabra.edge(str(self.palabra), "Vacio" + str(self.palabra)+"l")

    if self.tieneDerecho():
      palabra.node(str(self.derecha.palabra), str(self.derecha.palabra))
      palabra.edge(str(self.palabra), str(self.derecha.palabra))
      palabra.derecha.imprimirArbol(palabra)
    else:
      palabra.node("Vacio" + str(self.palabra)+"r","Vacio")
      palabra.edge(str(self.palabra), "Vacio" + str(self.palabra)+"r")