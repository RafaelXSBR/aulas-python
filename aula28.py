"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
Nome=input('Digite seu Nome: ')
idade=input('Digite sua Idade: ')
if not Nome and  not idade:
    print ("Desculpe, você deixou campos vazios.")
else:
    print (f"Seu nome é {Nome}")
    print (f"Seu nome invertido é {Nome[::-1]}")
    print ('Seu nome tem ', str(len(Nome)) ,'letras')
    print (f"A primeira letra do seu nome é {Nome[0]}")
    print (f"A última letra do seu nome é {Nome[len(Nome)-1]}")
