#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PySide import QtGui, QtCore
from MainWindow import Ui_MainWindow 
import Controller

class MTuring1Cinta:

    def __init__(self, transiciones, estados, alfabeto):
        self.inicial = ""  # estado inicial
        self.final = ""  # estado final
        self.estados = estados  # arreglo de estados
        self.transiciones = transiciones  # arreglo de transiciones
        self.alfabeto = alfabeto  # alfabeto

    def agregaEstIni(self, estIni):
        if(estIni != ""):
            if (estIni in self.estados):
                self.inicial = estIni
                salida = "Estado Inicial agregado"
            else:
                salida = "Ingrese un estado Inicial Valido"
        else:
            salida = "Ingrese algun estado Inicial"
        return salida

    def agregaEstFin(self, estFin):
        if(estFin != ""):
            if (estFin in self.estados):
                self.final = estFin
                salida = "Estado Final agregado"
            else:
                salida = "Ingrese un estado Final Valido"
        else:
            salida = "Ingrese algun estado Final"
        return salida

    def validaTrans(self, trans):
        tuplas = trans.split(';')
        salida = ""
        for i in tuplas:
            #print "i:", i
            cantidad = i.count(',')
            if(cantidad > 4):
                salida = "Hay Transiciones de mas de 5 elementos"
            if(cantidad < 4):
                salida = "Hay Transiciones de menos de 5 elementos"
            if (('D' not in i) and ('I' not in i)):
                salida = "Faltan Direcciones de Lectura"
        tupla = [5]
        tupla2 = [5]
        if (salida == ""):
            for i in tuplas:
                tupla = i.split(',')
                for j in tuplas:
                    tupla2 = j.split(',')
                    if ((tuplas.index(i) != tuplas.index(j)) and tupla[0] == tupla2[0] and tupla[1] == tupla2[1]):  # si se repite una combinacion de estado y simbolo en las transiciones
                        salida = "Hay Transiciones con el mismo estado y simbolo de lectura"
        if(salida == ""):
            salida = "Transiciones Ingresadas"
        return salida

    def aceptaPalabra(self, pala):
        palabra = list(pala)
        salidaLectura =""
        for i in range(len(palabra)):
            if(palabra[i] == 'B'):
               salida = "La palabra no necesita el simbolo blanco 'B' al final."
               return salida, salidaLectura
               exit()
        palabra.append('B')
        #palabra.append('B') #Posiblemente necesite una 2da B al final para ciertos algoritmos
        correcto = True
        for i in palabra:
            if (i not in self.alfabeto):
                correcto = False
        if (correcto):
            print correcto
            print "impresiones"
            i = 0
            simboloCinta = palabra[i]
            estadoActual = self.inicial
            posSimbolo = self.alfabeto.index(simboloCinta)
            posEstadoActual = self.estados.index(estadoActual)
            transicion = self.transiciones[posEstadoActual][posSimbolo]
            while (estadoActual != self.final and transicion != "_" and i < len(palabra)):  # mientras no se llegue al estado final, a una transicion vacia, o fin de la cadena
                estadoSiguiente = transicion[0]
                escribo = transicion[1]
                direccionAvance = transicion[2]

                #print estadoActual
                #print "palabra:"
                #print palabra
                #print " estadoActual:"

                print "-> ",
                salidaLectura += "->    "
                j = 0
                for j in range(len(palabra)):
                    print palabra[j],
                    salidaLectura += str(palabra[j])+"    "
                print ""
                salidaLectura += "\n       "
                salidaLectura += "      "*i+estadoActual+"\n"
                salidaLectura += "\n"
                print "  ",
                print "  "*i,
                print estadoActual
                print ""

                palabra[i] = escribo  # escribo el simbolo en la palabra de la cinta"
                estadoActual = estadoSiguiente  # paso al siguiente estado

                if (direccionAvance == 'D'): # sumo o resto segun direccion de avance
                    i = i + 1
                else:
                    i = i - 1
                if (i < len(palabra)):  # para no salirse del arreglo de la palabra
                    simboloCinta = palabra[i]
                posSimbolo = self.alfabeto.index(simboloCinta)
                posEstadoActual = self.estados.index(estadoActual)
                transicion = self.transiciones[posEstadoActual][posSimbolo]  # ubico la siguiente transicion
            print "-> ",
            j = 0
            for j in range(len(palabra)):
                print palabra[j],
            print ""
            print "  ",
            print "  "*i,
            print estadoActual
            print ""

            if(estadoActual == self.final):
            	salida = "Palabra Aceptada"
            else:
                salida = "Palabra Rechazada"
        else:
            salida = "La Palabra contiene un simbolo No reconocido por la MT"
        return salida,salidaLectura

