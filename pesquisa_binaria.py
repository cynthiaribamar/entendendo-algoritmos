# A pesquisa binária é um algoritmo baseado no paradigma de divisão e consquista
# Ela recebe uma lista ordenada e o item buscado
# Se o item está presente na lista, o algoritmo retorna sua localização, senão retorna none

def pesquisa_binaria(lista, item):
    
    baixo = 0
    alto = len(lista) - 1 #4
    
    while baixo <= alto:
        meio = (baixo + alto) / 2
        print(meio)
        chute = lista[int(meio)] #2
        
        if chute == item:
            return meio
        
        if chute > item:
            alto = meio - 1 #1
            
        else:
            baixo = meio + 1
            
    
minha_lista = [1,3,5,7,9]
print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, 19))
