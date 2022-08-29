# ABAIXO IMPORTANDO O RANDOM, FUNDAMENTAL PARA GERAR A LISTA DO CICLO3
import random


# --- LISTAS  ---

lista_nomes = ["Laura", "Pedro", "João", 
                "Vinicius", "Carlos", "Maria",
                "Leonardo", "Ana", "Daniela",
                "Marcos", "Wesley", "Luiz",
                "Daiane", "Felipe", "Teodoro",
                "Helena", "Natalia", "Beatriz",
                "Eduardo", "Caio"
]

ciclo1 = [  ["Laura","Pedro","João","Vinicius"],
            [ "Carlos", "Maria", "Leonardo", "Ana"],
            [ "Daniela", "Marcos", "Wesley","Luiza"],
            [ "Daiane", "Felipe", "Teodoro", "Helena"],
            [ "Natalia","Beatriz", "Eduardo", "Caio"] 
            
]

ciclo2 = [  [ "Teodoro", "Daiane", "Luiza" ],
            [ "Carlos", "João", "Helena"   ],
            ["Daniela","Pedro","Caio"       ],
            ["Leonardo","Maria","Laura"     ],
            ["Beatriz","Marcos","Vinicius"   ],
            ["Natalia","Felipe","Eduardo"   ],
            ["Ana","Wesley"                 ]

]            

# ---- VARIAVEIS ----

# Abaixo  groupSize é um Variável que define o tamanho da equipe
# Para listar novos grupos de 3, 4, 5 ... integrantes
# basta alterar o valor de groupSize    EX: grupos de 4 integrantes groupSize = 4
groupSize = 2  

# Abaixo variável conta os indices da lista
listSize = len(lista_nomes)  

# Abaixo int converte o resultado da divisão(float) em tipo inteiro
# numberofGroup recebe o valor de quantos grupos serão criados   
# len() tem a função de contar quantos elementos tem a lista
numberofGroup = int(len(lista_nomes) / groupSize)

# Abaixo o contatdor do while
i = 1

#declaração da lista do ciclo3
ciclo3 = []
# ----- FIM de Variáveis -----


# ------- inicio do while -------

# while é usado para criar a lista do ciclo3
# contador i menor ou igual ao numero de grupos possiveis calculado na linha 47
while i <= numberofGroup:  

    # abaixo newlist é declarada para receber a nova lista criada pelo random.sample
    # randon.sample(x,y) recebe 2 argumentos o primeiro a lista que vai ser trabalhada 
    # o segundo argumento recebe o tamanho da lista que será gerada
    # random.sample(x,y) foi escolhido pelo motivo da possibilidade de trabalhar com string
    newList = random.sample(lista_nomes, groupSize)
    i += 1

    # abaixo a lista ciclo3 recebe newList pelo metodo append
    # cada loop do while newList recebe uma nova lista do random.sample(x,y)
    ciclo3.append(newList)
    print(ciclo3)
    
# ------ fim do while ------
