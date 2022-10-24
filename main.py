import random
from claseTablaHash import TablaHash

if __name__ == '__main__':
    objTabla = TablaHash()
    for i in range(1000):
        elemento = random.randint(1000, 2500)
        objTabla.insertar(elemento)
    objTabla.recorrer()
    elemento_buscar = int(input('Ingrese un elemento a buscar: '))
    posicion = objTabla.buscar(elemento_buscar) 
    if posicion != None:
        print('Elemento encontrado en el bucket de la posicion: {}'.format(posicion))
    else:
        print('Elemento no encontrado')
    print('Cantidad de buckets desbordados: {}'.format(objTabla.getBucketsDesbordados()))
    print('Cantidad de buckets subocupados: {}'.format(objTabla.getBucketsSubocupados()))