class Nodo:
    def __init__(self, valor):
        self.hijoIzq = None
        self.hijoDer = None
        self.valor = valor


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def obtenerRaiz(self):
        return self.raiz

    def agregarNodos(self, nodo_valor):
        if (self.raiz == None):
            self.raiz = Nodo(nodo_valor)
        else:
            self._agregarNodos(nodo_valor, self.raiz)

    def _agregarNodos(self, nodo_valor, nodo_raiz):
        if (nodo_valor < int(nodo_raiz.valor)):
            if (nodo_raiz.hijoIzq != None):
                self._agregarNodos(nodo_valor, nodo_raiz.hijoIzq)
            else:
                nodo_raiz.hijoIzq = Nodo(nodo_valor)
        else:
            if (nodo_raiz.hijoDer != None):
                self._agregarNodos(nodo_valor, nodo_raiz.hijoDer)
            else:
                nodo_raiz.hijoDer = Nodo(nodo_valor)

    def encontrar(self, nodo_valor):
        if(self.raiz != None):
            return self._encontrar(nodo_valor, self.raiz)
        else:
            return None

    def _encontrar(self, nodo_valor, nodo_raiz):
        if (nodo_valor == int(nodo_raiz.valor)):
            return nodo_raiz
        elif (nodo_valor < nodo_raiz.valor and nodo_raiz.hijoIzq != None):
            return self._encontrar(nodo_valor, nodo_raiz.hijoIzq)
        elif(nodo_valor > nodo_raiz.valor and nodo_raiz.hijoDer != None):
            return self._encontrar(nodo_valor, nodo_raiz.hijoDer)

    def imprimirArbol(self):
        if(self.raiz != None):
            self._imprimirArbol(self.raiz)

    def _imprimirArbol(self, nodo_raiz):
        if(nodo_raiz != None):
            self._imprimirArbol(nodo_raiz.hijoIzq)
            print(str(nodo_raiz.valor) + ' ')
            self._imprimirArbol(nodo_raiz.hijoDer)

    def eliminarArbol(self):
        self.raiz = None

if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.agregarNodos(3)
    arbol.agregarNodos(5)
    arbol.agregarNodos(7)
    arbol.agregarNodos(9)
    arbol.agregarNodos(4)
    arbol.agregarNodos(10)
    arbol.agregarNodos(15)
    arbol.agregarNodos(21)

    #Imprimir arbol binario
    arbol.imprimirArbol()

    #Encontrar elemento
    print(arbol.encontrar(5))

    #Eliminar arbol binario
    arbol.eliminarArbol()
    print("--------------")

    arbol.agregarNodos(4)
    arbol.agregarNodos(2)
    arbol.agregarNodos(13)
    arbol.agregarNodos(14)
    arbol.agregarNodos(20)

    #Imprimir arbol binario
    arbol.imprimirArbol()

    #Encontrar elemento
    print(arbol.encontrar(5))

#Arboles binarios de busqueda
#Arboles AVL