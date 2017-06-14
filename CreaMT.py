#!/usr/bin/python
# -*- coding: utf-8 -*-

#Estructura Estado_Actual;Simbolo_Actual_Del_Cabezal;Estado_Siguiente;
#Simbolo_a_Escribir;Direccion_De_Avance
#D: movimiento derecha - I: Movimiento izquierda

#esta libreria tiene los metodos para obtener y llenar datos para ser usados en la MT


def llenarTransiciones(estados, alfabeto, ent): # lleno la matriz de transiciones luego de validarla
    n = len(estados)
    m = len(alfabeto)  # incluye el blanco
    print "Longitud estados = ",+n
    print "Longitud alfabeto = ",+m 
    transVacia = [["_" for x in xrange(m)] for x in xrange(n)] #Se reparo error de dimensión por indices
    transiciones = transVacia
    #for w in transiciones:
    #    print w
    posFil = 0
    posCol = 0
    aux = separaTupla(ent)
    #print "aux:", aux
    for i in aux:
        aux2 = separaElem(i)
        cont1 = 0
        cont2 = 0
        for a in estados:  # Obteniendo posiciones de cada transicion
            if aux2[0] == a:
                posFil = cont1
            cont1 = cont1 + 1
        for b in alfabeto:
            if aux2[1] == b:
                posCol = cont2
            cont2 = cont2 + 1
        #print posFil,posCol
        transiciones[posFil][posCol] = aux2[2], aux2[3], aux2[4]  # Agrego a la matriz
    print ""
    print "Matriz de Transiciones:"
    i = 0
    j = 0
    k = 0
    tmp = "   |"
    for i in range(len(alfabeto)):
        tmp += "    "
        tmp += alfabeto[i]
        tmp += "    "
    print tmp
    for k in range(len(transiciones)):
        w = transiciones[k]
        tmp = ""
        tmp += estados[k]
        tmp2 = "   |"
        tmp2 = tmp2[-4+len(estados[k]):]
        tmp += tmp2
        for i in range(len(w)):
            #print "w i: ", w[i]
            if w[i] != "_":
                tmp += "("
                for k in range(len(w[i])):
                    tmp += w[i][k]
                    tmp += ","
                tmp = tmp[:-1]
                tmp += ") "
            else:
                tmp += "[      ] "
        print tmp
    return transiciones


def obtEstadosAlfabeto(entrada0, final):  # filtro los estados y el elfabeto de la entrada
    tuplas = separaTupla(entrada0)
    stringEstados = ""
    stringAlfabeto = ""
    for i in tuplas:
        tupla = separaElem(i)
        #print tupla
        estadoActual = tupla[0]
        if (stringEstados.find(estadoActual) == -1):
            if (stringEstados == ""):
                stringEstados += estadoActual
            else:
                stringEstados += ','+estadoActual #Modificacion. para agregar ",+Elementos" en vez de "Elemento+,"" y forzar un siguiente vacio
        estadoSiguiente = tupla[2]
        if (stringEstados.find(estadoSiguiente) == -1):
            stringEstados += ','+estadoSiguiente # no verifico vacio ya que para este caso siempre habra ya un estado en la cadena
        simboloActual = tupla[1]
        if (stringAlfabeto.find(simboloActual) == -1):
            if (stringAlfabeto == ""):
                stringAlfabeto += simboloActual
            else:
                stringAlfabeto += ','+simboloActual
        simboloOtraPos = tupla[3] #en caso de que el simbolo solo aparezca en la posicion 4
        if (stringAlfabeto.find(simboloOtraPos) == -1):
            stringAlfabeto += ','+simboloOtraPos
    estados = stringEstados.split(',')
    alfabeto = stringAlfabeto.split(',')

    estados = sorted(estados)
    alfabeto = sorted(alfabeto)
    tmp_list_1 = []
    tmp_list_2 = []
    i = 0
    for i in alfabeto:
        if i.isupper():
            tmp_list_1.append(i)
        else:
            tmp_list_2.append(i)
    alfabeto = tmp_list_2 + tmp_list_1

    if final in estados:
        estados.remove(final)
        estados.append(final)
    if 'B' in alfabeto:
        alfabeto.remove('B')
    alfabeto.append('B')

    print ""
    print "Vector Estados:",
    #print estados
    tmp = "Q = {"
    j = 0
    for j in range(len(estados)):
        tmp += estados[j]
        tmp += ", "
    tmp=tmp[:-2]
    tmp += "}"
    print tmp
    print ""

    print "Vector Alfabeto:",
    #print alfabeto
    tmp = "G = {"
    j = 0
    for j in range(len(alfabeto)):
        tmp += alfabeto[j]
        tmp += ", "
    tmp=tmp[:-2]
    tmp += "}"
    print tmp

    print ""
    return (estados, alfabeto)


def separaTupla(entrada1):
    separaTupla = entrada1.split(';')
    return (separaTupla)


def separaElem(entrada2):
    separaElem = entrada2.split(',')
    return (separaElem)




