from rx import of, operators as op
import random


variavel = of(2,1,2,3,4,5,6,6,3)
	
resultRandom = variavel.pipe(
	op.map(lambda a: a+random.random())) # map é uma função de transformação utilizada para transformar uma função obtida em um observer aplicando uma função a cada item (nesse caso vai servir para aplicar a função random)

resultFilter = variavel.pipe(
	op.filter(lambda i: i <= 5)) #filtro para aparecer somente os números menores ou iguais a 5.

resultDistinct = variavel.pipe( #filtro para não aparecer números repetidos.
	op.distinct())

resultFirst = variavel.pipe( #filtro para aparecer apenas o primeiro elemento.
	op.first())

resultLast = variavel.pipe( #filtro para aparecer apenas o último elemento.
	op.last())




print("Valores com decimais randômicos: ")
subscriber1 = resultRandom.subscribe(lambda i: print("Resultado: {0}".format(i)))

print("Valores menores ou iguais a 5: ")
subscriber2 = resultFilter.subscribe(lambda i: print("Resultado: {0}".format(i)))

print("Valores sem repetição: ")
subscriber3 = resultDistinct.subscribe(lambda i: print("Resultado: {0}".format(i)))

print("Primeiro elemento: ")
subscriber4 = resultFirst.subscribe(lambda i: print("Resultado: {0}".format(i)))

print("Último elemento: ")
subscriber4 = resultLast.subscribe(lambda i: print("Resultado: {0}".format(i)))




