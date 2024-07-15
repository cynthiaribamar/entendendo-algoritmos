# A pesquisa binária é um algoritmo baseado no paradigma de divisão e consquista
# Ela recebe uma lista ordenada e o item buscado
# Se o item está presente na lista, o algoritmo retorna sua localização, senão retorna none

def pesquisa_binaria(lista, item):
    
    baixo = 0
    alto = len(lista) - 1 #4
    
    while baixo <= alto:
        
        meio = (baixo + alto) // 2 #2 o // é divisão inteira, para não resultar em um float 
        print(f"meio: {meio}")
        chute = lista[meio] #lista[2] chute: 5
        
        if chute == item: #false
            return meio
        
        if chute > item: #true
            alto = meio - 1 # 4 - 2 = 1
            
        else: 
            baixo = meio + 1
            
            
    
minha_lista = [1,3,5,7,9]
print(f"Endereço do item: {pesquisa_binaria(minha_lista, 3)}")
print(f"Endereço do item: {pesquisa_binaria(minha_lista, 19)}")
print(f"Endereço do item: {pesquisa_binaria(minha_lista, 7)}")

\