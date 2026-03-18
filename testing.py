#NO MODIFICAR ESTE ARCHIVO

import Laboratorio02;
import pytest;

##################################################################
def test_lab_1():
    assert Laboratorio02.contarGruposDeDigitos(15, 1) == 2

def test_lab_2():
    assert Laboratorio02.contarGruposDeDigitos(256145, 2) == 3

def test_lab_3():
    assert Laboratorio02.contarGruposDeDigitos(-245, 3) == 1

def test_lab_4():
    assert isinstance(Laboratorio02.contarGruposDeDigitos('abc', 2), str) == isinstance("Error: Solo es permitido número de tipo entero", str)

def test_lab_5():
    assert isinstance(Laboratorio02.contarGruposDeDigitos(2589, 5) , str) == isinstance("Error: No hay grupo de 5 digitos, excede la cantidad de dígitos", str)

##################################################################

def test_lab_6():
    assert Laboratorio02.numeroCapicua(101)  == True
    
def test_lab_7():
    assert Laboratorio02.numeroCapicua(1801)  == False
    
def test_lab_8():
    assert Laboratorio02.numeroCapicua(8)  == True
    
def test_lab_9():
    assert isinstance(Laboratorio02.numeroCapicua('abc') , str)  == isinstance("Error: Solo es permitido número de tipo entero", str)
