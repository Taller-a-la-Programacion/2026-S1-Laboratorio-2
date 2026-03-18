# LABORATORIO 02 

## Descripción General
- El siguiente laboratorio consiste en una serie de ejercicios para el desarrollo de programación en **sintaxis de Python**, además de evaluación de conceptos vistos en clases anteriores.
- El objetivo de este laboratorio está en el uso de la **condicional IF**, **creación de funciones**, **validación de los parámetros** y recuerde que en cada función que desarrollen agregar los **comentarios** (nombre, parámetros entrada, salida y restricciones).
- Finalizado el laboratorio subir el archivo con el nombre de **Laboratorio02.py**, la entrega cierra a las **11:20 am del 18 de marzo del 2026** y será a través del Github Classroom.
- Deben ser muy claros con los mensajes de error que programen en su código.
- Como observación, no solo se califica el correcto funcionamiento del código sino también las validaciones, comentarios y el uso correcto de las funciones o bloques de código permitidos


## contarGruposDeDigitos(num, grupo)
- Construir una función que retorne la cantidad de grupos de **N** dígitos llamado **grupo** que compone el número de parámetro **num** de entrada.
- El parámetro **num** y **grupo** deben ser entero
- El largo o total de dígitos de **num** debe ser menor o igual al número del parámetro **grupo**
- Por ejemplo : 
  -  num = 256145 grupo=2, el resultado a retornar es 3, porque hay 3 grupos de 2 dígitos,  25, 61 y 45
  -  num = -245 grupo = 3, el resultado a retornar es 1, porque hay 1 grupo de 3 dígitos,  solo -245
  -  num = 15 y grupo = 1, el resultado a retornar es 2, porque hay de 2 dígitos agrupados en un dígito

```python
>>>contarGruposDeDigitos(256145, 2)     
3
>>>contarGruposDeDigitos(-245, 3)     
1
>>>contarGruposDeDigitos(15, 1)     
2
>>>contarGruposDeDigitos('abc', 2)     
'Error: Solo es permitido número de tipo entero'

>>>contarGruposDeDigitos(2589, 5)     
'Error: No hay grupo de 5 digitos, excede la cantidad de dígitos'

```
## numeroCapicua(num)
Por definición, la capicúa (del catalán cap i cua, "cabeza y cola") es cualquier número que se lee igual de izquierda a derecha que de derecha a izquierda (ej. 101, 852258, 96369, 11). Aunque se aplica principalmente a cifras, el término destaca la simetría numérica, a menudo referida como un tipo de palíndromo numérico. 

La función **numeroCapicua(num)** retornará **True** o **False**, retornará **True** en el caso de que el número sea capicúa y **False** del caso de contrario

```python
>>>numeroCapicua(101)
True
>>>numeroCapicua(1801)
False
>>>numeroCapicua(8)
True
>>>numeroCapicua('abc')     
'Error: Solo es permitido número de tipo entero'
```
