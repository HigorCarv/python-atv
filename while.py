def lin ():
    print('--------------------')


cont = 0
while cont < 3:
    Nome = str(input('Qual o nome do aluno: '))
    Nota1 = int(input('Nota1: '))
    Nota2 = int(input('Nota2: '))
    media = (Nota1 + Nota2)/2
    print(f'Média final: {media}')
    lin()
    if media >= 7:
        print('Aprovado')
    else:
        print ('Reprovado')
    lin()
    cont += 1
    print(cont)
    