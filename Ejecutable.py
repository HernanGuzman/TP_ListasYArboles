from TP_ArbolYListas.ArbolBuscador import ArbolBuscador
from TP_ArbolYListas.ListaEnlazada import ListaEnlazada
Buscador1 = ArbolBuscador()

'''INSERTAR PALABRAS'''
Buscador1.insertarPalabra("Maestria", "www.unahur.com.ar")
Buscador1.insertarPalabra("Maestria", "www.UNSAM.com.ar")
Buscador1.insertarPalabra("Ingenieria", "www.unahur.com.ar")
Buscador1.insertarPalabra("Ingenieria", "www.UNSAM.com.ar")
Buscador1.insertarPalabra("Universidad", "www.unahur.com.ar")
Buscador1.insertarPalabra("Universidad", "www.UNSAM.com.ar")
Buscador1.insertarPalabra("Telecomunicaciones", "www.Claro.com.ar")
Buscador1.insertarPalabra("Telecomunicaciones", "www.Movistar.com.ar")
Buscador1.insertarPalabra("Telecomunicaciones", "www.UNSAM.com.ar")
'''Buscador1.insertarPalabra("Telecomunicaciones", "www.UNSAM.com.ar")'''

'''INSERTAR PAGINAS'''
listaDePalabras = ListaEnlazada()
listaDePalabras.append("Vegetariano")
listaDePalabras.append("Vegano")
listaDePalabras.append("Ovo-Vegano")
paginaWeb = "www.elvegano.com.ar"
Buscador1.insertarPagina(listaDePalabras, paginaWeb)

'''BUSCAR PALABRAS'''
listaDePalabras = ListaEnlazada()
listaDePalabras.append("Telecomunicaciones")
listaDePalabras.append("Ingenieria")
listaEncontrada = Buscador1.buscarPalabras(listaDePalabras)
listaEncontrada.recPre()

'''PALABRAS DE PAGINAS'''
dirWeb = "www.UNSAM.com.ar"
listaEncontrada = Buscador1.palabrasDePagina(dirWeb)
listaEncontrada.recPre()

'''ELIMINAR PALABRA'''
Buscador1.eliminarPalabra("Vegetariano")

'''ELIMINAR PAGINA'''
Buscador1.eliminarPagina("www.Claro.com.ar")
Buscador1.eliminarPagina("www.unahur.com.ar")

'''ESTA BALANCEADO'''
print(Buscador1.estaBalanceado())

'''CANTIDAD TOTAL DE PALABRAS'''
print(Buscador1.cantidadTotalPalabras(15))

'''ESTA BALANCEADO'''


'''PAGINAS EN NIVEL'''
listaEncontrada = Buscador1.paginasEnNivel(2)
listaEncontrada.recPre()

'''CANTIDAD DE PAGINAS'''
print(Buscador1.cantidadPalabrasMasUsadas(1))

'''INTERNAS MAYUSCULAS ALFABETICAMENTE'''
listaEncontrada = Buscador1.internasMayusculasAlfabetico()
listaEncontrada.recPre()



 
